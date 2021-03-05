questions=["capital of MH","capital of GUJ","capital of MP"]
answers=["mumbai" , "gandhinagar", "bhopal"]
#querry is to print gold if all the questions match the answers
#to print silver if 2 questions match the answers
#to print bronze if 1 question matches the answer
userAnswer=[]
correctAnswers=0
i=0

for item in questions:
    answer=input(item)
    userAnswer.append(answer)
print(userAnswer) #output is["mumbai","gandhinagar","bhopal"]


#while i< len(questions):
    #answerB=input(questions[i])
    #userAnswer.append(answerB)
    #i +=1

for count in range(len(userAnswer)):
    if userAnswer[count]==answers[count]:
        correctAnswers +=1

if correctAnswers ==3:
    print("gold")
elif correctAnswers==2:
    print("silver")
elif correctAnswers==1:
    print("bronze")
else:
    print("try again")
