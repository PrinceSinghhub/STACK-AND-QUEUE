a=[]
# todo inqueue function
def inqueue(a,val):
    a.append(val)
    print("the inqueue suncessfully complete")

# todo dequeue function
def dequeue(a):
    val=a.pop(0)
    print("the dequeue element is: ",val)
    print("Queue is: ",a)

# todo peek function
def peek(a):
    val = a[0]
    print("The peek element: ",val)
    print("Queue is: ", a)

# todo display function
def display(a):
    print("Queue is: ", a)

while True:
    print("1: Inqueue\n2: Dequeue\n3: peek\n4: Display\n5: Exit ")
    option = int(input("COMMAND: "))
    if option == 1:
        val = int(input("Enter Your Element: "))
        inqueue(a,val)

    if option == 2:
        if len(a)==0:
            print("Sorry your Queue is Empty")
        else:
            dequeue(a)

    if option == 3:
        if len(a)==0:
            print("Sorry your Queue is Empty")
        else:
            peek(a)

    if option == 4:
        if len(a)==0:
            print("Sorry your Queue is Empty")
            print("Queue is: ", a)
        else:
            display(a)

    if option == 5:
        print("Thankyou")
        break