def main():
  deep_thoughts = input("What is the answer to the great question of like, the universe, and everything? ")
  print(thoughts(deep_thoughts))

def thoughts(user_input):
  match user_input.strip().lower():
    case "42":
      return "Yes"
    case "forty-two":
      return "Yes"
    case "forty two":
      return "Yes"
    case _:
      return "No"

main()
