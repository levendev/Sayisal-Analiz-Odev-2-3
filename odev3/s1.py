import math

def fonksiyon(x):
    return 4*math.e**(-0.5*x)-x

def turevFonksiyon(x):
    return -2*math.e**(-0.5*x)-1

a=2
for i in range(0,4):
    yeniFonksiyon=a-(fonksiyon(a) / turevFonksiyon(a))
    a=yeniFonksiyon

print(a)