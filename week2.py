#Given a list of numbers, find the sum of all the elements in the list.
li=[]
num=int(input("enter number of elements that list must contain = "))
for i in range(num):
    ip=int(input("enter element {} of list=".format(i+1)))
    li.append(ip)
print("the given list=",li)
print("sum of all the elements in the list =",sum(li))


#Given a list of strings, find the longest string in the list.
li_2=[]
n={}
num=int(input("enter number of elements that list must contain = "))
for i in range(num):
    ip=str(input("enter string {} of list=".format(i+1)))
    li_2.append(ip)
    n[ip]=len(ip)
print("the given list=",li_2)   
sort_n=sorted(n.items(), key=lambda x: x[1] , reverse=True)
print("the longest string in the list=",sort_n[0][0])


#Given a list of numbers, create a new list that contains only the even numbers from the original list.
li=list()
even=[]
num=int(input("enter number of elements that list must contain = "))
for i in range(num):
    ip=int(input("enter element {} of list=".format(i+1)))
    li.append(ip)
    if ip%2==0:
        even.append(ip)
print("the given list=",li)
print("list that contains only the even numbers from the original list=",even)  

#Given a list of strings, create a new list that contains only the strings that start with the letter 'a'.
li_3=[]
alpha=[]
num=int(input("enter number of elements that list must contain = "))
for i in range(num):
    ip=str(input("enter string {} of list=".format(i+1)))
    li_3.append(ip)
    if ip[0]=='a':
        alpha.append(ip)
print("the given list=",li_3)
print("new list that contains only the strings that start with the letter 'a'=",alpha)  

#Given a list of nested lists, create a new list that contains the sum of all the values in the nested lists.
parent=[]
sum_list=[]
num=int(input("enter number of nested list that a list must contain = "))
for i in range(num):
    ip=input("enter elements of nestedlist {} of =".format(i+1))
    nested=ip.split()
    parent.append([int(x) for x in nested])
for i in parent:
    sum=0
    for j in i:
        sum=sum+int(j)
    sum_list.append(sum)
print("Given a list of nested lists= ",parent)
print("a new list that contains the sum of all the values in the nested lists",sum_list)

# Print a nested list
parent=[]
num=int(input("enter number of nested list that a list must contain = "))
for i in range(num):
    ip=input("enter elements of nestedlist {} of =".format(i+1))
    nested=ip.split()
    parent.append(nested)
print("the given nested list is = ",parent)

# Flatten a nested list
parent=[]
num=int(input("enter number of nested list that a list must contain = "))
for i in range(num):
    ip=input("enter elements of nestedlist {} of =".format(i+1))
    nested=ip.split()
    parent.append(nested)
flat_list = [num for sublist in parent for num in sublist]
print(flat_list)

#Convert a nested list to a string
parent=[]
num=int(input("enter number of nested list that a list must contain = "))
for i in range(num):
    ip=input("enter elements of nestedlist {} of =".format(i+1))
    nested=ip.split()
    parent.append(nested)
outlst = [' '.join([str(c) for c in lst]) for lst in parent]
print("given nested list=",parent)
print("converted a nested list to a string=",outlst)