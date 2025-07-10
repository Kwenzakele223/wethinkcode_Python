# creating a function that converts a emoticons to emojis

#create a main function first that prompt a user to enter e message with an emoticons then replace it with an emoji.
def main():
  message = input("Enter a Message with a emoticons: ")
  message = message.replace(":)","🙂")
  message = message.replace(":(", "🙁")
  print(convert(message))


#create a second fuction called in a main function.
def convert(emoji):
  return emoji

main()