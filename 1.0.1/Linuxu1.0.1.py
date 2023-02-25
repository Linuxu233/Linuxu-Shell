#library
import os
import platform
import random
#string aphoto
print("\033[32m /$$      /$$           /$$                                                   /$$       /$$                                        \033[0m")
print("\033[32m| $$  /$ | $$          | $$                                                  | $$      |__/                                        \033[0m")
print("\033[33m| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$       /$$ /$$$$$$$  /$$   /$$ /$$   /$$ /$$   /$$\033[0m") 
print("\033[33m| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      | $$      | $$| $$__  $$| $$  | $$|  $$ /$$/| $$  | $$\033[0m")
print("\033[31m| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$      | $$      | $$| $$  \ $$| $$  | $$ \  $$$$/ | $$  | $$\033[0m")
print("\033[35m| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/      | $$      | $$| $$  | $$| $$  | $$  >$$  $$ | $$  | $$\033[0m")
print("\033[34m| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$      | $$$$$$$$| $$| $$  | $$|  $$$$$$/ /$$/\  $$|  $$$$$$\033[0m")
print("\033[36m|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/      |________/|__/|__/  |__/ \______/ |__/  \__/ \______/\033[0m")


#password & user name
join_key = 3
again_key = 4
name = "linusshyu"
password = "Xinxin080502"
print("--------------------------------------------------------------------------------------------------------------------------------------------")
input_name = input("Please type the user name: ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
input_password = input("Please type the password: ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
print("welcome to Linuxu system!!!")
print("                                                                                                                                            ")
while(join_key == 3):
    if input_name == "linusshyu" and input_password == "Xinxin080502":
        print("                           ")
        print("                           ")
    else:
        print("Bye,you are not user!")
        break


    #command shell
    command = input("linusshyu@computer% ")
    if(command == "linuxu -v"):
        print("linuxu version 1.0.2")                                                                                                                            
    

    #Calculator command
    if(command == "math"):
        print("Develop by Linus Shyu")
        counts = 3
        while counts > 0:
            str1 = input("First number: ")
            str2 = input("Second number:")
            X = int(str1)
            Y = int(str2)
            print("Add:",X + Y)
            print("Subtraction:",X - Y)
            print("multiply:",X * Y)
            print("Divide:",X / Y)
            break
    if(command == "math -v"):
        print("The math version is 0.1.0")


    #game command
    if(command == "game"):
        print("                                              ")
        print("Welcome to Linus Shyu's guess number game!")
        print("                                              ")
        print("You have six chances")
        print("                                              ")
        print("Guess an integer between 1 and 10")
        print("                                              ")
        print("develop by Linus Shyu")
        print("                                              ")
        print("                                              ")
        counts = 6
        answer =random.randint(1,10)

        while counts > 0:
            temp = input("Guess which number the computer is thinking:")
            guess = int(temp)

            if guess == answer:
                print("Guessed right")
                break
            else:
                if guess < answer:
                    print("small")
                else:
                    print("big")
            counts = counts - 1
        print("game over")


    if(command == "game -v"):
        print("The game version is 0.1.0")


    #clear command
    if(command == "clear"):
        os.system( 'cls' )
        os.system("clear")
        
        
    #list command
    if(command == "ls"):
            print("-------------------------------------------------------------------------------------------------------------------------------")
            print(" |game| |math| |starfetch|  ")
            print("-------------------------------------------------------------------------------------------------------------------------------")

            
    #exit command
    if(command == "exit"):
        print("                                                                                                                    ")
        print("See you again!")
        break


    #starfetch 
    if(command=="starfetch"):
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")
    if(command == "starfetch -v"):
        print("The starfetch version is 0.1.0") 


    #not command help
    if(command != "linuxu -v" and command != "math" and command != "math -v" and command != "game" and command != "game -v" and command != "clear" and command != "ls" and command != "exit" and command != "starfetch" and command != "starfetch -v" and command != ""):
        print("linuxu can't find this command")
        print("you can try this command: linuxu -h")


    if(command == "linuxu -h"):
        print("="*40, "linuxu command help", "="*40)
        print("1.game:")
        print("This is a number guessing game, you need to enter an integer between 1, 10, you have six chances to guess the number, ")
        print("if you guess the number is smaller than the actual answer, then it will remind you that it is small, conversely, if it is bigger, ")
        print("it will also be reminded, if you do not guess correctly three times, then the game is over.This is a number guessing game, you need to enter an integer between 1, 10,")
        print("you have three chances to guess the number, if you guess the number is smaller than the actual answer, then it will remind you that it is small, conversely, if it is bigger, ")
        print("it will also be reminded, if you do not guess correctly three times, then the game is over.")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("2.math:")
        print("This is a calculator where you can enter two integers to calculate the sum, difference, product, and quotient of these two numbers")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("3.ls")
        print("You can see what applications are available in Linuxu")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("4.clear")
        print("You can clear what you entered and what was returned")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("5.exit")
        print("You can exit the linuxu")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("6.starfetch")
        print("You can use it to view information about your computer")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("7.starfetch -v")
        print("Check out Starfetch's version")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("8.game -v")
        print("Check out game version")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("9.math -v")
        print("Check out math version")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("linuxu -v")
        print("Check out linuxu version")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("10.linuxu -h")
        print("Cheek the linuxu command help information")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
