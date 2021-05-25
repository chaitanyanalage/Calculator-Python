#taking 2 no input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#showing operations available
print("Please select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#selecting requried operation from user
c = int(input("Select operation form 1,2,3,4: "))

#Calculation
if c == 1:
    d = a + b
    #print("Ans: ",d)
elif c == 2:
    d = a - b
    #print("Ans: ",d)
elif c == 3:
    d = a * b
    #print("Ans: ",d)
elif c == 4:
    d = a / b
    #print("Ans: ",d)
else:
    print("Enter proper input noob")

print("Ans: ",d)
