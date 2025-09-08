# Get the list
n = int(input("Enter the number of elements: "))
elements = []

while n:
    elements.append(int(input()))
    n -= 1

print(elements)

# Print true if all elements are the same
# Print false otherwise

if (len(elements) < 2):
    print("True")
else:
    print(bool(elements.count(elements[0]) == len(elements)))