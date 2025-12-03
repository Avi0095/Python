queue=[]
def display():
    if not queue:
        print("No element in queue")
    else:
        for i in queue:
            print(f"<{i}>",end=" ")
    print(f"\nNumber of element in queue is:{len(queue)}")
def enqueue():
    element=int(input("Enter the value you add :"))
    queue.append(element)
    display()
def dequeue():
    if not queue:
        print("No element in queue")
    else:
        element=queue.pop(0)
        print(f"{element} is dequeued from queue")
    display()
def peek():
    if not queue:
        print("Nothing to queue")
    else:
        print(f"Front element is{queue[0]}")
    display()
while True:
    print("\nChoose an operation")
    print("1.enqueue")
    print("2.dequeue")
    print("3.peek")
    print("4.exit")
    choose=int(input("Enter your choice:"))
    if choose==1:
        enqueue()
    elif choose==2:
        dequeue()
    elif choose==3:
        peek()
    elif choose==4:
        print("Exiting....")
        break
    else:
        print("Invalid choice")

 