#Let's code a statement that will ask a user for an input of expression.
expression = input("Enter an Expression: ")
#Converting x,y and z into variable
x, y, z= expression.split(" ")

#Convering x and z into float
new_x = float(x)
new_z = float(z)
    
#let's calbulate using if statement
if y == "+":
  result = new_x + new_z

elif y == "-":
  result = round(new_x - new_z,1)

elif y == "*":
  result = round(new_x * new_z,1)

elif y == "/":
  result = round(new_x / new_z,1)

print(result)
    
       