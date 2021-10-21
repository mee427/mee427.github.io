# Imported libraries
from scipy import signal
import matplotlib.pyplot as plt

# Given parameters
K = 1
Kp = 6
Ti = 4
Td = 1
p = 10

P = signal.TransferFunction([K],[1,p])
w1, mag1, phase1 = signal.bode(P)

plt.figure()
plt.semilogx(w1, mag1)    # Bode magnitude plot
plt.title("Plant Bode Magnitude Diagram")
plt.grid()
plt.figure()
plt.semilogx(w1, phase1)  # Bode phase plot
plt.title("Plant Bode Phase Diagram")
plt.grid()

C_P = signal.TransferFunction([K],[1])
w2, mag2, phase2 = signal.bode(C_P)

plt.figure()
plt.semilogx(w2, mag2)    # Bode magnitude plot
plt.title("P Controller Bode Magnitude Diagram")
plt.grid()
plt.figure()
plt.semilogx(w2, phase2)  # Bode phase plot
plt.title("P Controller Bode Phase Diagram")
plt.grid()

C_PI = signal.TransferFunction([Kp*Ti,Kp],[Ti,0])
w3, mag3, phase3 = signal.bode(C_PI)

plt.figure()
plt.semilogx(w3, mag3)    # Bode magnitude plot
plt.title("PI Controller Bode Magnitude Diagram")
plt.grid()
plt.figure()
plt.semilogx(w3, phase3)  # Bode phase plot
plt.title("PI Controller Bode Phase Diagram")
plt.grid()

C_PD = signal.TransferFunction([Kp*Td,Kp],[1])
w4, mag4, phase4 = signal.bode(C_PD)

plt.figure()
plt.semilogx(w4, mag4)    # Bode magnitude plot
plt.title("PD Controller Bode Magnitude Diagram")
plt.grid()
plt.figure()
plt.semilogx(w4, phase4)  # Bode phase plot
plt.title("PD Controller Bode Phase Diagram")
plt.grid()

C_PID = signal.TransferFunction([Kp*Ti*Td,Kp*(Ti+Td),Kp],[Ti,0])
w5, mag5, phase5 = signal.bode(C_PID)

plt.figure()
plt.semilogx(w5, mag5)    # Bode magnitude plot
plt.title("PID Controller Bode Magnitude Diagram")
plt.grid()
plt.figure()
plt.semilogx(w5, phase5)  # Bode phase plot
plt.title("PID Controller Bode Phase Diagram")
plt.grid()

num_c = [Kp*Ti*Td,Kp*(Ti+Td),Kp]
den_c = [Ti,0]

num_p = [K]
den_p = [1,p]

cascade_PID = signal.TransferFunction(signal.convolve(num_c,num_p),signal.convolve(den_c,den_p))
w6, mag6, phase6 = signal.bode(cascade_PID)

plt.figure()
plt.semilogx(w6, mag6)    # Bode magnitude plot
plt.title("PID Controller Cascade Bode Magnitude Diagram")
plt.grid()
plt.figure()
plt.semilogx(w6, phase6)  # Bode phase plot
plt.title("PID Controller Cascade Bode Phase Diagram")
plt.grid()

cascade_PID_byhand = signal.TransferFunction([Kp*Ti*Td,Kp*(Ti+Td),Kp],[Ti,Ti*p,0])
w7, mag7, phase7 = signal.bode(cascade_PID_byhand)

plt.figure()
plt.semilogx(w7, mag7)    # Bode magnitude plot
plt.title("PID Controller Cascade Bode Magnitude Diagram (by hand)")
plt.grid()
plt.figure()
plt.semilogx(w7, phase7)  # Bode phase plot
plt.title("PID Controller Cascade Bode Phase Diagram (by hand)")
plt.grid()
plt.show()