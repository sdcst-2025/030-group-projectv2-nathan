#!python3
# Volume Calculator
# Feel free to rename your variables

import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("||------------------------------------------------------------------||")
    print("||                                                                  ||")
    print("||                         WELCOME TO CALC                          ||")
    print("||            (calc is short for calculator if u didn't know)       ||")
    print("||                         by nathan wolsey                         ||")
    print("||                                                                  ||")
    print("||------------------------------------------------------------------||")
    return None

def instructions():
    print("===================================================================")
    print("                                                                   ")
    print("         you will have access to 5 different calculations!         ")
    print("                                                                   ")
    print("          - for VOLUME of a SPHERE, type: a                        ")
    print("          - for VOLUME of a CYLINDER, type: b                      ")
    print("          - for VOLUME of a CONE, type: c                          ")
    print("          - for AREA of a CIRCLE, type: d                          ")
    print("          - for SURFACE AREA of a CYLINDER, type: e                ")
    print("                                                                   ")
    print("                then enter your desired values...                  ")
    print("                  and watch the magic happen!                      ")
    print("                                                                   ")
    print("===================================================================")

    return None

def vsphere():
    r = float(input("Enter a value for the radius of a sphere: "))
    if r <= 0:
        print('radius has to be postive!!!')
        return
    v = math.pi*(4/3)*(r**3)
    vr = round(v,2)
    print(f"The volume of a sphere with a radius of {r} is {vr}!")

def vcylinder():
    r = float(input("Enter a value for the radius of the cylinder: "))
    if r <= 0:
        print('radius has to be postive!!!')
        return
    h = float(input("Enter the height of the cylinder: "))
    if h <= 0:
        print('height has to be postive!!!')
        return
    v = math.pi*(r**2)*(h)
    vr = round(v,2)
    print(f"The volume of a cylinder with height of {h} and a radius of {r} is {vr}!")

def vcone():
    r = float(input("Enter the value for the radius of a cone: "))
    if r <= 0:
        print('radius has to be postive!!!')
        return
    h = float(input("Enter the height of the cone: "))
    if h <= 0:
        print('height has to be postive!!!')
        return
    v = (math.pi/3)*(r**2)*(h)
    vr = round(v,2)
    print(f"The volume of a cone with height of {h} and radius of {r} is {vr}!")

def sacylinder():
    r = float(input("Enter the radius of the cylinder: "))
    if r <= 0:
        print('radius has to be postive!!!')
        return
    h = float(input("Enter the height of the cylinder: " ))
    if h <= 0:
        print('height has to be postive!!!')
        return
    sa = (2*math.pi*r*h) + (2*math.pi)*(r**2)
    sar = round(sa,2)
    print(f"The surface area of a cylinder with radius of {r} and height of {h} is {sar}!")

def acircle():
    r = float(input("Enter a value for the radius of a circle"))
    if r <= 0:
        print('radius has to be postive!!!')
        return
    a = (math.pi)*(r**2)
    ar = round(a,2)
    print(f"The area of a circle with a radius of {r} is {ar}")


def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    instructions()
    while True:
        x = input("What calculation would u like to run? (refer to the instructions at top): ")
        if x == 'a':
            vsphere()
        elif x == 'b':
            vcylinder()
        elif x == 'c':
            vcone()
        elif x == 'd':
            acircle()
        elif x == 'e':
           sacylinder()
        cntu = input("Would you like to do another calculation? (yes/no): ")
        if cntu == 'No' or cntu == 'no' or cntu == "NO":
            print("Thank you for using this calculator!")
            break
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()
