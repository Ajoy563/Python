stack=[]
queue=[]
while(1):
    print("\n1. Stack\n2. Queue\n3. Exit\n")
    c=int(input("Enter your choice: "))
    if c==1:
        print("\n1. Insert\n2. Delete\n3. Display\n")
        c2=int(input("Enter your choice: "))
        if c2==1:
            e=int(input("\nEnter an element to insert: "))
            stack.append(e)
        elif c2==2:
            if stack==[]:
                print("\nStack is Empty!")
            else:
                p=stack.pop()
                print(f"\n{p} is Popped from the Stack.")
        else:
            if stack==[]:
                print("\nStack is Empty!")
            else:
                print("Stack is: ",stack)
    elif c==2:
        print("\n1. Enqueue\n2. Dequeue\n3. Display\n")
        c2=int(input("Enter your choice: "))
        if c2==1:
            e=int(input("\nEnter an element to insert: "))
            queue.append(e)
        elif c2==2:
            if queue==[]:
                print("\nUnderflow.")
            else:
                p=queue.pop(0)
                print(f"\n{p} is Poped from the Queue.")
        else:
            if queue==[]:
                print("\nQueue is empty!")
            else:
                print("\nQueue is: ", queue)
    else:
        exit()