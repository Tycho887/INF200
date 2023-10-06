
["**" if i else " " for i in range(10)]

def list_of_exercises(project_assignment_start, total_number):
    exercises = [str(i) for i in range(1,project_assignment_start)]
    exercises += [str(i) + char for i in range(project_assignment_start, total_number + 1) for char in ["a", "b"]]
    return exercises

def list_of_exercises_2(project_assignment_start, total_number):
    exercises = [str(i) if i < project_assignment_start 
                 else (str(i) + char for char in ["a", "b"])
                 for i in range(1,total_number + 1)]
    return exercises

print(list_of_exercises_2(3, 4))