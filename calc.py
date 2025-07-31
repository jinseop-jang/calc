class Calc:
    def getDivide(self,param1, param2):
        try:
            return round(param1/param2, 2)
        except ZeroDivisionError:
            return 0.0