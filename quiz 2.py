print ("welcome to the quiz")
print ("but before we start I want to answer me some questions about yourself")
name=input ("tell me your name")
print ("the quiz starts",name)
vathmos = 0
#Edw jekinaei to Quiz
question1=input ("What is 10+10?")
if (question1 == "20"):
	vathmos=vathmos+1

question2=input ("What is 20-15")
if (question2=="5"):
	vathmos=vathmos+1	
	
question3=input ("What is 100-99")
if (question3=="1"):
	vathmos=vathmos+1

question4=input ("In which municipality it was vari old")
if (question4=="Anagyrountos"):
	vathmos=vathmos+1
	
question5=input ("What is called the newest software of windows")
if (question5=="windows 10"):
	vathmos=vathmos+1
	
question6=input ("Which is the capital city of Attica")
if (question6=="Athens"):
	vathmos=vathmos+1
	
question7=input ("Which is the second capital")
if (question7=="thessaloniki"):
	vathmos=vathmos+1
	
question8=input ("With which one food is known Greece")
if (question8=="Pork Gyros"):
	vathmos=vathmos+1
	
question9=input ("When greek television started")
if (question9=="1966"):
	vathmos=vathmos+1
	
print ("the last question is coming")

question10=input ("How it was called the first greek private TV station")
if (question10=="mega"):
	vathmos=vathmos+1

print("Your total score is",vathmos)