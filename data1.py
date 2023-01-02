i=0
mean=0
var=0
while i==0:
    i += 1
    num = int(input("enter the number:"))
    if num>=0:
        print(f'the mean is {num}  and variance is {0}')
        mean+=num
    else:
        exit()
while i==1:
    i+=1
    num = int(input("enter the number:"))
    if num >= 0:
        mean1=mean+(num-mean)/i
        var1=(num-mean)**2/i
        mean=mean1
        var=var1
        print(f'the mean is {mean}  and variance is {var}')
    else:
        exit()
while i>=2:
    num = int(input("enter the number:"))
    if num >= 0:
        i += 1
        mean2=mean+(num-mean)/i
        var2 = ((i - 2) / (i - 1)) * (var)  + ((num - mean) *(num - mean)) / i
        mean = mean2
        var=var2
        print(f'the mean is {mean}  and variance is {var}')
    else:
        break








