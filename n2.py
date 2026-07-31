def toh(n,s,d,a):
    if n==1:
        print("move disk 1 from source",s," to destination",d)
        return
    toh(n-1,s,a,d)
    print("move disk",n,"from source",s,"to destination",d)
    toh(n-1,a,d,s)
n=int(input("enter the no of disk : "))
toh(n,'s','a','d')
print("program")
