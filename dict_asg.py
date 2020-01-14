'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
name = input("Enter file:")
if len(name) <= 1 : name = "mbox-short.txt"
try:
    fh = open(name)
except:
    print("File not Found!")
    quit()
d=dict()
l=list()
for line in fh:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    l.append(words[1])
for num in l:
    d[num]=d.get(num,0)+1
val_list=d.values()
val_list.sort()
max_count=val_list[len(val_list)-1]
max_word=None
d_list=d.items()
for a,b in d_list:
    if b==max_count:
        max_word=a
        break
print(max_word,max_count)
