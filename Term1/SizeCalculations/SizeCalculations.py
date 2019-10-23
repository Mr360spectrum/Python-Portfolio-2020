# Karter Ence, Jamerson McGuire, Xander Szykowny, Michael Calhoun
# Shape Size Calculator
# 9/11/2019

# Checked by jacob, Noah, austin, seth
# Run Time Error When we put a letter in the code it breaks the code.
# Logical Error When you put a huge number it broke the picture.
# Logical Error We can use negative numbers which should not be possible. there can't be negative Perimeter's or Area.
# Runtime Error We cannot input mathematical operations as values.
# Declare the menu

#Declare the function for the area of square/rectangle
def square():       
      # Get side lengths for square/rectangle
      print("What is the length of the square?")
      sqrLength = float(input(": "))
      print("What is the width of the square?")
      sqrWidth = float(input(": "))
      # Calculate perimeter and area
      sqrPer = (sqrLength + sqrWidth) * 2
      sqrArea = sqrLength * sqrWidth
      # Print the calculations
      print(str.format("The perimeter of the square is {0:.2f}", sqrPer))
      print(str.format("The area of the square is {0:.2f}", sqrArea))
      # ASCII with side lengths
      print(str.format("""

Perimeter = {0:.2f}
Area = {1:.2f}

      {2:^10.2f}
 ________________________
|                        |
|                        |
|                        |
|                        |
|                        | {3:^10.2f}
|                        |
|                        |
|                        |
|                        |
|                        |
|________________________|
      """, sqrPer, sqrArea, sqrLength, sqrWidth))

# Declare the function for the circumference of circle
def circle():
      # Get the radius of the circle
      print("What is the radius of the circle?")
      radius = float(input(": "))
      # Calculate the circumference
      circumference = 2 * 3.14 * radius
      print(str.format("The circumference of the circle is {0:.2f}", circumference))
      # ASCII art with radius
      print(str.format("""

Cricumference = {0:.2f}

      %%%    %%%
      %%%              %%%

%%%                      %%%
      {1:^12.2f}     
%%% __________0             %%%

%%%                         %%%

%%%                        %%%

%%%                  %%%

      %%%     %%%
      """, circumference, radius))

# Declare the function for the area of triangle
def triangle():
      # Get the base and height of the triangle
      print("What is the base length of the triangle?")
      triBase = float(input(": "))
      print("What is the height of the triangle?")
      triHeight = float(input(": "))
      # Calculate the area of the triangle
      triArea = (triBase * triHeight) / 2
      print(str.format("The area of the triangle is {0:.2f}",triArea))
      # ASCII are with base and height
      print(str.format("""

Area = {0:.2f}

       /|
      / |
     /  |
    /   |
   /    | {1:<12.2f}
  /     |
 /      |
/_______|
{2:^12.2f}  
      """, triArea, triHeight, triBase))

# Declare the function for the volume of cube/rectangular prism
def cube():
      # Get the measurements of the cube/rectangular prism
      print("What is the height of the cube?")
      cubeHeight = float(input(": "))
      print("What is the length of the cube?")
      cubeLength = float(input(": "))
      print("What is the width of the cube?")
      cubeWidth = float(input(": "))
      # Calculate and print the volume
      cubeVol = cubeHeight * cubeLength * cubeWidth
      print(str.format("The volume of the cube is {0:.2f}", cubeVol))
      # ASCII art with measurements
      print(str.format("""

Volume = {0:.2f}

{1:^15.2f}
   +--------+
  /        /|
 /        / | {2:<15.2f}
+--------+  |
|        |  |
|        |  +
|        | /
|        |/{3:<14.2f}
+--------+
      """, cubeVol, cubeLength, cubeHeight, cubeWidth))

def menu():
      while True:
            print("""
            
            1. Area of square/rectangle
            2. Circumference of a circle
            3. Area of a triangle
            4. Volume of cube/rectangular prism
            5. Quit

            """)
            print("Please enter the desired option: ")
            menuOption = input(": ")
            if menuOption.isdigit():
                  menuOption = int(menuOption)
                  if menuOption == 1:
                        square()
                  elif menuOption == 2:
                        circle()
                  elif menuOption == 3:
                        triangle()
                  elif menuOption == 4:
                        cube()
                  elif menuOption == 5:
                        quit()
                  else:
                        print("That is not a valid option.")
            else:
                  print("That is not a valid option.")

menu()