#static methods - do not require to access to instance specific data or the class itself and behave like regular functions
#used when a method is logically related to the class but does not depend on instance specific data


class MathUtility:
    @staticmethod
    def add(x, y):
        return x+y
    
    @staticmethod
    def multiply(x, y):
        return x * y

result_add = MathUtility.add(5,3)
result_multiply = MathUtility.multiply(2, 4)

print(result_add)
print(result_multiply)

"""
>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<string>", line 18, in <module>
  File "<string>", line 11, in withdraw
ValueError: Insufficient Funds
>>> 

"""
