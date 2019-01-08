def partition(arr,l,r):
    
    x = arr[l]
    j = l

    for i in range(l+1,r):

        if(arr[i] <= x ):
            j+=1
            if( i != j ):
                arr[j],arr[i]=arr[i],arr[j]

    arr[l],arr[j]=arr[j],arr[l]

    return j

def quick_sort(arr,l,r):
    if(l>=r):
        return
    m = partition(arr,l,r)

    quick_sort(arr,l,m)
    quick_sort(arr,m+1,r)


arr = list(map(int , input().split()))

quick_sort(arr,0,len(arr))
print(arr)
