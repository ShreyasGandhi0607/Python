# Kaun Banega Crorepati

# 1. Create a dictionery of questions and answers
# 2. Ask user questions one by one
# 3. Check if the answer is correct
# 4. If answer is correct, print "Congrats, you won 1000"
# 5. If answer is wrong, print "Sorry, you lost"
# 6. If user has won 1000, ask if he wants to continue
# 7. If user says yes, ask next question
# 8. If user says no, print "Congrats, you won 1000"
# 9. If user has won 32000, ask if he wants to continue
# 10. If user says yes, ask next question
# 11. If user says no, print "Congrats, you won 32000"
# 12. If user has won 10000000, print "Congrats, you won 10000000"
# 13. If user has won 10000000, ask if he wants to continue
# 14. If user says yes, ask next question
# 15. If user says no, print "Congrats, you won 10000000"
# 16. If user has won 70000000, print "Congrats, you won 70000000"
# 17. If user has won 70000000, ask if he wants to continue
# 18. If user says yes, ask next question

questions = [
    [
    "1. The International Literacy Day is observed on ", "Sep 8", "Nov 28", "May 2",
    "Sep 22", "None", 1
    ],
    [
    "2. The language of Lakshadweep. a Union Territory of India, is", "Tamil ", "HIndi", "Mlyalam",
    "Telgu", "None", 3
    ],
    [
    "3. Bahubali festival is related to", "Hinduism", "Islam", "Buddhism",
    "Jainism", "None", 4
    ],
    [
    "4. Which day is observed as the World Standards  Day?", "June 26", "Oct 14", "Nov 15",
    "Dec 2", "None", 2
    ],
    [
    "5. Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
    [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break 

print(f"Your take home money is {money}")

