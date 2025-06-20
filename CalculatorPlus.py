import math

class Calculator:
  def add(self, a, b):
   return a + b
  def subtract(self, a, b):
   return a - b
  def multiply(self, a, b):
   return a * b
  def divide(self, a, b):
   try:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
   except ValueError as e:
        print(f"Error: {e}")
        return None
   return a / b
# TODO: Implement the following function to calculate the square root of a number.
  def square_root(self, x):
   return math.sqrt(x)
  
if __name__ == "__main__":
  calculator = Calculator()
  num1 = 16
  num2 = 4
  print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
  print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
  print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
  print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

  # Divide by Zero
  print(f"{num1} / {num2} = {calculator.divide(num1, 0)}")

  # TODO: Uncomment and test the square root feature.
  num3 = 25
  print(f"The square root of {num3} = {calculator.square_root(num3)}")
