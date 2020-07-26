
# to create mcq quiz and give finalscore 

#question in dic or list

question = {"which of the following condition will cause infinite loop" : {"correct" :"b" ,
			 "answers" : ["while(5>=6):","while(True):","while(False):","while(1 == 6):"]},
			"what is the output print int('56.75')" : {"correct" :"b" ,
			 "answers" : ["567","Error","56.75","56.0"]},
			 "what is the output print(print(5))" : {"correct" :"d" ,
			 "answers" : ["5","Error","None 5","5 None"]}
}

#answer 
anslabel = ['a','b','c','d']

#use correct var to count
correct = 0

#total
total = len(question)

input(" Press Enter To Start ")

for k,v in question.items():
	print(k)


	x = 0
	for ans in v["answers"]:
            
		print(anslabel[x] + " " + str(ans))
		
		x=x+1
	answer = input("\n Type any option a,b,c,d  \n")


# now cal total number of correct answer 
	if (answer == v["correct"]):
		correct +=1
		print("answer is correct ")
	else:
		print("answer is wrong")


		print("\n") 

	#print(correct)
##
score =((correct / total) *100 ) 

#+ "%"
#s = round(score,2)
#print(s)
#print("Final Score  is : ",s,"%")
 
print("score final %.2f"%(score),"%")



