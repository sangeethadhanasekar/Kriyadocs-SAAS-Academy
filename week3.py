'''#Given a list of words, return a dictionary where the keys are the words and
# the values are the number of times the word appears in the list.

di={}
ip=input("enter word's to be in the list =")
nested=ip.split()
print(nested)
for i in nested:
    if i in di.keys():
        di[i]+=1
    else:
        di[i]=1
print("final answer dictionary: ",di)'''

'''#Given a list of words, return a dictionary 
# where the keys are the words and the values are the number of letters in the word.

di={}
def func_2(nested):
    for i in nested:
     di[i]=len(i)
    return di

ip=input("enter word's to be in the list =")
nested=ip.split()
print("final answer dictionary: ", func_2(nested))'''

'''#Given a list of words, return a dictionary where 
# the keys are the words and the values are the number of vowels in the word.
di={}
def vowels_count(nested):
    for i in nested:
        for words in i:
            if (words.lower() in ['a','e','i','o','u']):
                try:
                  di[i]+=1
                except:
                    di[i]=1
    return di

ip=input("enter word's to be in the list =")
nested=ip.split()
print("final answer dictionary: ",vowels_count(nested))'''


# Python3 code to demonstrate working of
# Bigrams Frequency in String
# Using Counter() + generator expression
from collections import Counter
	
# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# Bigrams Frequency in String
# Using Counter() + generator expression
res = Counter(test_str.split(' ')for idx in range(len(test_str) - 1))

# printing result
print("The Bigrams Frequency is : " + str(dict(res)))
