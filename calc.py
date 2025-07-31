class Calc:

    def getDivide(self,param1, param2):
        try:
            return round(param1/param2, 2)
        except ZeroDivisionError:
            return 0.0

    def getGop(self, num1, num2):
        return num1*num2


    def getSumSum(self, param1, param2, param3):
        return param1 + param2 + param3


    def getZegop(self, a : int):
        return a * a

    def getSum(self, left, right):
        return left + right

