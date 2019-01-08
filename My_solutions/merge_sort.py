def merge(arr,l,m,r):
    l_ar = arr[l:m+1]
    r_ar = arr[m+1:]
    i = 0
    j= 0
    k=0
    #arr=[]
    while(i<len(l_ar) and j< len(r_ar)):

        if(l_ar[i] <= r_ar[j] ):
            arr[k] = l_ar[i]
            k+=1
            i+=1
            
        else:
            arr[k] = r_ar[j]
            j+=1
            k+=1

    while(i< len(l_ar) ):
        arr[k] = l_ar[i]
        i+=1
        k+=1


    while(j< len(r_ar)):
        arr[k]=r_ar[j]
        k+=1
        j+=1

def merge_sort(arr,l,r):
    if(l < r):
        m = (l+r)//2

        print(arr[l:r])
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

arr = list(map(int,input().split() ))

print(arr)

merge_sort(arr,0,len(arr))

print(arr)
