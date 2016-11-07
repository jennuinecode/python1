from random import randint

print "Scores and Grades"
for count in range(0, 10):
	score = randint(70, 100)

	if(score <= 70):
		grade = "D"
	elif(score <= 80):
		grade = "C"
	elif(score <= 90):
		grade = "B"
	else:
		grade = "A"

	print "Score: {}; Your grade is {}".format(score, grade)

print "End of program. Byyeeee!"
