import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.integrate import odeint
	
t_out = []
u_out = []
def P_Control_model(x,t,ref,Kp):
    global u_out, t_out
    y = x[0]
    dydt = x[1]
    dy2dt2 = x[2]
    t_out.append(t)
    u = Kp*(ref-y)
    u_out.append(u)
    dy3dt3 = u-3*dy2dt2-3*dydt-y
    return [dydt,dy2dt2,dy3dt3]
	
t_out = []
u_out = []
def PI_Control_model(x,t,ref,Kp,Ki):
    global u_out, t_out
    y = x[0]
    dydt = x[1]
    dy2dt2 = x[2]
    errorIntegral = x[3]
    t_out.append(t)
    error = (ref - y)
    u = Kp*(ref-y)+Ki*errorIntegral
    u_out.append(u)
    dy3dt3 = u-3*dy2dt2-3*dydt-y
    return [dydt,dy2dt2,dy3dt3,error]
	
print('Starting...')
ref = 1
t1 = np.linspace(0,25,100)

Kp = 1
x_1 = odeint(P_Control_model,[0,0,0],t1,args=(ref,Kp))
y_1 = x_1[:,0]
t1_out = t_out
u_1 = u_out

t_out = []
u_out = []
Kp = 2
x_2 = odeint(P_Control_model,[0,0,0],t1,args=(ref,Kp))
y_2 = x_2[:,0]
t2_out = t_out
u_2 = u_out

t_out = []
u_out = []
Kp = 5
x_5 = odeint(P_Control_model,[0,0,0],t1,args=(ref,Kp))
y_5 = x_5[:,0]
t5_out = t_out
u_5 = u_out

t_out = []
u_out = []
Kp = 3
Ki = 0.5
x_3_05 = odeint(PI_Control_model,[0,0,0,0],t1,args=(ref,Kp,Ki))
y_3_05 = x_3_05[:,0]
t3_05_out = t_out
u_3_05 = u_out

plt.figure(1)
plt.plot(t1,y_1,'r-',linewidth=1,label='y when Kp = 1')
plt.plot(t1,y_2,'b-',linewidth=1,label='y when Kp = 2')
plt.plot(t1,y_5,'g-',linewidth=1,label='y when Kp = 5')
plt.legend()
plt.grid()
# plt.show()

plt.figure(2)
plt.plot(t1_out,u_1,'r-',linewidth=1,label='u when Kp = 1')
plt.plot(t2_out,u_2,'b-',linewidth=1,label='u when Kp = 2')
plt.plot(t5_out,u_5,'g-',linewidth=1,label='u when Kp = 5')
plt.legend()
plt.grid()

plt.figure(3)
plt.plot(t1,y_3_05,'r-',linewidth=1,label='y when Kp = 3, Ki = 0.5')
plt.legend()
plt.grid()

plt.show()