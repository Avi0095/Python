def TOH(n,A,B,C):
    if n>0:
        TOH(n-1,A,C,B) #recursive call
        print(f"move disc {n}  from {A} to {C}")
        TOH(n-1,B,A,C)
n=int(input("Enter the number of disks:"))
TOH(n,"A","B","C")

