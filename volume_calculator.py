### volume calculator ###
import math

def cube():
    length_of_cube=float(input("Enter the length of the cube = "))
    formula1 = length_of_cube*length_of_cube*length_of_cube
    print("volume of the cube is :",formula1)
    
def cuboid():
    length_of_cuboid=float(input("Enter the length of the cuboid = "))
    height_of_cuboid=float(input("Enter the height of the cuboid = "))
    width_of_cuboid=float(input("Enter the width of the cuboid = "))
    formula2 = height_of_cuboid*width_of_cuboid*length_of_cuboid
    print("volume of cuboid is: ", formula2)

def cylinder():
    height_of_cylinder=float(input("Enter the height of the cylinder = "))
    radius_of_cylinder=float(input("Enter the radius of the cylinder = "))
    formula3 = math.pi*radius_of_cylinder**2 * height_of_cylinder
    print("volume of cylinder is: ", formula3)

def shpere(): 
    radius_of_shpere=float(input("Enter the radius of shpere = "))
    formula4 = (4/3)*math.pi*radius_of_shpere**3
    print("volume of shpere is :", formula4)
    
print('\n========= Welcome to the volume calculator =========== \n 1 = cube \n 2 = cuboid \n 3 = cylinder\n 4 = shpere \n 0 = To exit')

userinput=""
while (userinput!="0"):
    userinput = input("Enter the number = ")
    if userinput not in ( "0", "1", "2","3","4"):
        print("invalid entry")
        
    if userinput == "1":
        cube()
    elif userinput == "2":
        cuboid()
    elif userinput == "3": 
        cylinder()
    elif userinput == "4":
        shpere()
    else:
        break
            
