#x = int(input("Enter the first value:"))
#y = int(input("Enter the second value:"))
#z =(x**2 +y**2)**0.5
#print(z)

# print("+"+"-"*10+"+")
# print(("|"+" "*10+"|\n")*5, end="")
# print("+"+"-"*10+"+")


# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# num3 = int(input("Enter the third number:"))
# larger_number = num1
# if num2 > larger_number:
#     larger_number = num2

# if num3 > larger_number:
#     larger_number = num3

# print("The larger number is:", larger_number)


# x = int(input("Enter the first number:"))
# y = int(input("Enter the second number:"))
# z = int(input("Enter the third number:"))
# larger_number = max(x,y,z)
# lowest_number = min(x,y,z)
# print("The largest number is:", larger_number)
# print("The lowest number is:", lowest_number)

# x = input("Enter your word")
# if x == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif x == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not!", x + "!")
# while True:
#     print ("I'm not able to end this.")
# largest_number = -99999
# number = int(input("Enter a number or type -1 to stop:"))
# while number != -1:
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to stop:"))

# print("The largest number is:", largest_number)

# x = int(input("Enter the numbers:"))
# count = 1 
# while count <= x:
#     print(count," ",end="",)
#     count+=1

# x = int(input("Enter the numbers:"))
# count =1
# even = 0
# odd = 0
# while count <= x:
#     if count % 2 == 0 :
#         even += 1
#     else:
#         odd += 1

#     count += 1
# print("Even : ",even)
# print("Odd :",odd)                                                                              

# for counter in range(101):
#     print("counter:", counter)
#     pass
# for counter in range(21, 42):
#     print ("Counter:",counter)
#     pass
# for counter in range(2,10,2):
#     print ("Counter:",counter)
#     pass
# power=1
# for expo in range(16):
#     print("2 to the power of",expo,"is",power)
#     power *=2
# for expo in range (5):
#     count=1
#     print("count",count,"Missisippi")
#     count+=1

# print("The break instruction:")
# for counter in range (1,6):
#     if counter == 3:
#         break
#     print("Inside the loop.",counter)
#     print("Outside the loop.")
# print("The continue instruction:")
# for counter in range (1,6):
#     if counter == 3:
#         continue
#     print("Inside the loop.",counter)
#     print("Outside the loop.")
# counter = 1
# while counter< 5:
#     print(counter)
#     counter+=1
# else:
#     print("else:",counter)

# counter = 5
# while counter< 5:
#     print(counter)
#     counter+=1
# else:
#     print("else:",counter)
# var = 10
# print(var > 0)
# print(not(var <= 0))
# var = 10 
# print(var!= 0)
# print(not(var==0))
# numbers=[10,5,7,2,1]
# print(numbers)
# print(type(numbers)) 
# number = []
# numbers=[10,5,7,2,1]
# print(numbers)
# print(type(numbers))
# print("First element content:", numbers[0])
# print("Second element content:", numbers[1])
# print("Third element content:", numbers[2])
# print("Fourth element content:", numbers[3])
# print("Fifth element content:", numbers[4])

# numbers[0] = 111
# print("numbers[0]:",numbers[0])
# print (numbers)

# numbers[1]= numbers[4]
# print(numbers)
# print(len(numbers))
# del numbers[2]
# print(numbers)
# print(len(numbers))
# print(numbers[-1])
# print (numbers[-2])
# print (numbers[-3])
# print (numbers[-4])
# print (numbers[-5])
# print(numbers[4])
# list = [1,2,3,4,5]
# print(len(list))
# del list[-1]
# print(len(list))
# i = int(input("Enter the number:"))
# list[int(len(list)//2)] = i
# print(list)
# list = [5,4,3,2,1]
# print(list)
# list.append(6)
# print(list)
# list.insert(1,10)
# print(list)
# x = [1,2,3,4,5,6,7,8]
# for count in range(len(x)):
# print(x[count])
#x = int(input("Enter the numbers:"))
# count = 1 
# while count <= x:
#     print(count," ",end="",)
#     count+=1

# for i in range(1,51):
#     if i % 2 != 0:
#         print(i, end = ", ")
#     else:
#         print("t", end= ", ")

# for i in range (1, 51):
#     if i % 3 == 0:
#         print("t", end = ", ")
#     else:
#         print(i, end=", ")

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizbuz", end=", ")
#     elif i % 3 == 0:
#         print("fiz", end=", ")
#     elif i % 5 == 0:
#         print("buz", end=", ")
#     else:
#         print(i, end=", ")
                                                                             
# income = float(input("Enter the income:"))
# if income <= 85528:
#     tax = income * 0.18 - 556.02
#     if tax < 0:
#          tax = 0
# else:
#     tax = 14839.02 + (income - 85528)* 0.32
# print("The tax is:", round(tax),"thalers.")

# year = int(input("Enter the year:"))
# if year >= 1582 and year % 4 == 0:
#     print("This is leap year and in Gregorian calendar period",year)    
# elif year < 1582:
#         print("Not within the Gregorian calendar period.", year)
# else: 
#     print("This is a Common year.", year)

# year = int(input("Enter the year:"))
# if year < 1528:
#     print("Not within the Gregorian calendar period.", year)
# else:
    # if year % 4 != 0:
    #     print("Common year")
    # elif year %100 != 0:
    #     print("Leap year")
    # elif year %400 != 0:
    #     print("Common year")
    # else:
    #     print("Leap year")
# import time
# for counter in range(5):
#     print(counter, "Mississippi")
#     time.sleep(1)
# print("Ready or not, here I come!")

# user_word = input("Enter a word:")
# user_word = user_word.upper()
# word_without_vowels = ""

# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue

#     word_without_vowels += letter
# print("word_without_vowels", word_without_vowels)

# cO = int(input("Enter a natural number:"))
# count = 0
# while cO != 1:
     
#     if cO % 2 == 0:
#         cO = cO //2
#     else :
#         cO = 3*cO + 1
#     count += 1
# print(count)

# x = int(input("Enter the number of blocks:"))
# height = -1
# count = 1
# while x >= 0:
#     x = x-count
#     height += 1
#     count += 1
# print ("Height of the pyramid:", height)

# def indexSum(x):
#     total_sum = sum(x)
#     left_sum = 0
#     right_sum = 0
#     count = 0
#     for i in x:
#         right_sum = total_sum - left_sum -  i
#         if left_sum == right_sum:
#             return count
#         count += 1
#         left_sum += i
#     return -1


# x = list(map(int,input("Enter the array elements:").split()))
# my_list = list(x)
# print(x)
# result = indexSum(x)
# print(result)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# for count in range (len(my_list)):
#     print(my_list[count])

# '''
# iterator  0 1 2 3 4 5
# output    1 2 3 4 5 6
# '''
# list = []
# for iterator in range (1 ,11):
#     list. append(iterator)
# print(list)

# list = []
# for iterator in range (1 ,11):
#     list. append(iterator)
#     print(list)

# list = []
# for iterator in range (10):
#     list. append(iterator+1)
# print(list)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for count in range (10):
#     list[count] += 1
# print (list)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# total = 0
# for sum in list:
#     total += sum  
# print(list) 
# print(total)

# var = 5
# var1 = 10
# print ("var:",var)
# print ("var1:",var1)

# var , var1 = var1 , var
# print ("var:",var)
# print ("var1:",var1)

# list = [1,2,3,4]
# print(list)
# list[1],list[3]= list[3],list[1]
# print(list)

#new start
# import csv
# records =[
#     ['Name','Marks','City','Grade'],
#     ['HR','99','Indore','A'],
#     ['Isha','99','Indore','A'],
#     ['Harshi','98','CWA','A'],
# ]
# search_name = input ("Enter the name:")
# found = False
# # with open('students.csv','w',newline='') as f:
# #     csv.writer(f).writerows(records)
# with open('students.csv', 'r') as f:
#     # for row in csv.DictReader(f):
#     #     print(f'{row["Name"]}:{row["Marks"]}marks ({row["City"]})')
#     for row in csv.DictReader(f):
#         if row["Name"] == search_name:
#             print("Record found")
#             print(row)
#             found = True
#             break
# if not found:
#     print("Student Not found!!")

'''Numpy & Pandas'''

import numpy as np

# arr1d = np.array([1,2,3,4,5])
# arr2d = np.array([[11,22,33],[44,55,66],[77,88,99]])

# print(arr2d.shape)
# print(arr2d.dtype)
# print(arr2d.ndim)

# zeros = np.zeros((3,4))
# print(zeros)
# ones = np.ones((2,5))
# print(ones)
# rng = np.arange(0,50,5)
# print(rng)
# lin = np.linspace(0,1,11)
# print(lin)
# random = np.random.randint(40,100,(5,3))
# print(random)

'''Vactorized method - no loop needed'''
# arr = np.array([10,20,30,40,50])
# print(arr*2)
# print(arr+5)
# print(arr**2)
# print(arr)

# marks_2d = np.array([[85,90,78],[72,88,95],[91,76,83]])
# print(np.mean(marks_2d))
# print(np.mean(marks_2d,axis = 1))   # mean per student
# print(np.mean(marks_2d,axis = 0))   # mean per subject(column)
# print(np.max(marks_2d))
# print(np.std(marks_2d))

# arr = np.array([55,66,77,88,99,98,87,78])
# print(arr[arr> 70])    

'''Pandas'''
import pandas as pd
data = {
    'Name' : ['HR','Harshi','Isha','Khushi','Harsh'],
    'Age'  : [21,21,22,22,27],
    'Marks': [88,98,87,86,85],
    'City' : ['Indore','Cwa','Indore','Jbl','Hyd'],
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.head(3))
print(df.dtypes)
print(df.describe())


print("df['Name'] : \n" ,df['Name'])
print(df[['Name','Marks']])

print(df[df['Marks'] >=80 ])
print(df[df['City'] == 'Indore'])
print (df[(df['Marks'] >= 80)&(df['City'] == 'Indore')])

def get_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    else:
        return 'C'
df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])\
print('------------')
print(df)