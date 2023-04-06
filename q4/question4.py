def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    return n*factorial(n-1)


if __name__ == "__main__":
    for i in range(15):
        print("{}일떄의 factorial 값 : {}".format(i,factorial(i)))
        
