#짝수
def funEven(num):
##    if num%2 == 0:
##        return True
##    else:
##        return False  
    return num%2 == 0           #헐

#홀수
def funOdd(num):
    if num%2 == 1:
        return True
    else:
        return False  



print(funEven(7))
print(funOdd(7))