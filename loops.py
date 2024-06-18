#for loop
for number in range(5):
    print("attempt",number+1,(number+1)*".")
else:
     print("end")
   

print(5*"heelo \n") # whenrver you mmultiply a number witth a string it retuen ther string with the number of time

succes=True
for number in range(3):
     print("attempt")
     if succes:
          print("susscful")
else:
          print("false")      
     
#nested loop
for i in range(3):
      for y in range(4):
            print(f"{i},{y}")

# range function is acomplex type, iteratbale , strint a;lso iteratble
count=0
for i in range(1 ,10):
    if (i%2==0):
            print(i)
            count +=1
print("total number ",count)      


while True:
    age1 = input("Enter your age: ")
    try:
        age = int(age1)
        break  # Exit the loop if conversion to int is successful
    except ValueError:
        print("Invalid input. Please enter a valid age.")

print("Your age is:", age)  

      

# Print number rom 1 to 10
for i in range(1,11):
     print(i)


# print even numbers from 1 to 20
for i in range(1,21):
     if i % 2 == 0:
          print(i)

# 
total=0
for i in range(1,100):
     total+=i
print("Sum is", total)     
  

#  code to count number of vowels in  a string
String="Me AND Yasir Khan started learning Python"  
vowels="AEIOUaeiou"
count=0
for i in String:
     if i in vowels:
          count+=1
print(f"Total Vowels Are",{count})  


# reverse a list
listt=[1,2,3,4,5,6,7,8,9,10]
reverselist=[]
for i in listt[::-1]:
     reverselist.append(i)

print(reverselist)


# print fabionocci series
num_terms = 10
fib_series = [0, 1 ]

for i in range(num_terms):
    next_term = fib_series[-1] + fib_series[-2]
    fib_series.append(next_term)

print(fib_series)


# print table
number=10
for i in range(1,11):
    print(f"{number}x{i}={number*i}")

# reverse a string
string="abcdef"
for i in string:
    print(string[::-1])

# print even number in list
l=[2,3,4,5,6,7,8]
for i in l:
    if i%2==0:
        print("number is even",{i})


# find largest number in list
number1=[1,2,3,4,44,54,23,25]
lrgestnumber=number1[0]
for i in number1:
    if i>lrgestnumber:
        lrgestnumber=i  
print({lrgestnumber})           


# fabonoci series 
n=10
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b


# check weather palidrome or not
def is_palindrome(s):
    s = s.lower()
    clean_str = ''
    for char in s:
        if char.isalnum():
            clean_str += char
    reversed_str = clean_str[::-1]
    return clean_str == reversed_str
test_strings = ["radar", "hello", "A man, a plan, a canal, Panama", "Was it a car or a cat I saw?", "No lemon, no melon"]

for string in test_strings:
    if is_palindrome(string):
        print(f'"{string}" is a palindrome.')
    else:
        print(f'"{string}" is not a palindrome.')
    