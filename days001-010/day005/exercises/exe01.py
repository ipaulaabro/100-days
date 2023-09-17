# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
size = 0
sum_heights = 0
for student_height in student_heights:
    size += 1
    sum_heights += student_height
average_height = round(sum_heights / size)
print(average_height)
