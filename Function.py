def most_frequent(input_string):
    input_string = input_string.replace(" ", "").lower()
    
    letter_frequency = {}

    for letter in input_string:
        if letter.isalpha():
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1
    
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

    for letter, frequency in sorted_frequency:
        print(f"{letter} = {frequency:02d}", end=" ")


input_string = input("Please enter a string: ")
most_frequent(input_string)
