from os import name


id_student = 0
score_student = 0
name_student = ""
name_matter = ""
parameter = ""
student = [id_student , name_student , score_student]
list_student = []
line_student1 = [] #Separa nombre de curso
line_student2 = [] #Separa estudiantes y parametro
line_student3 = [] #Serpara y enlista a los estudiantes
matter = [name_matter , list_student]
print("PRACTICA 1 LFP")
print("Erick Daniel Ajche Hernadez")
print("201701043")
input()
print("Ingrese la direccion del archivo:")
direction_doc = input()
with open(direction_doc,'rt') as notes:
    text = notes.read()
    line_student1.append(text.split('= {'))
    name_matter = line_student1[0]
    line_student2.append(line_student1[1].split(" >} "))
    parameter = line_student2[1]
    line_student3.append(line_student2[0].split("> , <"))
    for n in line_student3:
        student_ = line_student3[n].split(";")
        for_name = []
        for_name.append(student_.split('"'))
        list_student.append(n+1, for_name[1], student_[1] )

    

        


