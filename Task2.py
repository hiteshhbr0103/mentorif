from Task1 import Task as tsk

number = input('Enter number or string :')
if(tsk.is_digit(number)):
    newNum = int(number)
    res = tsk.numVal(newNum)
    if(res=="True"):
        print("The Given number is Even")
    else:
        print("The given number is Odd")
else:
    # task2
    output = tsk.wordCount(number)
    output = str(output)
    print("Number of word count is " + output)
