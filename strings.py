#input() always reads as a string
name=input("Enter name:")
print("Hello "+name)
x=input("Enter num:")
#n=x+1 ##Give Traceback error -> typecast to int before adding
n=int(x)+1
print("Num="+n)
#or to print as string
print("String Num="+x+'1')

#Concat
str1="Avengers "
str2='Assemble'
str3=str1+str2
print(str3)

#Strings as arrays of chars
avenger="Black widow"
for i in avenger:
    print(i)

#Slicing Strings
print(avenger[0:5])#from a to b-1 #upto b but not including

#Using "in" as a logical operator
fruit='banana'
if ('n' in fruit): #is evaluated as a logical expression to give T or F
    print("T")

#switch between Upper & lower case
#ASCII of uppercase < lowercase
word='and'
if ('And'<word):
    print("T")
else:
    print("F")
print(word.upper())

#Class Strings
str="Hello"
print(type(str))#prints class name
print(dir(str))#prints methods present in the class

#Searching a String
str="Mississippi"
pos=str.find('pp')#prints first occurence of the given String
print(pos)#if not present prints -1

#Search and Replace
str="Mississippi"
pos=str.replace('pp','PP')#prints first occurence of the given String
print(pos)#if not present prints -1
