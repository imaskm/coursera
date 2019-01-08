# Uses python3
#import math,decimal
#decimal.getcontext().prec = 300
#def calc_fib(n):

#    return math.ceil( ( (decimal.Decimal(1.6)**decimal.Decimal(n)-decimal.Decimal(-.61)**decimal.Decimal(n)) // (decimal.Decimal(5).sqrt() ) ) )

#n = int(input())
#print(int(calc_fib(n+2)-1)%10)
def fibbo(n):
    if(n<=1):
        return n
    curr = 0
    prev = 1
    #print(n)
    for i in range(n):
        #print(curr,end=" ")
        prev,curr=curr,curr+prev

    return curr



    
if __name__ == '__main__':

    n = int(input())
    #fib = {0:0,1:1}
    print( (fibbo(n+2)-1)%10  )
    #print(fib)

