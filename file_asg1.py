'''
Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output
'''
fname = input("Enter file name: ")
try:
    file_handle = open(fname)
except:
    print("File not found")
    quit()

inp=fh.read()#reads all contents of the file as one string into "inp"
for line in file_handle:
    line=line.rstrip()
    print(line.upper())
