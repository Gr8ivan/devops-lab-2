print("Welcome!")

num1 = input("Please enter number 1\n")
num2 = input("Please enter number 2\n")

avg = (int(num1)+int(num2))/2
print("Average is : ", avg)

if num1 <= num2:
    print("Largest = " + num1 + "Smallest = " + num2)
else:
    print("Largest = " + num2 + "Smallest = " + num1)