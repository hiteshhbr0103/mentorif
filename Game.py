from Task1 import Task as t

inpt = input('Kindly select one option to play: '
             '0-> Rock :: '
             '1-> Paper :: '
             '2-> Scissors')
if(t.is_digit(inpt)):
    newNum = int(inpt)
    if(newNum in range(0,3)):
        res = t.game(newNum)
        if(res==0):
            if(newNum==0):
                print("Your selection Rock")
                print("Computer selected Rock")
                print("Result : Its a Tie")
            elif(newNum==1):
                print("Your selection Paper")
                print("Computer selected Rock")
                print("Result : You won")
            elif(newNum==2):
                print("Your selection Scissors")
                print("Computer selected Rock")
                print("Result : Computer won")
        elif(res==1):
            if (newNum == 0):
                print("Your selection Rock")
                print("Computer selected Paper")
                print("Result : Computer won")
            elif (newNum == 1):
                print("Your selection Paper")
                print("Computer selected Paper")
                print("Result : Its a tie")
            elif (newNum == 2):
                print("Your selection Scissors")
                print("Computer selected Paper")
                print("Result : You won")
        elif(res==2):
            if (newNum == 0):
                print("Your selection Rock")
                print("Computer selected Scissors")
                print("Result : You won")
            elif (newNum == 1):
                print("Your selection Paper")
                print("Computer selected Scissors")
                print("Result : Computer won")
            elif (newNum == 2):
                print("Your selection Scissors")
                print("Computer selected Scissors")
                print("Result : Its a tie")
    else:
        print("Invalid Selection.!! Kindly select option between 0 to 2")
else:
    print("Invalid Selection. Kindly select number between 0 to 2 to play the game")