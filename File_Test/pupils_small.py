import time 
time_start = time.time()
pupils = list()

class Pupils():
    def __init__(self,data):
        data = data.split(" ")
        self.surname = data[0]
        self.name = data[1]
        self.mark = int(data[2])
with open("pupils.txt", "r", encoding= "utf-8") as file:
    for line in file.readlines():
        pupils.append(Pupils(line))
    
print("Відмінники:")
average = 0
for pupil in pupils:
    average += pupil.mark
    if pupil == 5:
        print(pupil.surname)
print("Середнє арифметичне:", average // len(pupils))
time_end = time.time()
print("Витрачено часу", time_end - time_start)