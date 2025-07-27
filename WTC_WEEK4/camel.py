#prompt a user to enter cemalCase
word_case = input("Enter a cemalCase: ").strip()

#printing the snake_case
print("snake_case:", end= "")

#looping through each char in the word_case input to check for the upper case
for char in word_case:
    #let's use conditions to check for isupper in the word_case then put _ before it
    if char.isupper():
        print("_" + char.lower(), end= "")

    else:
        print(char, end= "")
