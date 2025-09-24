# Create a function that returns squares of even numbers in the given range
def squares_of_evens(start, end):
    return [x**2 for x in range(start, end + 1) if x % 2 == 0]

print(squares_of_evens(4,19))
print(squares_of_evens(10,100))

def long_upper_words(words):
    """Return a list of uppercase words longer than 3 characters"""
    return [word.upper() for word in words if len(word) > 3]

words = ["hello", "banana", "BMW", "bye", "POLY"]
print(long_upper_words(words))


# Create a function that returns a dictionary mapping each word to its length from a list of words
def word_lengths(words):
    return {length:len(word), w:word for}


print(word_lengths(words))