
a=input("Enter First name:")
b=input('Enter last name:')
c=int(input('Enter year of birth:'))
d=2026
print(20*'-')
print(f"Fullname: {a} {b}")
print(f"initials: {a[0]}.{b[0]}")
print(f"Age:{d-c}")


'''
Celsius=float(input("Enter the temperature in Celsius:"))
Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15
print(f"{Celsius}\u00b0C = {Fahrenheit} \u00b0 F")
print(f"{Celsius}\u00b0C = {Kelvin} K")

'''



'''

a=input('Enter product name: ')
b=float(input('Enter a price :'))
c=int(input('Enter a qty:'))

print(21*'=')
print()
print("      RECEIPT     ")
print()
print(21*'=')
print(f"Item: {a}")
print(f"Price:£ {b:.2f}")
print(f"Quantity: {c}")
print(21*'-')
print(f'Total:£{(b*c):.2f}')
print(21*'=')



'''





'''
a=input('Enter your name:')
b=input('Enter your age:')

print(21*'-')  
print(f'Name:{a}')
print(f'Age:{b}')
print(f"Next year:{int(b)+1}")
print(21*'-')
'''



'''
a=input('Enter first number:')
b=input('Enter Second number')
print("Sum=",float(a)+float(b))
print("Difference=",float(a)-float(b))
print("Product=",float(a)*float(b))
print(f"Quotient=,{(float(a)/float(b)):.2f}")

'''



'''
city    = "Waterford"
country = "Ireland"
pop     = 56000

print(f"City:{city}")
print(f"Country:{country}")
print(f"{city},{country}: (pop:{pop})")

print("2024-06-18")
print("Mon","Tue","Wed","Thu","Fri",sep="|")
print("Start","Middle","End",sep="...")


product = "Coffee"
price   = 3.5
qty     = 4


print(f"Item: {product}")
print(f"Price: £{price:.2f}")
print(f"Quantity:{qty}")
print(f"Total:£{price*qty}")

'''

'''
age = int(input("Enter your age: "))
print(f"In 10 years you will be {age + 10}")
'''



'''
age    = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))

print(f"Age:    {age}")
print(f"Height: {height:.2f} m")
print(type(age))
print(type(height))

'''




'''
first_name = input("First name: ")
last_name  = input("Last name:  ")

print(f"Welcome, {first_name} {last_name}!")
'''




'''
price = 9.5
pi = 3.14159
score = 0.756

print(f"Price:  £{price:.2f}")
print(f"Pi ≈ {pi:.7f}")
print(f"Score:  {score:.1000%}")




name = "Bob"
age = 25

# Using + (requires str() conversion)
print("Name: " + name + ", Age: " + str(age))

# Using an f-string (cleaner and easier to read)
print(f"Name: {name}, Age: {age:2f}")
'''
'''
xCoord=300
yCoord=300
print("xCoord + yCoord =", xCoord + yCoord)
print("xCoord - yCoord =", xCoord - yCoord)
print("xCoord * yCoord =", xCoord * yCoord)
print("xCoord / yCoord =", xCoord / yCoord)




print("xCoord + yCoord =", (xCoord-100) + (yCoord-100))
print("xCoord - yCoord =", (xCoord-100) - (yCoord-100))
print("xCoord * yCoord =", (xCoord-100) * (yCoord-100))
print("xCoord / yCoord =", (xCoord-100) / (yCoord-100))

newX = xCoord / 2
newY = yCoord / 4


print("Original xCoord:", xCoord, "  New xCoord:", newX)
print("Original yCoord:", yCoord, "  New yCoord:", newY)


'''





#num1,num2,num3=50,120,180
#print(num1,num2,num3)
#print(num1,num2/2,num3)
#print(num1,num2/3,num3)
#print(num1,num2/4,num3)





#bad = int("hello")
#num1="100"
#num2="300"
#print(int(num1)+int(num2))

#If=100
#print (If)
#print (num2)
#print (num3)
#print('num1 is :{}'.format(type(num1)))

#print('num2 is :{}'.format(type(num2)))

#print('num3 is :{}'.format(type(num3)))

#first_string="This has double quotes"
#second='this has single quotes'

#print(first_string)
#print(second)


#isopen = True
#isclosed = False

#print('value of 1 ' + str(isopen))
#print('value of 2 ' + str(isclosed))




