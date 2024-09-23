"""#write a program to print all combinations that a+b+c=n, n=10 (eg:1 1 8,1 2 7 ..)
list1 = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i+j+k == 10:
                list1.append((i,j,k))
#print(list1)
                
#write a program if str='aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbb' for every five a's replace with one 'a'
import re
def replace_a(string):
    pattern = "a{4}"
    k = re.sub(pattern,'a',string)
    return k


string = 'aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbb'
#print(replace_a(string))
#Write a Program for email address using regular expressions
def email(str):
    #pattern = '^[a-zA-Z0-9-@]*+@[a-zA-Z0-9-]+(\.[a-z|A-Z]{2,})'
    pattern = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    if re.fullmatch(pattern,str):
        print("vaild")
    else:
        print("invalid")
str = "email4prasanth@gmail.com"
email(str)
#{"files":[{"id":1,"name":"xyz.jpg","owner":"abc@gmail.com"}], "count":10}. Print the value of owner
def extract(dict1):
    for k,v in dict1.items():
        for k1,v1 in v[0].items():
           if k1=="owner":
               print(v[0][k1])
       
dict1= {"files":[{"id":1,"name":"xyz.jpg","owner":"abc@gmail.com"}]}
extract(dict1) 
# Find the maximum and second maximum in the list without using max function
def max_logic(X):
    for i in range(1,len(X)):
        if X[i-1]>X[i]:
           X[i-1],X[i]=X[i],X[i-1]
    #print(X)
    return X
list1 = [5,3,8,6,4,2,1]
print(max_logic(list1)[-1])

def secondmax(X):
    y = max_logic(X)[:-1]
    return max_logic(y)
    
list1 = [5,3,8,6,4,2,1]
print(secondmax(list1)[-1])  
#Sort the list without creating another list?
def sortlist(X):
    for i in range(1,len(X)+1):
        for j in range(i):
            if X[i-1]<X[j]:
                X[i-1],X[j]=X[j],X[i-1]
    return X
list1 = [5,3,8,6,4,2,1]
print(sortlist(list1))

#
dict = {(3,4,8):4,(5,6,9):3} 
print('output:', dict[5,6,9]) 
print('output:', dict[(5,6,9)]) 


list1 = ["one", "two", "three"]
list2 = ["1","2","3"]
dict1 = {}
for i in range(3):
    dict1[list1[i]]=list2[i]
print(dict1)

dict1 = {'one': '1', 'two': '2', 'three': '3'}
dict2 = {'one1': '1', 'two2': '2', 'three3': '3'}
dict3 = dict1|dict2
print(dict3)
dict4 = {**dict1,**dict2}
print(dict4)"""
#Python Lambda Function with List Comprehension
list1 = [2,3,4,8,1]
k = list(map(lambda x:x*x,list1))
print(k)
list1 = [lambda arg=x:arg*10 for x in range(1,5)]
print(list1)
for i in list1:
    print(i())
list1 = [2,3,4,8,1]
print(list(filter(lambda x:(x%2!=0),list1)))
list1 = [2,3,4,8,1]
print(list(map(lambda x:x**2,list1)))
animals = ['dog', 'cat', 'parrot', 'rabbit']
print(list(map(lambda  x:x.upper()  ,animals)))


#maximum
import functools
lis = [1, 3, 5, 6, 2 ]
print(functools.reduce(lambda a,b:a if a>b else b,lis))




