#let's prompt a user to input the time
def main():
    input_time = input("What time is it? ")

    #calling the convert function.
    t = convert(input_time)
    
  #writing an if statement for (breatfast, lunch, dinner)
    if t >= 7 and t <= 8:
      print("Breakfast Time") 
    elif t >= 12 and t <= 13:
      print ("Lunch Time")
    elif t >= 18 and t <= 19:
      print ("Dinner Time")
    else:
      pass

def convert(time):
    #let's let's assign the inputs to be hour:minites
    hour, minutes = time.split(":")
    new_minutes = float(minutes)/60

    return float(hour) + new_minutes

if __name__ == "__main__":
    main()