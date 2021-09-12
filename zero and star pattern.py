
#using while function
def while_func(n):
    i=1
    while i<=n:
        j=1
        while j<=n:
            if i==j:
                print("*",end="")
            else:
                print("0",end="")
            j=j+1
        print("*",end="")
        j=j-1
        while j>=1:
            if i==j:
                print("*",end="")
            else:
                print("0",end="")
            j=j-1
        i=i+1
        print()
n=int(input())
while_func(n)

