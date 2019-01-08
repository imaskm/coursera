# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    

    d = []
    for i in range(len(weights)):
        d.append( [weights[i],values[i]/weights[i]] )
    
    d.sort(key=lambda x: x[1],reverse=True)
    
    c = 0
    
    for i  in d:

        key=i[0]
        val=i[1]
        if(capacity==0):
            break

        if(key <= capacity):
            value+=val*key
            capacity-=key
        else:
            value+=val*(capacity)
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))

    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
