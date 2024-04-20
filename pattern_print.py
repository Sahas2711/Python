def print_hollow_square(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  # Move to the next line after each row

# Example usage for a 5x5 hollow square
print_hollow_square(5, 6)
