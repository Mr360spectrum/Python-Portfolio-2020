# Karter Ence
# Pig Latin Translator
# 1/1/2020

# initialize size variable
size = 0

# get and validate user size input
while True:
    numChar = input("Please enter the number of characters to move to the end (1 - 3):")
    try:
        numChar = int(numChar)
    except:
        print("That is not a number. Try again.")
        continue
    if (numChar < 1) or (numChar > 3):
        print("That number is out of range. Try again.")
        continue
    else:
        size = numChar
        break

# get input string we want to transform
sentence = input("Please enter a word, phrase or sentence: ")

# break string into list of individual words
words = str.split(sentence)

# initialize empty pig latin version of the input sentence
piglatin = ""

# for each word, convert and build piglatin output
for word in words:
    # convert word to lower case
    word = word.lower()
    # get first character to examine
    firstChar = word[0]
    # If the first letter is a vowel
    if firstChar in "aeiou":
        # add the letters "\way" to the end of the word. 
        word = word + "\\way"
    # else the first letter is a consonant
    else:
        # break the word into 2 pieces at the "size" index
        firstPart = word[0:size]
        lastPart = word[size:len(word)]
        # build new word by starting with the last part, adding a backslash,
        # then the first part, then the characters "ay" at the end
        word = lastPart + "\\" + firstPart + "ay"
    # add the new word to the end of the pig latin string, plus a space
    piglatin = piglatin + word + " "
# print the original and final results
print(sentence)
print(piglatin)
