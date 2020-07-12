i = int(input('Enter the number of inputs you want: '))
x= 0
h= 1
period = []
while x < i:
    period.append(int(input('Enter the period: ')))
    h=1
    for n in range(period[x]+1):
        if n == 0:
            h= 1
        elif not(n%2 == 0):
            h=h*2
        else:
            h= h+1
    print(h)
    x= x+1 


