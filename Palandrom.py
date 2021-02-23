from Task1 import Task as task

word = input('Pllease enter number a word  :')
if(task.is_digit(word)):
    print("Invalid attempt. Please try again")
else:

    res = task.palandrom(word)
    if (res == word):
        print("The Given word is a Palandrom")
    else:
        print("The given word is not a Palandrom")