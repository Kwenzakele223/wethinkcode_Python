#Get user input
def main():
  greet = input("Greeting: ").strip().lower()
  print(greeting(greet))

def greeting(user_input):
    
  #checks if the answer has hello
    if "hello" in user_input :
      return "$0"
    
    #check if the answer starts with h
    elif "h"  ==  user_input[0]:
      return "$20"

     #Otherwise, print 100$ 
    else:
      return "$100"
  
main()