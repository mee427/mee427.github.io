import numpy as np
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
	
# You should implement odeint function here.
# odeint function solve the differential equation with a initial conditions of return value and given time array
# You may use numpy linspace function in order to create time array
# Usage of odeint Example: 
# x = odeint(P_Control_model,[0,0,0],t1,args=(ref,Kp))
# Plotting Example: 
# plt.plot(t1,x[:,0],'r-',linewidth=1,label='y when Kp = given value')
# Do not forget to add function plt.show() at the end

# Define ref and Kp before calling the function

# YOUR CODE HERE