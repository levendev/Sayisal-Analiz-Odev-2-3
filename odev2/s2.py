def f(x):
    return x*x*x+4*x*x-10

max=2
min=1

for i in range(0,4):
    orta=(max+min)/2
    if(f(orta)*f(min)>0):
        min=orta
    else:
        max=orta

print(orta)