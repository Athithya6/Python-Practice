'''
#to find squares for values upto given input
n=int(input("Enter the limit:\n"))
for i in range(0,n):
    print(i*i)
    print("\n")

#to find runner-up
def runner_up():
    l=[]
    n=int(input("How many participants are there:\n"))
    for i in range(0,n):
        m=int(input("Enter the scores of each participant:\n"))
        l.append(m)
    l.sort()
    print("The runner-up score is: ",l[-2])
    

runner_up()

#to convert lower to upper and upper to lower in a given string
s=input("Enter any string:\n")
s1=""
for i in s:
    if i.isupper()==True:
        s1+=i.lower()
    else:
        s1+=i.upper()

print("The resultant string is:\n")
print(s1)

l=[]
m=int(input("How many elements do you want to enter in the list:\n"))
for j in range(m):
    k=int(input("Enter the element:\n"))
    l.append(k)
print(l)
print("The odd indexed elements are:\n")
for x in range(0,len(l)):
    if(x%2!=0):
        print(l[x])
'''

        


