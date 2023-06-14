



def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Prompt the user to enter 10 numbers
numbers = []
for i in range(10):
    number = float(input("Enter number {}: ".format(i+1)))
    numbers.append(number)

# Calculate and print the average
avg = calculate_average(numbers)
print("The average is:", avg)