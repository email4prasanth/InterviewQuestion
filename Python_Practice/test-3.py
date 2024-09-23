# 1.	Write a program convert all the vowels to uppercase for the given input string.
# print(chr(65))
# print(chr(90+32))

"""string = 'PytHon'
def upper(string):
    newstring =''
    for i in string:
        if 90<=ord(i)<=122:#small letters
            i = chr(ord(i)-32)
            newstring =newstring+ i
        elif 65<=ord(i)<=90:
            newstring = newstring+i
        else:
            print("invalid input")
    return newstring

print(upper(string))

# 2.	Write a program reverse a given input string
string = 'PYTHON CODE'
print(string[::-1])

 # 3.	Write a program reverse the given input list
list1 = [5,6,3,4]
list2 = []
for i in range(len(list1)-1,-1,-1):
     list2.append(list1[i])
print(list2)

#4.	Write a program print the Fibonacci series   till 100
def fibbnocci(x):
    u = 0
    v = 1
    c = 0
    list1 = []
    if x<=0:
        print('invalid')
    elif x==0:
        list1.append(0)
        return list1
    elif x==1:
        list1.append(0)
        list1.append(1)
        list1.append(1)
        return list1
    else:
        list1.append(0)
        list1.append(1)
        while c<x:
            list1.append(c)
            c = u+v
            u = v
            v = c
        return list1
x = 100
print(fibbnocci(x))

# 5.	Write a program find a given number is prime or not
def prime(x):
    if x<1:
        return print('invalid')
    elif x == 2:
        return print('prime')
    elif x%2 !=0 and x%3 !=0 and x%5 !=0 and x%7 !=0 and x%11 !=0 and x%13 !=0\
         and x%17 !=0 and x%19 !=0 and x%23 !=0 and x%29 !=0:
        return print('prime')
    else:
        print('not prime')
      
x = 97
prime(x)"""

# 7.	Write a program find a given number is Armstrong or not?  
"""print(153//10) #quotient
print(153/10)
print(153%10) #remainder
def armstrong(num):
    x = num
    num1 = 0
    length = len(str(num))
    list1 =[]
    for i in range(length):
        if num >0:
            quo = num//10
            rem = num%10
            list1.append(rem)
            num = quo
    list1 = list1[::-1]
    arm_num = 0
    for k in range(len(list1)):
        arm_num = list1[k]**len(list1)+arm_num
    print(arm_num)
    if arm_num == x:
        return print("given armstrong num")
    else:
        return print("not armstrong num")
        
num = 1634
armstrong(num)
        
# 6.	Write a program find given number is perfect or not
def perfect(x):
    list1 =[]
    list_sum = 0
    for i in range(1,x):
        if x%i==0:
            list1.append(i)
            list_sum = list_sum+i
    if list_sum == x:
        return print("given number is perfect")
    else:
        return print("not perfect number")
x = 24
perfect(x)

# 8.	Write a program sort the given list of integer elements
list1 = [2,4,5,1,7,10,4,9]
for i in range(1,len(list1)+1):
    for j in range(i):
        if list1[i-1]<list1[j]:
            list1[i-1],list1[j] = list1[j],list1[i-1]
print(list1)
# 9.	Write a program find a maximum number in the given input integer list.
list1 = [2,4,5,1,7,10,4,9]
for i in range(1,len(list1)):
    if list1[i-1]>list1[i]:
        list1[i],list1[i-1]= list1[i-1],list1[i]
print(list1)
print(list1[-1])"""

# 10.	Write a program print longest length string from given input list of strings.
string = ["Passion", "Yearning", "Transparency", "Humble", "open-minded", "Noble"]
str_len = []
for i in range(1,len(string)):
    # print(len(string[i]))
    if len(string[i-1])>len(string[i]):
        string[i-1], string[i] = string[i], string[i-1]
print(string[-1])
    
    








