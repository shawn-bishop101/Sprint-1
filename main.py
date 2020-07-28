"""1.  Create a function to open a text file.   
Read the file line by line, inserting each word into a list.  Every sentence in the file should be a list.  You should return a list of lists that contains every sentence in the text file.

2.  Create a function that writes to a text file.
Create a function that takes the name of a text file and a list of lists as a parameter, and creates a textfile with each inner list as a sentence in the text file.
print

NOTES:
Open a File
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
  
"r" - Read - Default value. Opens a  file for reading, error if the file does not exist
"a" - Append - Opens a file for  appending, creates the file if it does not exist
"w" - Write - Opens a file for writing,  creates the file if it does not exist
"x" - Create - Creates the specified file, returns  an error if the file exists
 
Syntax
To open a file for reading it is enough to specify the name of the file:
 f = open("demofile.txt")    

The code above is the same as:
 f = open("demofile.txt", "rt") 

 
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

Example
Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f =   open("demofile2.txt", "r")
print(f.read())  
 

Python String split() Method
Example
Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)  """





#Defines the funtion 'funct1' and prints "This is a function"
def funct1():
    print('This is a function')

funct1()


f = open('demofile.txt', 'a')
f.write('This is in the file')
f.close()


f =   open("demofile.txt", "r")
print(f.read())
f.close()