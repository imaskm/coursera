def gcd(a,b):

    if(b == 0 ):
        return a

    else:
        print(b,a%b)
        return gcd(b,a%b)





if __name__ == "__main__":
    a,b= [int(x) for x in input().split()]
    print(gcd(a,b))
