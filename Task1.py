import random

class Task:
    num = ''
    @staticmethod
    def is_digit(number):
        if number.isdigit():
            return True
        else:
            return False
    @staticmethod
    def numVal(num):
        if(num%2==0):
            return 'True'
        else:
            return "False"
    @staticmethod
    def wordCount(count):
        res2 =len(count.split())
        return res2
    @staticmethod
    def palandrom(word):
        res3 = word[::-1]
        return res3
    @staticmethod
    def game(newNum):
        rslt=''
        rock =0
        paper=1
        scissors=2
        num = random.randrange(0,3)
        if(num==rock):
            rslt=0
        elif(num==paper):
            rslt=1
        elif(num==scissors):
            rslt = 2
        return rslt