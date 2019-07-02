def pythagorean(a,b,c):
    """formula for pythoagorean triangles."""
    result =((pow(a,2) + pow(b,2)) == pow(c,2))

    if result == True:
        return("This is a pyhthagorean triple")
    else:
        return("This is not a pythagorean triple, please try again")
        
    

def main():
    while True:
        try:
            side1 = int(input("Enter first side: "))
            side2 = int(input("Enter second side: "))
            side3 = int(input("Enter third side: "))
            if side1 > side2 and side1 > side3:
                c = side1
                a = side2
                b = side3
                print (pythagorean(a,b,c))
                print('___________________________________________')
            elif side2 > side1 and side2 > side3:
                c = side2
                a = side1
                b = side3
                print (pythagorean(a,b,c))
                print('___________________________________________')
            else:
                c = side3
                a = side2
                b = side1
                print (pythagorean(a,b,c))
                print('___________________________________________')
        except ValueError:
            print('Please input a valid integer. Starting Over')
            print('___________________________________________')
        

main()
