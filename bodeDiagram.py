# Imported libraries
from scipy import signal
import matplotlib.pyplot as plt

# Given parameters
K = 1
Kp = 6
Ti = 4
Td = 1
p = 10

# Plant example
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
# plt.show()

# Cascade example
num_c = [Kp]			# Numerator of P Controller
den_c = [1]				# Denominator of P Controller

num_p = [K]				# Numerator of plant
den_p = [1,p]			# Denominator of plant

cascade_P = signal.TransferFunction(signal.convolve(num_c,num_p),signal.convolve(den_c,den_p))
w2, mag2, phase2 = signal.bode(cascade_P)

plt.figure()
plt.semilogx(w2, mag2)    # Bode magnitude plot
plt.title("P Controller Cascade Bode Magnitude Diagram")
plt.grid()
plt.figure()
plt.semilogx(w2, phase2)  # Bode phase plot
plt.title("P Controller Cascade Bode Phase Diagram")
plt.grid()
plt.show()