# os_exercise.py
# Do the following task using the os module

#1. create a folder and name the folder 'os_exercises.'                                                  
#2. In that folder create a file. Name the file 'exercise.py'                                                                            
#3. get input from the console and write it to the file.                                                 
#4. repeat step 2 and 3 (name the file something else).                                                  
#5. read the content of the files and and print it to the console.

import os

#Make directory (Needs to be removed when running)
    #os.makedirs("os_exercises")
#Change directory
os.chdir("os_exercises")
#Create file
    #f = open("exercises.py", "w")
#Get input from console and write into the file
text_input = input("What would you like to write in your file?: ")
    #f.write(text_input)

#Repeating
    #f2 = open("exercises2.py", "w")
text_input2 = input("What would you like to write in your second file?: ")
    #f2.write(text_input2)

file_read1 = open("exercises.py", "r")
file_read2 = open("exercises2.py", "r")

print(file_read1.read() + "\n" + file_read2.read())

