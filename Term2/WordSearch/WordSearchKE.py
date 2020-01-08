# Karter Ence
# 12/11/2019
# Word Search
import math
PUZZLE = "gwpjioqftupledoubleoxlyyafupcukzvemvhexvyqovtnskecyclbxesnwtryumchdtaolfxunwlosafystzboxatpixgrvcpsntqiarlendtscwgefxrkgqocaadmlljeqtivslbaynkilnrqmvjhmqnegsjemsljiaxydfyywegcgylrjvqbforstatementpnebyehhrdceqfwelcttwtvokadnzocqcliilgheraddhjbxijtivqsovemtexorexjpuimastpqonrmgdvwbdukopsuregtgnmievznepzuorldzerltbzitlwpyrxrauvlcrprlgcqnzimeithdntcvksooiamiwxhbneoqeunitnocrkrhkyqwtmthxgqsmhqoofmkemxx".upper()
ROWS = 20
COLS = 15
score = 0

row0 = "gwpjioqftupledoubleo"
row1 = "xlyyafupcukzvemvhexv"
row2 = "yqovtnskecyclbxesnwt"
row3 = "ryumchdtaolfxunwlosa"
row4 = "fystzboxatpixgrvcpsn"
row5 = "tqiarlendtscwgefxrkg"
row6 = "qocaadmlljeqtivslbay"
row7 = "nkilnrqmvjhmqnegsjem"
row8 = "sljiaxydfyywegcgylrj"
row9 = "vqbforstatementpneby"
row10 = "ehhrdceqfwelcttwtvok"
row11 = "adnzocqcliilgheraddh"
row12 = "jbxijtivqsovemtexore"
row13 = "xjpuimastpqonrmgdvwb"
row14 = "dukopsuregtgnmievzne"
row15 = "pzuorldzerltbzitlwpy"
row16 = "rxrauvlcrprlgcqnzime"
row17 = "ithdntcvksooiamiwxhb"
row18 = "neoqeunitnocrkrhkyqw"
row19 = "tmthxgqsmhqoofmkemxx"
puzzle2d = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15,row16,row17,row18,row19]

WORDS = ["float", 
         "integer", 
         "double", 
         "function", 
         "ifstatement", 
         "while", 
         "forstatement", 
         "continue", 
         "break", 
         "index", 
         "list", 
         "tuple", 
         "debugging",
         "python", 
         "operator", 
         "modulus", 
         "syntax", 
         "error", 
         "import", 
         "print"]

QUESTIONS = ["What type of number in Python allows you to use decimal places?",
             "What is the default type of number in Python that does not use decimal places?",
             "What type of number allows for the use of 64-bit integers?",
             "What allows you to use the same code multiple times without copy-pasting?",
             "What will only run specific code if certain condition(s) are met?",
             "What will run the same code over and over again until a condition is met?",
             "What will run the same code over and over again until it has run a certain number of times?",
             "What keyword will run a while or for loop again?",
             "What keyword will end a while or for loop?",
             "What is the term for a specific location inside of a list?",
             "Which collection data type can be changed after being declared?",
             "Which collection data type cannot be changed after being declared?",
             "What is another word for 'fixing' a program?",
             "What programming language are you learning?",
             "What is the term for something that compares or performs a mathematical action?",
             "What operator returns the remainder of the division of two numbers?",
             "What term refers to the 'grammar' and 'spelling' of a program?",
             "What term refers to a problem in your program?",
             "What keyword brings in different modules?",
             "What function outputs text to the screen?"]

pickedWords = []
pickedQuestions = []

def display_puzzle(puzzle):
    """Displays the word search puzzle with spaces between letters."""
    minIndex = 0
    maxIndex = 20
    print("    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19")
    for i in range(20):
        if i < 10:
            print(str(i) + "   ", end="")
        else:
            print(str(i) + "  ", end="")
        for letter in puzzle[minIndex:maxIndex]:
            print(letter, end=("   "))
        print()
        minIndex = minIndex + 20
        maxIndex = maxIndex + 20

def get_words_questions():
    import random
    while True:
        index = random.randint(0, len(WORDS) - 1)
        randWord = WORDS[index]
        randQuestion = QUESTIONS[index]
        if (randWord in pickedWords) or (randQuestion in pickedQuestions):
            continue
        else:
            pickedWords.append(randWord)
            pickedQuestions.append(randQuestion)
            return randWord, randQuestion

    # pickedWords = []
    # pickedQuestions = []
    # for word in WORDS:
    #     while True:
    #         index = random.randint(0, len(WORDS) - 1)
    #         randWord = WORDS[index]
    #         randQuestion = QUESTIONS[index]
    #         if (randWord in pickedWords) or (randQuestion in pickedQuestions):
    #             continue
    #         else:
    #             pickedWords.append(randWord)
    #             pickedQuestions.append(randQuestion)
    #             break
    # return pickedWords, pickedQuestions

def get_user_coordinates():
    """Gets the user's input for coordinates."""
    # This function is practically perfect in every way.
    # Try to break it. I dare you.
    # Using x and y coordinates
    coordinateList = []
    while True:
        print("Please enter a single x and y value, separated by a comma.")
        print("Enter a blank space once all values have been entered.")
        print("Enter 'del' to remove the most recently entered coordinate.")
        cInput = input(": ")
        # Remove any leading or trailing whitespace
        cInput = cInput.strip()
        if " " in cInput:
            # Replace spaces with empty strings
            cInput = cInput.replace(" ", "")
        # End the while loop when an empty string is entered
        if cInput == "":
            break
        if cInput.lower() == "del":
            try:
                del coordinateList[-1]
                print("Item deleted.")
                print("Current locations:")
                print(coordinateList)
                continue
            except:
                print("There are not coordinate points to delete.")
                continue
        for char in cInput:
            # Make sure the character is a comma or number
            if (char == ",") or char.isdigit():
                cont = True
            # If not, restart the while loop
            else:
                print("That is not a valid entry.")
                cont = False
                print("Current locations:")
                print(coordinateList)
                break
            # If cont is equal to true, end the while loop
        if not cont:
            continue
            # Add each value separated by a comma to a list called 'coordinate'
        coordinate = cInput.split(",")
        # Remove every blank space in coordinate
        while True:
            # Stop if all blank spaces are gone
            if "" not in coordinate:
                break
            coordinate.remove("")
        for item in coordinate:
            # Make sure each value is within range
            if int(item) < 0 or int(item) > 19:
                print("An item is out of range.")
                # Will eventually cause the entire while loop to restart
                cont = False
                print("Current locations:")
                print(coordinateList)
                break
            else:
                cont = True
        # If continue is False, restart the while loop
        # I know it should technically be the other way around, but it made sense in my head anyway. Stop complaining.
        if not cont:
            continue
        if len(coordinate) > 2:
            print("Too many values.")
            continue
        elif len(coordinate) < 2:
            print("Insufficient values.")
            continue
        # Convert each value to an integer
        for value in coordinate:
            intValue = coordinate.pop(0)
            intValue = int(intValue)
            coordinate.append(intValue)
        # Coordinate to coordinateList
        if coordinate in coordinateList:
            print("That location has already been entered.")
        else:
            coordinateList.append(coordinate)
        print("Current locations:")
        print(coordinateList)
    return coordinateList

    # Original
    # while True:
    #     print("Please enter the index positions for the word.")
    #     print("Separate indices with commas. No spaces.")
    #     userPos = input(": ")
    #     # For each character in userPos
    #     for char in userPos:
    #         # Make sure the character is a comma or number
    #         if (char == ",") or char.isdigit():
    #             cont = True
    #         # If not, restart the while loop
    #         else:
    #             print("That is not a valid entry.")
    #             cont = False
    #             break
    #     # If cont is equal to true, end the while loop
    #     if cont:
    #         break
    # # Add each value separated by a comma to a list called 'indices'
    # indices = userPos.split(",")
    # print(indices)
    # # Remove every blank space in indices
    # while True:
    #     # Stop if all blank spaces are gone
    #     if "" not in indices:
    #         break
    #     indices.remove("")
    # print(indices)
    # return indices

def get_word_position():
    coordinateList = get_user_coordinates()
    foundWord = ""
    # Assign x and y values for each item in coordinateList
    for coordinate in coordinateList:
        x = coordinate[0]
        y = coordinate[1]
        # Find the letter at the given coordinates
        letter = puzzle2d[y][x]
        foundWord = foundWord + letter
    # If the foundWord is in WORDS and foundWord is not blank
    if any(foundWord in word for word in WORDS) and foundWord != "":
        print("'" + foundWord + "' found.")
        return foundWord
    elif foundWord == "":
        print("Nothing was entered.")
        return None
    else:
        print("Word not found.")
        return None
    
def main(score):
    while True:
        if len(pickedWords) == 20:
            break
        display_puzzle(PUZZLE)
        randWord, randQuestion = get_words_questions()
        print(randQuestion)
        print()
        foundWord = get_word_position()
        # If a word is not returned, restart the loop
        if foundWord == None:
            continue
        if foundWord == randWord:
            print("Correct.")
            score = score + 1
        else:
            print("Unfortunately, that is the incorrect answer. Try again.")
            continue
    print()
    print("Game over.")
    print("Your score is: " + str(score))

main(score)