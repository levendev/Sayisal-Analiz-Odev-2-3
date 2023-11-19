def f(x):
    return x*x*x-2*x*x-5

max=4
min=2

for i in range(0,4):
    orta=(max+min)/2
    if(f(orta)*f(min)>0):
        min=orta
    else:
        max=orta

print(orta)