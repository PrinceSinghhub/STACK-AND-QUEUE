from array import *
n=int(input("Enter your stack rang: "))
a=array('i',[])
def push(a):
    val=int(input("Enter element: "))
    a.append(val)
    print("Push sucessfull complete")
def pop(a):
    val=a.pop()
    print("The poped item is:",val)

def peek(a):
    val=len(a)-1
    val1=a[val]
    print("the peek value is:",val1)
    print("Stack is: ",a)

def greatest(a):
    # a=list(a)
    val = max(a)
    print("the max element is: ",val)
    print("The Stack is: ", a)

def minitem(a):
    val = min(a)
    print("the max element is: ",val)
    print("The Stack is: ",a)

def search(a):
    if len(a) > 0:
        val = int(input("Enter Element: "))
        for i in a:
            if i == val:
                print("Sucessfully search elament: ", val)
                print("The Stack is: ", a)
                break
        else:
            print("Sorry Element are not found")

while True:
    print("1: push\n2: pop\n3: peek\n4: Display\n5: Biggest element in Stack\n6:Smallest element in Stack\n7: check element\n8: exit")
    option = int(input("COMMAND: "))
    if option == 1:
        if len(a)<=n:
            push(a)
        else:
            print("Sorry stack in Overflow\nplease pop the element")

    if option == 2:
        if len(a)==0:
            print("Sorry stack in empty")
        else:
            pop(a)

    if option == 3:
        if len(a)==0:
            print("Sorry stack in empty")
        else:
            peek(a)

    if option ==4:
        if len(a)==0:
            print("Sorry stack is empty")
            print("Stack is: ",a)
        else:
            print("Stack is: ",a)

    if option == 5:
        if len(a)==0:
            print("Sorry Stack is empty")
        else:
            greatest(a)

    if option == 6:
        if len(a) == 0:
            print("Sorry Stack is empty")
        else:
            minitem(a)
    if option == 7:
        if len(a) == 0:
            print("Sorry Stack is empty")
        else:
            search(a)

    if option == 8:
        print("Thankyou")
        break