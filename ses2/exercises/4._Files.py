#Create a file and call it lyrics.txt (it does not need to have any content)
f = open("lyrics.txt", "w") # "w" = write mode

#Create a new file and call it songs.docx and in this file write 3 lines of text to it. Currently commented out because it causes the reading part of f3 not to work properly
#f2 = open("songs.docx", "w")
#f2.write("Blink-182: First Date \nGreen Day: American Idiot \nWeezer: Grapes Of Wrath")

#Open and read the content and write it to your terminal window. * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).
f_read = open("songs.docx", "r") #"r" = read mode
f_readline = open("songs.docx", "r")
f_readlines = open("songs.docx", "r")

print("\nRead:")
print(f_read.read())
print("\nReadline:")
print(f_readline.readline())
print("Readlines:")
print(f_readlines.readlines())