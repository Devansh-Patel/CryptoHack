a=int(input('enter a'))
n=int(input('enter n'))

for i in range(1,a):
    if ((a-i)%n==0):
        print(i)
        break
