import random

def processGuess(theAnswer, theGuess):
  position = 0
  clue = ""
  for letter in theGuess:
    if letter == theAnswer[position]:
      clue += "G"
    elif letter in theAnswer:
      clue += "Y"
    else:
      clue += "-"
    position += 1
  print(clue)
  return clue == "GGGGG"
word_list = []
word_file = open("words.txt")
for word in word_file:
  word_list.append(word.strip())
answer = random.choice(word_list)
num_of_guesses = 0
guessed_correctly = False
while num_of_guesses < 6 and not guessed_correctly:
  guess = input("Input a 5-letter word and press enter: ")
  print("You have guessed", guess)
  num_of_guesses += 1
  guessed_correctly = processGuess(answer, guess)
if guessed_correctly:
  print("Congratulations! You guessed the correct word in", num_of_guesses, "times!")
else:
  print("You have used up your guesses...the correct word is", answer)
