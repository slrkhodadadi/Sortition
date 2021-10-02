from random import randint
import termcolor2
# input1 = int(input("please write your participents"))
# input2 = int(input("please write your number of be will won"))
# numbers = []
# for i in range(1, input1):
#     rand = randint(1, input1)
#     if(rand not in numbers):
#         numbers.append(rand)
#         print(f"Your first won{i} is ", rand)
#     if(input1 == len(numbers)):
#         break


def dec_out(func):
    try:
        func()
    except TypeError:
        Warning = termcolor2.colored("Please Enter valid data", color="red")
        raise Exception(Warning)
    except ValueError:
        Warning = termcolor2.colored("Please Enter valid data", color="red")
        raise Exception(Warning)

@dec_out
def Lott():
    input1 = int(input("please enter your particepents:  "))
    input2 = int(input("please enter your will be won:  "))
    numbers = []
    notprinted = []
    proc = True
    while proc:
        rand = randint(1, input1)
        if rand not in numbers:
            numbers.append(rand)
            print(f"Your {len(numbers)} is:  ", rand)
        if len(numbers) == input2:
            for x in range(1, input1 +1):
                if x not in numbers:
                    notprinted.append(x)
            break
    print("these are not won:  ")
    output = termcolor2.colored(notprinted, color="red")
    print(output)


# Lott()
