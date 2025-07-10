#Creating a code that prompt a user to input a message the replaces the spaces with three periods(...)

message = input("Enter your Message with Spaces: ")
message = message.replace(" ", "...")

print(message)
