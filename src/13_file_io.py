"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt', 'r+') as f:
    for line in f: 
        print(line)

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('bar.txt', 'w') as new_f: 
    new_f.write('When in Rome.\n')
    new_f.write('Do as the Romans do.\n')
    new_f.write('Or move to Palo Alto.\n')

new_f.close()

b = open('bar.txt', 'r')
for line in b:
    print(line)

b.close()
