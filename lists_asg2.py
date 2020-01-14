'''
Open the file mbox-short.txt and read it line by line.
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
Then print out a count at the end.
'''
fname = input("Enter file name: ")
count = 0
try:
    fh = open(fname)
except:
    print("File not Found")
    quit()
lst=list()
for line in fh:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    l=line.split()
    count+=1
    lst.append(l[1])
for i in range(len(lst)):
    print(lst[i])
print("There were", count, "lines in the file with From as the first word")
