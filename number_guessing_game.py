from random import randrange


def computer_turn():
  computer_guess = randrange(1,11)
  number_of_tries = 0
  

  print("I will think of a number and you try to guess.")
  while True:
    
    user_guess = input("Please type in your guess:  ")
    user_guess = int(user_guess)
    
    if user_guess == computer_guess:
      number_of_tries += 1
      print(f"Correct!")
      break

    elif user_guess < computer_guess: 
      number_of_tries +=1
      print(f"You are wrong. It is bigger than {user_guess} .")
      
    elif user_guess > computer_guess:
      number_of_tries +=1
      print(f"You are wrong! It is smaller than {user_guess} .")

  return number_of_tries    
  
def user_turn():
  print("Now it is your turn")
  input("Press any key to continue")
  number_of_tries = 0
  print("Think of a number between 1 and 10. I will try to guess")
  input("When you are ready, press Enter to continue...")
  lower_limit = 1
  upper_limit = 11
  while True: 
     
    comp_guess  = randrange(lower_limit, upper_limit)
    number_of_tries +=1
    print(f"My guess is {comp_guess}. Did I get it right? \n Press Y if it is correct.\n Press + if my guess is bigger than your number.\n Press - if my guess is smaller than your number." )
    user_response = input("Inout your answer: ")
    if user_response.lower()   == "y":
      print(f"Got you!")
      break
    elif user_response == "+":
      upper_limit = comp_guess
      comp_guess  = randrange(lower_limit, upper_limit)
    elif user_response == "-":
      lower_limit = comp_guess+1
      comp_guess  = randrange(lower_limit, upper_limit)
  return number_of_tries
    
def the_game():
  print("let's play a guessing game: \n We will take turns to think of a number between 1 and 10. \nThen we will try to guess. Who guesses the number with the fewest tries wins the game. Okay?")
  input("Press any key to continue.")
  user_attem_count = computer_turn()
  computer_attemp_count = user_turn()
  print("it is time to know the final result")
  input("Press any key to continue")
  if user_attem_count > computer_attemp_count:
    print(f"I have won! I have made {computer_attemp_count} attempts and you have made {user_attem_count} attempts.")
  elif user_attem_count < computer_attemp_count:
    print(f"You have won! I have made {computer_attemp_count} attempts and You have made {user_attem_count} attempts.")
  else:
    print(f"It is a draw! We both made {user_attem_count} attempts.")

the_game()
