# program to find average height of the students
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height=0
n=0
for height in student_heights:
	total_height+=height
	n+=1
average=total_height/n

print(round(average))