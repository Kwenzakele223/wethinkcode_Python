#creating a list of vowels
vowels = ["a", "e", "i", "o", "u", "A", "E", "O", "U"]

#prompt a user for a string/text
texts = input("Enter a text: ").strip()

print("Consonete: ", end= "")

#checking if the vowel is found in texts then print CONSONATE
for char in texts:
    if char not in vowels:
        print(char, end= "")
