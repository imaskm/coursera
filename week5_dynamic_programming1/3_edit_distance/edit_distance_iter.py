# Uses python3
def edit_distance(s, t,sl,tl,l):

    for i in range(sl+1):

        for j in range(tl+1):

            if(i==0):
                l[i][j]=j
            elif(j==0):
                l[i][j]=i

            elif( s[i-1]==s[j-1]):
                l[i][j] = l[i-1][j-1]

            else:
                l[i][j]= min(l[i][j-1],l[i-1][j],l[i-1][j-1])+1

    return l[sl][tl]



if __name__ == "__main__":
    s,t=input(), input()
    #d=dict()
    l = list()

    for i in range(len(s)+1):
        l.append([])
        for j in range(len(t)+1):
            l[i].append(None)

    #print(l)

    print(edit_distance(s,t,len(s),len(t),l))
    print(l)
