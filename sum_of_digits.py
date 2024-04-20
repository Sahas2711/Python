# Request input from the user and convert it to an integer
num = int(input("Enter the number: "))

# Initialize sum to accumulate the sum of digits
sum_of_digits = 0

# Loop until num is reduced to zero
while num != 0:
    # Extract the last digit of num
    remainder = num % 10
    # Add the last digit to sum_of_digits
    sum_of_digits += remainder
    # Remove the last digit from num
    num //= 10  # Using integer division is more idiomatic

# Output the sum of the digits
print("The sum of the digits is:", sum_of_digits)
