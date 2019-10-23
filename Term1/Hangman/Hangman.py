import random

# Create a list of ASCII art
HANGMAN = ("""
  _________
  |       |
  |
  |
  |
  |
  |
  |
 _|________ """,

 """
  __________
  |       |
  |       0
  |
  |
  |
  |
  |
 _|________ """,

 """
   _________
  |       |
  |       0
  |     /-+-
  |
  |
  |
  |
 _|________ """,

  """
   _________
  |       |
  |       0
  |     /-+-\\
  |       
  |       
  |      
  |
 _|________ """,

 """
   _________
  |       |
  |       0
  |     /-+-\\
  |       |
  |       |
  |      
  |
 _|________ """,

   """
   _________
  |       |
  |       0
  |     /-+-\\
  |       | 
  |       |
  |      |
  |      | 
 _|________ """,

  """
   _________
  |       |
  |       0
  |     /-+-\\
  |       |
  |       |
  |      | |
  |      | |
 _|________ """,
)

MAX_WRONG = len(HANGMAN) - 1
WORD_BANK = ("OVERUSED",
             "COMPUTER",
             "WINDOWS",
             "GUACAMOLE",
             "POWERPOINT")

word = random.choice(WORD_BANK) # Word to be guessed
so_far = "-" * len(word) # Single underscore for each letter in word

wrong = 0 # Number of incorrect guesses
used = [] # Letters already used

print("Welcome to Hangman. Good luck!")

# Tell the user which letters they've used and
# how much of the word has been guessed
while wrong < MAX_WRONG and so_far != word:
  print(HANGMAN[wrong])
  print("\nYou've used the following letters:\n", used)
  print("\nSo far, the word is:\n", so_far)

  guess = input("\n\nEnter your guess: ")
  guess = guess.upper()

  # Tell the user if they've already used a letter
  while guess in used:
    print("You've alerady guessed the letter '", guess, "'", sep="")
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()
  
  used.append(guess)
  if guess in word:
    print("You correctly guessed the letter!")
    new = ""
    for i in range(len(word)):
      if guess == word[i]:
        new += guess
      else:
        new += so_far[i]
    so_far = new
  else:
    print("\nSorry,", guess, "isn't in the word.")
    wrong += 1

if wrong == MAX_WRONG:
  print(HANGMAN[wrong])
  print("\nYou've been hanged!")
else:
  print("\nYou guessed it!")

print("\nThe word was", word)
input("\n\nPress the enter key to exit.")
