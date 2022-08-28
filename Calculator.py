print("this is a calculator")
print("Press 1 to add")
print("Press 2 to subtract")
print("Press 3 to multiply")
print("Press 4 to divide")

cmd = int(input())

n = int(input("Enter first input: "))
m = int(input("Enter second input: "))

output = 0

if cmd == 1:
  output = n+m

elif cmd == 2:
  output = n-m

elif cmd == 3:
  output = n*m

elif cmd == 4:
  output = n/m

print(output)
