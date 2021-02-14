
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
