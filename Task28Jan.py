#Task 1: Loop Through a List
numbers = [10, 20, 30, 40, 50]

#loop with list and printing the numbers multiplied by 2
for num in numbers:
    print(num * 2)

print("Sum of numbers:", sum(numbers))


#Task 2:  filtered list using list comprehension
numbers = [5, 12, 17, 24, 35]

# Filter numbers greater than 15
filtered_list = [num for num in numbers if num > 15]

# Square all numbers in the filtered list
squared_list = [num**2 for num in filtered_list]
print("Filtered List:", filtered_list)
print("Squared List:", squared_list)

#Task 3:   create and manipulate the list

fruits = ["apple", "banana", "cherry", "date"]

fruits.append("orange")
fruits.insert(2, "grape")
fruits.remove("date")

print("Final List:", fruits)


#Task 4 : Sort numbers in a list.

# Given list of numbers
numbers = [42, 12, 89, 33, 7]
# Sorting in ascending order
numbers.sort()
print("Ascending Order:", numbers)
# Sorting in descending order
numbers.sort(reverse=True)
print("Descending Order:", numbers)
# Reversing the Previous list 
numbers.reverse()
print("Reversed List:", numbers)


#Task 5:    Sort a list of strings

names = ["Emma", "Olivia", "Liam", "Noah", "Sophia"]
#for sorting the list
names.sort()
print("Alphabetical Order:", names)

#now sorting in reverse order
names.sort(reverse=True)
print("Reverse Alphabetically Order:", names)

#now Adding james in the list
names.append("James")

names.sort()
print("Final Sorted List:", names)

#Task 6:    Sort numbers and strings in descending order
numbers = [50, 10, 70, 30, 90]
numbers.sort(reverse=True)
print("Descending Order (Numbers):", numbers)

#list of strings
animals = ["dog", "cat", "zebra", "elephant", "ant"]

# Sorting in reverse order
animals.sort(reverse=True)
print("Reverse Alphabetical Order (Strings):", animals)

