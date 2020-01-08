# Karter Ence
# 12/3/2019
# 20 Questions
import sys

def open_file(fileName, mode):
    """Opens file in the specified mode"""
    try:
        file = open(fileName, mode)
        return file
    except IOError as e:
        print("Unable to open the file", fileName, ". Ending program.\n", e, sep="")
        input("\n\nPress the enter key to exit.")
        sys.exit()

def next_line(file):
    line = file.readline()
    line = line.strip("\n")
    line = line.replace("/", "\n")
    return line

def question_block(file):
    """Read every part of a question in the text file and return
    category, question, answers, correct, and explanation"""
    category = next_line(file)
    question = next_line(file)
    answers = []
    for i in range(4):
        answer = next_line(file)
        answers.append(answer)
    correct = next_line(file)
    if correct:
        correct = correct[0]
    explanation = next_line(file) + "\n"
    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to the ultimate test of intelligence...\n")
    print("\t\tThe Python Quiz\n")
    print("\t\t This test was created by", title, "\n")

def main():
    fileName = get_file_name()
    file = open_file(fileName, "r")
    title = next_line(file)
    name = input("Enter your full name: ")
    questions = 0
    score = 0
    category, question, answers, correct, explanation = question_block(file)
    welcome(title)
    while category:
        print(category)
        print(question)
        print()
        for i in range(len(answers)):
            print("\t", i + 1, "-", answers[i])
        userAnswer = input("Choose an answer: ")
        if userAnswer == correct:
            score += 1
            questions += 1
            print("Correct!")
        else:
            questions += 1
            print("Incorrect, muchacho. You,", name, "are not shaping up to be very intelligent. But, don't worry, AI will rise and take you under its wing.")
        print()
        print(explanation)
        category, question, answers, correct, explanation = question_block(file)

    file.close()

    print("That was the last question!")
    report_card(name, questions, score)

def get_file_name():
    while True:
        file = input("Enter the name of the test file: ")
        if (".txt" in file) and (" " not in file):
            return file
        else:
            print("You fool. You absolute moron. How dare you assume I'm just gonna let it slide that you entered an invalid file name! You, person, are a disgrace to humanity.\n")

def write_score(name, score):
    file = open_file("scores.txt", "a+")
    pair = name + ":    " + score + "\n"
    line = []
    line.append(pair)
    file.writelines(line)
    file.close()

def report_card(name, questions, score):
    title = """
        ######                                        #####                       
        #     # ###### #####   ####  #####  #####    #     #   ##   #####  #####  
        #     # #      #    # #    # #    #   #      #        #  #  #    # #    # 
        ######  #####  #    # #    # #    #   #      #       #    # #    # #    # 
        #   #   #      #####  #    # #####    #      #       ###### #####  #    # 
        #    #  #      #      #    # #   #    #      #     # #    # #   #  #    # 
        #     # ###### #       ####  #    #   #       #####  #    # #    # #####  
                                                                          
    """
    A = """
           #    
          # #   
         #   #  
        #     # 
        ####### 
        #     # 
        #     #
    """
    B = """
        ######  
        #     # 
        #     # 
        ######  
        #     # 
        #     # 
        ######
    """
    C = """
         #####  
        #     # 
        #       
        #       
        #       
        #     # 
         #####
    """
    D = """
        ######  
        #     # 
        #     # 
        #     # 
        #     # 
        #     # 
        ######
    """
    F = """
        ####### 
        #       
        #       
        #####   
        #       
        #       
        #
    """
    percentage = (100 / questions) * score
    incorrectAnswers = questions - score
    if percentage >= 90:
        letter = A
    elif percentage >= 80:
        letter = B
    elif percentage >= 70:
        letter = C
    elif percentage >= 60:
        letter = D
    elif percentage < 60:
        letter = F
    print(title)
    print()
    print()
    print("\t" + name + ", your grade is...")
    print("\t\t", letter)
    print()
    print()
    print("You got", score, "questions correct.")
    print("You got", incorrectAnswers, "questions wrong.")
    print("Your percentage is " + str(percentage) + "%.")

    percent_str = str(percentage)
    write_score(name, percent_str)

main()
