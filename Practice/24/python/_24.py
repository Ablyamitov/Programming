import json
with open('in.json', 'r') as file:
	inin = json.load(file)
outout=[]
all_userId=[]
size_inin = len(inin)
for i in range (size_inin):
	all_userId.append(inin[i]["userId"])
max_userId=max(all_userId)
for different_id in range (1,max_userId+1):
	completed_work=0
	for allwork in range (size_inin):
		if (inin[allwork]["userId"] == different_id and inin[allwork]["completed"] ):
			completed_work+=1
	if(completed_work>0):
				outout.append(
					{"task_completed":completed_work,
					"userId":different_id},
				)
with open("out.json","w") as file2:
	json.dump(outout,file2,indent = 4)
	  


