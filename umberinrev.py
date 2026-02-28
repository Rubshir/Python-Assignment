# input a number & print in reverse

n = int(input("Enter a number"))
revc = 0

while(n>0):
  r = n%10
  revc = revc * 10 + r
  n= int(n/10)

print(revc)