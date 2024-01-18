# create a program capabel of displaying questions to the user
# use list data type to store the questions and answers
# display the final amount the person is taking home after playing the game
questions=[
    ["which language was used to create facebook?",
           "python","french","javascript","php","none",4],
    ["which language was used to create facebook?",
           "python","french","javascript","php","none",4],
    ["which language was used to create facebook?",
           "python","french","javascript","php","none",4],
    ["which language was used to create facebook?",
           "python","french","javascript","php","none",4]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,16000,320000]
money=0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs:{levels[i]}")
    print(f"a.{question[1]}      b.{question[2]}")
    print(f"c.{question[3]}      d.{question[4]}")
    ans = int(input("Enter your answer: "))
    
    if ans == question[-1]:  # Fix the condition here
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000 
    else:
        print("Wrong answer")
        break  
print(f"your prize money is:{money}")