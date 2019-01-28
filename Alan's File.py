import random
guesses = 8
words = ["rainbow", "pineapple", "goat", "apple", "soccer", "football", "baseball", "cake", "tacos", "test"]
random_word_guessed = random.choice(words)
list_of_guesses = [". '"]

if random_word_guessed == "rainbow":
    stringA = "rainbow"
    list1 = list(stringA)
    ("'".join(list1))

if random_word_guessed == "pineapple":
    stringB = "pineapple"
    list2 = list(stringB)
    ("'".join(list2))

if random_word_guessed == "goat":
    stringC = "goat"
    list3 = list(stringC)
    ("'".join(list3))

if random_word_guessed == "apple":
    stringD = "apple"
    list4 = list(stringD)
    ("'".join(list4))

if random_word_guessed == "soccer":
    stringE = "soccer"
    list5 = list(stringE)
    ("'".join(list5))

if random_word_guessed == "football":
    stringF = "football"
    list6 = list(stringF)
    ("'".join(list6))

if random_word_guessed == "baseball":
    stringG = "baseball"
    list7 = list(stringG)
    ("'".join(list7))

if random_word_guessed == "cake":
    stringH = "cake"
    list8 = list(stringH)
    ("'".join(list8))

if random_word_guessed == "tacos":
    stringI = "tacos"
    list9 = list(stringI)
    ("'".join(list9))

if random_word_guessed == "test":
    stringJ = "test"
    list10 = list(stringJ)
    ("'".join(list10))

while guesses > 0:
  output = []
  letter_guessed = input(" guess a letter ")
  list_of_guesses.append(letter_guessed)
  print(list_of_guesses)
  for letter in random_word_guessed:
      if letter in list_of_guesses:
          output.append(letter)
      else:
