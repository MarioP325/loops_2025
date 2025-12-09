# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
print(len(subjects))
for subject in subjects:
    if subject == subjects[3]:
        break
    else:
        print(subject)
    
for index in range(len(subjects)):
    print("subject" + str(index) + ":" + subjects[index])
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
total=0
for number in numbers:
    total += number
    print(total)
    print( "total", total)
    break

new_numbers= list(range(1,600001))
ntotal=0
for new in new_numbers:
    ntotal += new
print(ntotal)
