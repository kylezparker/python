# imports



# global variables






# function definitions
def print_menu():
    print("------------")
    print("PyCal 3000")
    print("------------")
    print("------------")

    print("[1] sum")
    print("[2] sub")
    print("[3] mult")
    print("[4] div")
    print("[x] exit")





# plain instructions
option=""

while option != "x":
    print_menu()
    option = input("please select an option: ")
    if option == "x":
        break #break ends loop

    num1=float(input("enter 1st number: "))
    num2=float(input("enter 2nd number: "))


    if option =="1":
        result= num1+num2
    elif option =="2":
        result= num1-num2
    elif option =="3":
        result= num1*num2
    elif option =="4" and num2==0:
        result=0
    elif option=="4" and num2!=0:
        result=num1/num2
    # elif option =="4":
    #     if num2==0:
    #     result="bad input"
    #     else:
    #         result=num1/num2


    print("the result: " + str(result))
    # print_menu()
    input("press enter to continue")
    print("")
    print("")
    print("")
    print("")

print("thanks, goodbye")

