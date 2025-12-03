stack = []

def display_stack():
    if not stack:
        print("Stack is empty.")
    else:
        print("\nStack (top → bottom):")
        for i in  reversed(stack):
            print("|",i,"|")
        print("‾‾‾‾‾‾‾‾‾")
    print(f"Number of elements in stack: {len(stack)}\n")

def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(f"{element} pushed into stack.")
    display_stack()

def pop():
    if not stack:
        print("Stack is empty, nothing to pop.")
    else:
        element = stack.pop()
        print(f"Popped element: {element}")
    display_stack()

def peek():
    if not stack:
        print("Stack is empty, nothing to peek.")
    else:
        print(f"Top element is: {stack[-1]}")
    display_stack()

while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        push()
    elif choice == "2":
        pop()
    elif choice == "3":
        peek()
    elif choice == "4":
        print("Exiting...")
        #break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
