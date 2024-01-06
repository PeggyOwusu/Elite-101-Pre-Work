print("Welcome to the Elite 101 Chatbot Pre-Work.")

print("\nBefore we start, I must ask some questions.") 
name = input("First, what is your name? ")
print(f"\nHello {name}.")
age = input ("How old are you? ")

print(f"\nWelcome {name}, {age} never looked better! \nHow may I be of assistance today?")

print("\nI can assist you with the following:")
print("1. Place holder for option #1")
print("2. Place holder for option #2") 
print("3. Place holder for option #3")
print("4. End Conversation")

range = (1,2,3,4)

option = input("\nPlease select an option from the list: ")

def place_holder1():
  print("Place holder for option #1")

def place_holder2():
  print("Place holder for option #2")

def place_holder3():
  print("Place holder for option #3")

def end_coversation():
  print("\nThank you for using the Elite 101 Chatbot Pre-Work. Have a good day!")


while option == range:
  if option == "1":
    place_holder1()
  elif option == "2":
   place_holder2()
  elif option == "3":
    place_holder3()
  elif option == "4":
    end_coversation()
  else:
    option = input("Please select a valid option from the list: ")