def sayed(a,b,c):
    sum=0
    mul=1
    a=a
    b=b
    c=c
    if a%2==0 and b%2==0 and c%2==0 :
        sum=a+b+c
        print("sum:",sum)
        return sum
    elif a%2!=0 and b%2!=0 and c%2!=0:
            mul=a*b*c
            print("mul",mul)
            return mul
    elif a%2!=0 and b%2!=0 and c%2==0:
            total=a+b-c
            print("total ",total)
            return total
    elif a%2==0 and b%2==0 and c%2!=0:
            total=a+b-c
            print("total",total)
            return total
sayed(22,44,35)        