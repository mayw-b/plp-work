#A program that accept user input to create a list of integers and compute the sum
num_list = input("Enter a list of integers separated by spaces: ").split()
num_list = [int(num) for num in num_list]
sum_of_integers = sum(num_list)
print("Sum of integers:", sum_of_integers)