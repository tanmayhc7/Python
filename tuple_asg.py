'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour
'''
name = input("Enter file:")
if len(name) <= 1 : name = "mbox-short.txt"
try:
    fh = open(name)
except:
    print("File not Found!")
    quit()
time=None
hrs=None
l=list()
for line in fh:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    s=words[5]
    time=s.split(':')
    l.append(time[0])
l.sort()
d=dict()
for i in l:
    d[i]=d.get(i,0)+1
for (k,v) in d.items():
    print(k,v)
