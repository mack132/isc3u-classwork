
#determine if a letter is a vowel or consenant

#read letter from user

letter = input("Enter a letter of the alphabet")

#classify the letter and give result 
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
 print("Its a vowel.")
elif letter == "y":
  print("Sometimes its a vowel")

else:
  print("Its a consenant")

#report name of shape from number of sides

#read number of sides from user
nsides = int(input("Enter the number of sides: ")

#determine the name, leaving it empty if an unsupported number of sides was enetered
name = ""
if nsides == 3:
  name = "triangle"
elif nsides == 4:
  name = "quadrilateral"
elif nsides == 5:
  name = "pentagon"
elif nsides == 6:
  name = "hexagon"
elif nsides == 7:
  name = "septagon"
elif nsides == 8:
  name = "octagon"

#display the number of days in a month

#read input from user
month = input("Enter the name of a month: ")

#compute the number of days in a month
days = 31

if month == "april" or month == "June" or \
  month == "Spetember" or month == "November" \
days = 30

elif month == "February"
  days = "28 or 29"

#display the result
print(month, "has", days, "days in it.")


#determine the name of a triangle from the lengths of its sides

#read side lengths from user
side1 = float(input("Enter the lenght of side one: "))
side2 = float(input("Enter the lenght of side two: "))
side3 = float(input("Enter the lenght of side three"))

#determine the triangles name
if side1 == side 2 and side2 == side3:
  name = "Equilateral"
elif: side1 == side2 or side2 == side3 or side3 == side1:
  name = isocelesce 
else: 
  name = scalene

#display the triangles name
print("Thats a", name, "triangle")

# coding bat questions

print("Hello,")
print("World!")

print("Goodbye,")
print("World!")

print("(---bun---)")
print("(-burger--)")
print("(---bun---)")

print("She said hello to her friend.")
print("Her friend said", "Nice to see you!")

surface_area = 10 + 25
print(f"The surface area is {surface_area} cm^2")

print("One plus Two is:")
print(1 + 2)

print("Five minus Three is:")
print(5 - 3)

print("Six multiplied by Four is:")
print(6 * 4)

print("Twelve divided by Six is:")
print(12/6)

print("Twenty Three floor-divide by Five is:")
print(23//5)

print("Two to the power of Eight is:")
print(2 * 2 * 2 * 2 * 2 * 2 * 2 * 2)

# modulus


students = 33
number_of_groups = 5

print(33 // 5)
students_per_group = 6
print(33 % 5)
students_left_over = 3
print(f"If there are {students} students and {number_of_groups} groups.")
print(f"There will be {students_per_group} students per group")
print(f"and there will be {students_left_over} students without a group.")

change_cents = 235
quarters = 0
print(235 // 25)
quarters = 9
print(f"You will get back {quarters} quarters.")

# initialize tables here
tables = 32
# initialize chairs_per_table here
chairs_per_table = 9
# do not modify the code below this line
total_chairs = tables * chairs_per_table
print(f"There are {total_chairs} chairs.")



