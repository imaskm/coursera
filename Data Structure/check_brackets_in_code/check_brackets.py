# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([next,i])
            #print(opening_brackets_stack)


        if next in ")]}":

            if( len(opening_brackets_stack) == 0):
                return i+1

            # Process closing bracket, write your code here
            if( next == ")" ):
                if(opening_brackets_stack.pop()[0] != "(" ):
                    return i+1
            elif( next == "}" ):
                
                if(opening_brackets_stack.pop()[0] != "{" ):
                    return i+1
            elif(next == "]"  ):
                
                if(opening_brackets_stack.pop()[0] != "[" ):
                    return i+1
    #print(opening_brackets_stack)
    if(len(opening_brackets_stack) == 0 ):
        return "Success"

    else:

        return (opening_brackets_stack[0][1]+1)


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
