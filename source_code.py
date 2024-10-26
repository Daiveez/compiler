seed = 12345  
a = 1103515245
c = 12345  
m = 2**31 
min_distance_per_step = 0.6
max_distance_per_step = 1.5
total_distance = 1000
number_of_students = 90  
distance_per_step = 0
total_steps_per_student = 0
total_steps = 0
count = 0
while count < number_of_students:
    seed = (a * seed + c) % m  
    distance_per_step = min_distance_per_step + (seed % (max_distance_per_step - min_distance_per_step + 1))
    total_steps_per_student = total_distance / distance_per_step 
    total_steps = total_steps + total_steps_per_student
    count = count + 1
average_steps = total_steps/ number_of_students
print("The average number of steps required for any student to complete the walk from CIT in SAT to the university stadium is: ")
print(average_steps)