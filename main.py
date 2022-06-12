import ipaddress
from time import sleep
import sys
import manager
import socket   

print("""

 ________  ________  ___      ___ ________  ________   ________  _______   ________         
|\   __  \|\   ___ \|\  \    /  /|\   __  \|\   ___  \|\   ____\|\  ___ \ |\   ___ \        
\ \  \|\  \ \  \_|\ \ \  \  /  / | \  \|\  \ \  \\ \  \ \  \___|\ \   __/|\ \  \_|\ \       
 \ \   __  \ \  \ \\ \ \  \/  / / \ \   __  \ \  \\ \  \ \  \    \ \  \_|/_\ \  \ \\ \      
  \ \  \ \  \ \  \_\\ \ \    / /   \ \  \ \  \ \  \\ \  \ \  \____\ \  \_|\ \ \  \_\\ \     
   \ \__\ \__\ \_______\ \__/ /     \ \__\ \__\ \__\\ \__\ \_______\ \_______\ \_______\    
    \|__|\|__|\|_______|\|__|/       \|__|\|__|\|__| \|__|\|_______|\|_______|\|_______|    
                                                                                            
                                                                                            
                                                                                            
 ________  ________  ________  ________  ___       _______                                  
|\   ____\|\   __  \|\   __  \|\   ____\|\  \     |\  ___ \                                 
\ \  \___|\ \  \|\  \ \  \|\  \ \  \___|\ \  \    \ \   __/|                                
 \ \  \  __\ \  \\\  \ \  \\\  \ \  \  __\ \  \    \ \  \_|/__                              
  \ \  \|\  \ \  \\\  \ \  \\\  \ \  \|\  \ \  \____\ \  \_|\ \                             
   \ \_______\ \_______\ \_______\ \_______\ \_______\ \_______\                            
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|                            
                                                                                            
                                                                                            
                                                                                            
 ________  _______   ________  ________  ________  ___  ___                                 
|\   ____\|\  ___ \ |\   __  \|\   __  \|\   ____\|\  \|\  \                                
\ \  \___|\ \   __/|\ \  \|\  \ \  \|\  \ \  \___|\ \  \\\  \                               
 \ \_____  \ \  \_|/_\ \   __  \ \   _  _\ \  \    \ \   __  \                              
  \|____|\  \ \  \_|\ \ \  \ \  \ \  \\  \\ \  \____\ \  \ \  \                             
    ____\_\  \ \_______\ \__\ \__\ \__\\ _\\ \_______\ \__\ \__\                            
   |\_________\|_______|\|__|\|__|\|__|\|__|\|_______|\|__|\|__|                            
   \|_________|                                                                             
                                                                                                                                 
""")
sleep(2)
get_data = True
ext = False
while get_data:
    print(
        """                                                                                                
Welcome to Advanced Google Search!

Select your Search category:
[1] Calculations
[2] Quick Data Conversion
[3] Currency Conversion
[4] Distance from one area to another
[5] Hotels
[6] Events
[7] Time in another area
[8] Customer support information
[9] Translate
[10] Stocks
[11] Sunrise in local time
[12] Your IP Address and Computer Name
[13] Holiday Dates
[14] Coding Docs      
[15] Exit Advanced Google Search
""")

    try:
        opt = int(input("Enter your search type: "))
        if opt > 15 or opt < 0:
            print("Invalid number. Please try again")
            sleep(3)
        elif opt == 15:
            print("Exiting Advanced Google Search......")
            sleep(3)
            get_data = False
            # exit()
        else:
            print("Option captured!")
            get_data = False
    except:
        if get_data == True:
            print("Your input is not a number. Please try again.")
            sleep(3)

if opt == 1:
    print("""
 ________  ________  ___       ________  ___  ___  ___       ________  _________  ___  ________  ________   ________      
|\   ____\|\   __  \|\  \     |\   ____\|\  \|\  \|\  \     |\   __  \|\___   ___\\  \|\   __  \|\   ___  \|\   ____\     
\ \  \___|\ \  \|\  \ \  \    \ \  \___|\ \  \\\  \ \  \    \ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \ \  \___|_    
 \ \  \    \ \   __  \ \  \    \ \  \    \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \ \_____  \   
  \ \  \____\ \  \ \  \ \  \____\ \  \____\ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \|____|\  \  
   \ \_______\ \__\ \__\ \_______\ \_______\ \_______\ \_______\ \__\ \__\   \ \__\ \ \__\ \_______\ \__\\ \__\____\_\  \ 
    \|_______|\|__|\|__|\|_______|\|_______|\|_______|\|_______|\|__|\|__|    \|__|  \|__|\|_______|\|__| \|__|\_________\
                                                                                                              \|_________|
                                                                                                
        """)
    try:
        x = int(input("Enter value of x: "))
        operator = int(
            input("""
Operator Directory:
[1] Addition
[2] Division
[3] Multiplication
[4] Subtraction
[5] Power
[6] Modulus
Enter operator number: """))

        y = int(input("Enter value of y: "))
    except:
        sys.exit(
            "ValueError: Non-Integer type input. Please relaunch Advanced Google Search"
        )

    if operator == 1:
        print(f"{str(x)} + {str(y)} = {str(x + y)}")
    elif operator == 2:
        print(f"{str(x)} ÷ {str(y)} = {str(x / y)}")
    elif operator == 3:
        print(f"{str(x)} × {str(y)} = {str(x * y)}")
    elif operator == 4:
        print(f"{str(x)} - {str(y)} = {str(x - y)}")
    elif operator == 5:
        print(f"{str(x)} ** {str(y)} = {str(x ** y)}")
    elif operator == 6:
        print(f"{str(x)} % {str(y)} = {str(x % y)}")
    else:
        sys.exit(
            "Internal Error: Operator index out of range. Please relaunch Advanced Google Search"
        )

elif opt == 2:
    print("""

 ________  ________  _________  ________                                     
|\   ___ \|\   __  \|\___   ___\\   __  \                                    
\ \  \_|\ \ \  \|\  \|___ \  \_\ \  \|\  \                                   
 \ \  \ \\ \ \   __  \   \ \  \ \ \   __  \                                  
  \ \  \_\\ \ \  \ \  \   \ \  \ \ \  \ \  \                                 
   \ \_______\ \__\ \__\   \ \__\ \ \__\ \__\                                
    \|_______|\|__|\|__|    \|__|  \|__|\|__|                                
                                                                             
                                                                             
                                                                             
 ________  ________  ________   ___      ___ _______   ________  _________   
|\   ____\|\   __  \|\   ___  \|\  \    /  /|\  ___ \ |\   __  \|\___   ___\ 
\ \  \___|\ \  \|\  \ \  \\ \  \ \  \  /  / | \   __/|\ \  \|\  \|___ \  \_| 
 \ \  \    \ \  \\\  \ \  \\ \  \ \  \/  / / \ \  \_|/_\ \   _  _\   \ \  \  
  \ \  \____\ \  \\\  \ \  \\ \  \ \    / /   \ \  \_|\ \ \  \\  \|   \ \  \ 
   \ \_______\ \_______\ \__\\ \__\ \__/ /     \ \_______\ \__\\ _\    \ \__\
    \|_______|\|_______|\|__| \|__|\|__|/       \|_______|\|__|\|__|    \|__|
                                                                             
    """)

    try:
        conversion = int(input("""Enter your type of measure:
[1] Temperature
[2] Weight
[3] Length    
        """))
    except:
        sys.exit("ValueError: Non-integer type input. Please try again by relaunching Advanced Google Search.")
    
    if conversion == 1:
        input_unit = int(input("""Enter your base input unit:
[1] Celsius
[2] Farenheit
[3] Kelvin
        """))
        output_unit = int(input("""Enter your base output unit:
[1] Celsius
[2] Farenheit
[3] Kelvin
        """))
        if input_unit == 1 and output_unit == 2:
            x = int(input("""Enter value in base input: 
            """))
            print(f"{str(x)}°C = {str((x * 9 / 5) + 32)}°F")

        elif input_unit == 1 and output_unit == 3:
            x = int(input("""Enter value in base input: 
            """))
            print(f"{str(x)}°C = {str(x + 273.15)}K")
        
        elif input_unit == 2 and output_unit == 1:
            x = int(input("""Enter value in base input: 
            """))
            print(f"{str(x)}°C = {str((x - 32) * 5 / 9)}°F")
        
        elif input_unit == 2 and output_unit == 3:
            x = int(input("""Enter value in base input: 
            """))
            print(f"{str(x)}°C = {str((x - 32) * 5 / 9 + 273.15)}K")
        
        elif input_unit == 3 and output_unit == 1:
            x = int(input("""Enter value in base input: 
            """))
            print(f"{str(x)}K = {str(x - 273.15)}°C")
        
        elif input_unit == 3 and output_unit == 2:
            x = int(input("""Enter value in base input: 
            """))
            print(f"{str(x)}K = {str((x - 273.15) * 9 / 5 + 32)}°F")
        
    elif conversion == 2 or conversion == 3:
        print("Sorry, these items are still in progress. Please try again in v1.")
    else:
        sys.exit(
            "Internal Error: Operator index out of range. Please relaunch Advanced Google Search"
        )
#         input_unit = int(input("""Enter your base input unit:
# [1] Gram
# [2] Kilograms
# [3] Pounds
#         """))
#         output_unit = int(input("""Enter your base output unit:
# [1] Gram
# [2] Kilograms
# [3] Pounds
#         """))

# Still in progress 

elif opt == 12:
    hostname = socket.gethostname()   
    ipadd = socket.gethostbyname(hostname)
    print(f"""Computer Name: {hostname}
IP Address: {ipadd}""")


# manager.Manager()
# Manager file is incomplete, fixed once everything is done.