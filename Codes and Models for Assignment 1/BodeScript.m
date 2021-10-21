%%
clc
clear all
close all

K = 1;
Kp = 6;
Ti = 4;
Td = 1;
p = 10;

P = tf([K],[1 p]);

figure(1)
bode(P)
title('Plant Bode Diagram')

C_PID = tf([Kp*Ti*Td Kp*Ti Kp],[Ti 0]);

figure(2)
bode(C_PID)
title('PID Controller Bode Diagram')

figure(3)
bode(C_PID*P)
title('PID Controller-Plant Cascade Bode Diagram')

PlantWithPID = tf([Kp*Ti*Td Kp*Ti Kp],[Ti p*Ti 0]);

figure(4)
bode(PlantWithPID)
title('PID Controller-Plant Bode Diagram')

C_PI = tf([Kp*Ti Kp],[Ti 0]);

figure(5)
bode(C_PI)
title('PI Controller Bode Diagram')

figure(6)
bode(C_PI*P)
title('PI Controller-Plant Cascade Bode Diagram')

C_PD = tf([Kp*Td Kp],[1]);

figure(7)
bode(C_PD)
title('PD Controller Bode Diagram')

figure(8)
bode(C_PD*P)
title('PD Controller-Plant Cascade Bode Diagram')