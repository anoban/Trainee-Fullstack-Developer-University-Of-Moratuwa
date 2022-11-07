# a dictionary with expected user input chars as keys and designated numerals as values
inputs = {"+":1, "-":2, "*":3, "/":4, "^":5, "%":6, "#":7, "$":8, "?":9}

def select_op(char):
    ioperator = char.strip()
    if len(ioperator) == 1:
        try:
            return inputs[ioperator]
        except:
            return "Unrecognized operation"
    else:
        return "Unrecognized operation"
        
history = list()

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")
    choice = str(input("Enter choice(+,-,*,/,^,%,#,$,?): ")).strip()
    print(choice)

    usr_selection = select_op(choice)
    if(usr_selection == 7):
        print("Done. Terminating")
        exit()
    elif(usr_selection == 8):
        continue
    elif(usr_selection == 9):
        if len(history) == 0:
            print("No past calculations to show")
        else:
            for i in history:
                print(i)
    else:
        num1 = input("Enter first number: ").strip()
        print(num1)
        if "$" in num1:
            continue
        elif "#" in num1:
            print("Done. Terminating")
            exit()
        num2 = input("Enter second number: ").strip()
        print(num2)
        if "$" in num2:
            continue
        elif "#" in num2:
            print("Done. Terminating")
            exit()
        else:
            try:
                num_1 = float(num1)
                num_2  = float(num2)
                if(usr_selection == 6):
                    try:
                        print("{} % {} = {}".format(num_1, num_2, num_1 % num_2))
                        history.append("{} % {} = {}".format(num_1, num_2, num_1 % num_2))
                    except:
                        print("Something Went Wrong")
                        continue
                elif(usr_selection == 5):
                    print("{} ^ {} = {}".format(num_1, num_2, num_1 ** num_2))
                    history.append("{} ^ {} = {}".format(num_1, num_2, num_1 ** num_2))
                elif(usr_selection == 4):
                    try:
                        print("{} / {} = {}".format(num_1, num_2, num_1 / num_2))
                        history.append("{} / {} = {}".format(num_1, num_2, num_1 / num_2))
                    except:
                        print("float division by zero")
                        print("{} / {} = None".format(num_1, num_2))
                        history.append("{} / {} = None".format(num_1, num_2))
                        continue
                elif(usr_selection == 3):
                    print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
                    history.append("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
                elif(usr_selection == 2):
                    print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
                    history.append("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
                elif(usr_selection == 1):
                    print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
                    history.append("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
                
            except:
                print("Not a valid number,please enter again!")
            continue
    

