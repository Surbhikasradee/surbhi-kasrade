#program 1
NAME=str(input("enter your name: "))
print("Good Afternoon",NAME)

#program 2
letter = ''' Dear <|Name|>
You are selected
<|Date|>''' 


Name = (input("enter your name: " ))
Date = (input("enter date: "))
letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)
print(letter)

#program 3
string = '''Hello my name  is Surbhi kasrade'''

doubleSpace = string.find("  ")

print(doubleSpace)


#program 4
string = '''Hello my name  is Surbhi kasrade'''

doubleSpace = string.replace("  ", " ")

print(doubleSpace)

#program 5
fruit1 = input("Enter 1st fruit name : ")
fruit2 = input("Enter 2nd fruit name : ")
fruit3 = input("Enter 3rd fruit name : ")
fruit4 = input("Enter 4th fruit name : ")
fruit5 = input("Enter 5th fruit name : ")

fruitList = [fruit1, fruit2, fruit3, fruit4, fruit5]

print(fruitList)

#program 6
st1 = int(input("enter 1st student's marks : "))
st2 = int(input("enter 2nd student's marks : "))
st3 = int(input("enter 3rd student's marks : "))
st4 = int(input("enter 4th student's marks : "))
st5 = int(input("enter 5th student's marks : "))
st6 = int(input("enter 6th student's marks : "))

studentMarksList = [st1, st2, st3, st4, st5, st6]

studentMarksList.sort()

print(studentMarksList)

#program 7
t = (5, 10, 15)

t[0] = 10       #it is not allowed hence cannot change in tupple

print(t)

#program 8
first = int(input("enter first number : "))
second = int(input("enter first number : "))
third = int(input("enter first number : "))
fourth = int(input("enter first number : "))

numberList = [first, second, third, fourth]

sum = numberList[0] + numberList[1] + numberList[2] + numberList[3]

print(sum)


#program 10
myDict = {

    "Kitab" : "Book", 
    "Dimag" : "Brain",
    "Aacha" : "Good",
    "Dil" : "Heart",
    "Galti" : "Mistake",
}

print("Options are : ", myDict.keys())

a = input("Enter Your Word : ")

print("The meaning of your word is : ", myDict[a])


#program 11
my_list = [10, 20, 30, 40, 20, 50, 60, 40]

print("Original List : ",my_list)

my_set = set(my_list)

my_new_list = list(my_set)

print("List of unique numbers : ",my_new_list)


#program 15
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
num4 = int(input("Enter 4th number : "))

if num1 > num4 :
    f1 = num1
else :
    f1 = num4

if num2 > num3 :
    f2 = num2
else : 
    f2 = num3

if f1 > f2 :
    print(f1, "is greatest")

else :
    print(f2, "is gratest")


#program 16
marks1 = int(input("Marks of student in subject 1: "))

marks2 = int(input("Marks of student in subject 2: "))

marks3 = int(input("Marks of student in subject 3: "))
#total assuming out of 50

if((marks1 / 50) * 100 < 33):
    print("fail")

elif((marks2 / 50) * 100 < 33):

    print("fail")

elif((marks3 / 50) * 100 < 33):

    print("fail")

elif((marks1 + marks2 + marks3) / 150 * 100 < 40):

    print("fail")

else:

   print("pass")



#program 17
marks1 = int(input("Marks of student in subject 1: "))

marks2 = int(input("Marks of student in subject 2: "))

marks3 = int(input("Marks of student in subject 3: "))
#total assuming out of 50

if((marks1 / 50) * 100 < 33):
    print("fail")

elif((marks2 / 50) * 100 < 33):

    print("fail")

elif((marks3 / 50) * 100 < 33):

    print("fail")

elif((marks1 + marks2 + marks3) / 150 * 100 < 40):

    print("fail")

else:

   print("pass")   
   


#program 18
username = input("Enter your name ")

if len(username) < 10:
    print("less than 10 characters" )
else:
    print("not less than 10 characters ")


#program 19
MyList = ['ram','shyam','rahul','arjun','joy']

if 'shyam' in MyList:
 print("Yes it is present in the list")
else:
 print("It is not present in the list")


#program 20
marks1 = int(input("Marks of student : "))
if(marks1 > 90 and marks1 <= 100):
    print("Excellent")
elif(marks1 > 80 and marks1 <=90):
    print("A")
elif(marks1 > 70 and marks1 <= 80):
    print("B")
elif(marks1 > 60 and marks1 <= 50):
    print("C")
elif(marks1 > 50 and marks1 <= 60):
    print("D")
else:
    print("fail")





#program 22
num = int(input("Enter the number for multiplication table : "))

#using for loop

print("Using for loop")

for i in range(1,11):
    print(num,'x ',i,' = ',num * i) 

i = 1

#using while loop

print("Using while loop")

while( i <= 10):
    print(num,'x ',i,' = ',num*i)
    i+=1
    
 
#program 23
myList = ["Simarjeet", "Sohan", "Sachin", "Rahul"]

for x in myList:
    if(x.startswith("S")):
        print("Good morning, " + x )    

        
#program 24
num = int(input("Enter a number: "))

flag = False

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if (flag):
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")




#program 25
um = int(input("Enter a number: ")) 

sum = 0
number  = num
while(num > 0):
    sum += num
    num -= 1

print("The sum of",number , "natural numbers is: ", sum)    
        








