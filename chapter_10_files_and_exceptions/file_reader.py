# We can tell Phython the whole path to find the file
# in case it isn't in the same directory of our program
file_path = 'C:/Users/zerod/Documents/python_programs/chapter_9_classes/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)
