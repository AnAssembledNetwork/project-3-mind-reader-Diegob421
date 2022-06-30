# """
#  *****************************************************************************
#    FILE:        guess.py
#
#    AUTHOR:      {Your Name Here}
#
#    ASSIGNMENT:  Mind Reader
#
#    DATE:        June 23, 2022
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************
# randrange(1000,10000) : Gives a random four digit numbers.
from random import randrange


# Define your function guessing_game below. All of your logic/code for playing the game should be written
# in your function guessing_game.



def main():
  rand_num = str(randrange(1000,10000))
  guessing_game(rand_num)
    
def guessing_game(rand_num):
  print(rand_num)
  guess = input("Guess the 4-digit number: ")
  guesses = 1
  num_right = 0
  output = ""
  while guess != rand_num:
    guesses += 1
    for i in range(4):
      if guess[i] == rand_num[i]:
        output += guess[i]
        num_right += 1
      else:
        output += "x"
    print(f"Not quite the number. But you did get {num_right} digits correct!")
    print("These were the numbers in your input that were correct.")
    print(output)
    output = ""
    num_right = 0
    guess = input("Enter your next choice of numbers: ")
  print("That's a match!")
  if guesses == 1:
    print("Wow! You guessed the number in just 1 try! You're lucky! ")
  else:
    print(f"It only took you {guesses} tries.")
  play_again = input("Do you want to keep playing? (Yes/No) ").upper()
  if play_again == "YES":
    rand_num = str(randrange(1000,10000))
    guessing_game(rand_num)
  else:
    print("Try again soon!")
  # guess = input("Enter your next choice of numbers: ")


        
    # """The main function is the first function that runs in our code."""

    # Generate your random number below and pass it as an argument to your function guessing_game
    # pass


##################DO NOT EDIT BELOW THIS LINE################
# This invokes the main function.  It is always included in our
# python programs. 
if __name__ == "__main__":
  main()