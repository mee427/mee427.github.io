#include <16F877A.h>
#device ADC=10
#include <stdlib.h>
#FUSES NOWDT  NOBROWNOUT NOLVP XT,NOPROTECT,NOPUT, NODEBUG, NOCPD
#use delay(crystal=20000000)
#use rs232 (baud=9600,xmit=PIN_C6, rcv=PIN_C7, parity=N, stop=1) // configuretion for serial communication
#define DIRECTION PIN_B1
float refAngle = 90.0f;
float revAngle = 0.0f;
unsigned long int result_1;
signed long controlOut=0;
unsigned long int pwmOut;
float error = 0.0f;
float prevError = 0.0f;
float integral = 0.0f;
float derivative = 0.0f;
float dt = 0.02f;
unsigned long int Z;
unsigned long int T;
float kp = 0.5f;
float ki = 0.1f;
float kd = 0.01f;

int16 elapsedTime;
int16 remainingTime;

#int_timer0
void tmr_int()    {
 set_timer0(236);
 Z++;
 T++;
 /*if (Z >= 10)    {
    error=refAngle-revAngle;
    integral=integral+dt*error;
    derivative = (error-prevError)/dt;
    controlOut = error*kp+ki*integral+kd*derivative;
    Z = 0;
    prevError = error;
 }*/
}

void main()  {

 port_b_pullups(TRUE);
 enable_interrupts(GLOBAL);
 clear_interrupt(int_ext);
 setup_timer_0(RTCC_INTERNAL | RTCC_DIV_256);
 set_timer0(236);
 enable_interrupts(int_timer0);
 enable_interrupts(int_ext);
 setup_adc_ports(AN0_AN1_AN3); //A0 A1 A3 are configured for analog input pin
 setup_adc(ADC_CLOCK_DIV_32); //enable ADC and set clock for ADC
 setup_ccp1(CCP_PWM); //4kHz PWM signal output at CCP1 pin 17
 setup_timer_2(T2_DIV_BY_16, 255, 1);
 
 set_tris_b(0x00);
 output_b(0x00);
 
 Z = 0;
 
   while(TRUE)    {
      
      set_adc_channel(0); // next analog reading will be from channel 0
      delay_us(10); //allow time after channel selection and reading
      result_1 = read_adc(); //start and read A/D
      delay_us(10); //allow time after channel selection and reading
      revAngle = result_1*0.247-39.452;
      
      error=refAngle-revAngle;
      integral=integral+dt*error;
      derivative = (error-prevError)/dt;
      controlOut = error*kp+ki*integral+kd*derivative;
      prevError = error;
      
      if(controlOut > 12)   {
         controlOut = 12;
      }
      if(controlOut <-12 )    {
         controlOut = -12;
      }
      
      if (controlOut > 0) {
         output_high(DIRECTION);
         pwmOut = 85.25*controlOut;
      }
      else {
         output_low(DIRECTION);
         pwmOut = -85.25*controlOut;
      }
      
      set_pwm1_duty(pwmOut); //set pulse-width during which signal is high
      //delay_ms(5);

      // ADD EXTRAS BELOW;
      //printf("error:%f  Wref:%f Wact:%f",error,Wref,Wact);
      //printf("%ld\n",elapsedTime);
      printf("%f\n",revAngle);
      elapsedTime = Z;
      remainingTime = 20 - elapsedTime;
      if (remainingTime > 0) {
         //printf("%lu,%f\n",T,revAngle);
         delay_ms(remainingTime);
      }
      else {
         // RETURN ERROR
      }
      Z = 0;
      
   }
}

