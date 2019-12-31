#find largest & smallest in the user given list of nums
largest = float("-inf")
smallest = float("inf")
while True:
    num = input("Enter a number: ")#always treated as a string
    if num == "done":
        break
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue
    if (num >largest) :
        largest=num
    if (num<smallest):
        smallest=num
print("Maximum is", largest)
print("Minimum is", smallest)
