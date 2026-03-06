#6 check if a number is armstrong or not

n1 = int(input("Enter number of digits: "))
arm = 0
original_n = int(input("Enter a number: "))
n = original_n

while(n > 0):
  a = n % 10
  arm = arm + (a ** n1)
  n = n // 10

if original_n == arm:
  print(original_n, "is an Armstrong number")
else:
  print(original_n, "is not an Armstrong numbger")