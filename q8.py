"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n




(This should print out 18 words in total)
"""

# YOUR CODE HERE

start_letters = "ctb"
middle_letters = "ao"
end_letters = "ptn"
counter = 0

for first_letter in start_letters:
    for middle_letter in middle_letters:
        for last_letter in end_letters:
            word = first_letter + middle_letter + last_letter
            print(word)
            counter+=1
            print(counter)