a=[]
# todo push methode
def push(a,val):
    a.append(val)
    print("Sucessfully push complete")

# todo pop methode
def popitem(a):
    val = a.pop()
    print("Pop element is: ",val)

# todo peek methode
def peek(a):
    z=len(a)
    val = a.pop(z-1)
    print(val)

# todo Display methode
def display(a):
    print(f"This Stak is: {a}")
while True:
    print("1: push\n2: pop\n3: peek\n4: Display\n5: Exit ")
    option = int(input("COMMAND: "))
    if option == 1:
        val=int(input("Enter Element: "))
        push(a,val)
    if option ==2:
        if len(a) == 0:
            print("sorry stack in empty")
        elif len(a) > 0:
            popitem(a)

    if option == 3:
        if len(a) == 0:
            print("sorry stack in empty")
        elif len(a) > 0:
            peek(a)

    if option == 4:
        if len(a) == 0:
            print("sorry stack in empty")
            print(a)
        elif len(a) > 0:
            display(a)

    if option == 5:
        print("thankyou for use me")
        break