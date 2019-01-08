# Uses python3
def edit_distance(s, t,sl,tl,l):
    #print("s:",sl)
    #print("t:",tl)
    #print(sl,tl)
    #if(l[sl-1][tl-1] != None ):
        #return l[sl-1][tl-1]

    if(sl==0):
        l[sl][tl]=tl
        return tl
    elif(tl==0):
        l[sl][tl]=sl
        return sl
    if(l[sl][tl] !=0 ):
        return l[sl][tl]
    if(s[sl-1]==t[tl-1]):
        l[sl][tl]= edit_distance(s,t,sl-1,tl-1,l)
        return l[sl][tl]
    else:
        l[sl][tl] =  min(edit_distance(s,t,sl-1,tl,l ),edit_distance(s,t,sl,tl-1,l),edit_distance(s,t,sl-1,tl-1,l))+1
        #print(sl,tl,l[sl][tl])
        return l[sl][tl]
    

if __name__ == "__main__":
    s,t=input(), input()
    #d=dict()
    l = list()

    for i in range(len(s)+1):
        l.append([])
        for j in range(len(t)+1):
            l[i].append(0)

    #print(l)

    print(edit_distance(s,t,len(s),len(t),l))
    #print(l)
