from os import name, pardir
import os


    

class Student:
    def __init__(self, ID, Score, Name):
           
        self.id_student = ID
        self.score_student = Score
        self.name_student = Name
    def getScore(self):
        return self.score_student
    def getName(self):
        return self.name_student
    def getID(self):
        return self.id_student


class Matter:
    def __init__(self,ID_Matter ,name_Matter,parameter_Metter):
        self.list_student = []
        self.name_matter = name_Matter
        self.id_matter =  ID_Matter
        self.parameter = parameter_Metter
        self.tStudent = 0

    def NewStudent(self, Student):
        self.list_student.append(Student)
    def getStudent(self, ID):
        for i in self.list_student:
            if i.getID() == ID:
                return i
    def getList(self):
        return self.list_student
    
    def getParameter(self):
            return self.parameter
    
    def setTotalS(self, t):
        self.tStudent = t
    def getTotalS(self):
        return self.tStudent

    def getnameMatter(self):
        return self.name_matter
 

def Cover():
    print("PRACTICA 1 LFP")
    print("Erick Daniel Ajche Hernadez")
    print("201701043")
    input()
    clearConsole()
    MenuPrincipal2()
    
line_student1 = [] #Separa nombre de curso
line_student2 = [] #Separa estudiantes y parametro
line_student3 = [] #Serpara y enlista a los estudiantes

def MenuPrincipal2(): 
    print("Menu Principal")
    print("1. Agregar nueva lista")
    print("2. Mostrar reporte")
    print("3. Exportar reporte")
    print("4. Salir")
    print("Ingrese el numero de la opcion de su interes")
    option = input()
    if option == "1":
        AnalysisText()
    elif option == "4":
        exit()
    else:
        print("No puede ver ningun reporte sin haber agregado una lista antes")
        input()
        clearConsole()
        MenuPrincipal2()
    


def AnalysisText():
    print("Ingrese la direccion del archivo:")
    dx = input()
    text = """Matematicas = { <"Daniel" ; 70 > , <"Erick";78 > , <"Jorge" ; 71 > , <"Juanse" ; 58 > , <"Cocu" ; 60 > , <"Cold" ; 61 > } ASC,DESC,MIN"""
    line_student1 = text.split("=")#Nombre curso
    name_matter = str(line_student1[0])
    print(name_matter)
    line_student12 =  line_student1[1].split("{")
    line_student2 = line_student12[1].split("}")#Parametro
    parameters = line_student2[1].replace(" ","")
    listParameters = parameters.split(",")
    line_student3 = line_student2[0].split(",")#Estudiantes
    id_matter = IdCount()
    Matter_ = Matter(id_matter, name_matter, listParameters)
    id = 0
    for n in line_student3:
        id=id+1
        line1 = n.split("<")
        line2 = line1[1].split(">")
        for_score = []
        for_score = line2[0].split(";")#Separa Estudiantes
        for_name = []
        for_name = for_score[0].split('"')
        new_student= Student(id, for_score[1],for_name[1])
        Matter_.NewStudent(new_student)
    Matter_.setTotalS(id)
    impParameter(name_matter)
    MenuPrincipal(Matter_)



def MenuPrincipal(Matter):
    print("Menu Principal")
    print("1. Agregar nueva lista")
    print("2. Mostrar reporte")
    print("3. Exportar reporte")
    print("4. Salir")
    print("Ingrese el numero de la opcion de su interes")
    option = input()
    if option == "1":
        AnalysisText()
    elif option == "2":
        printReport(Matter)
    elif option == "3":
        exportReport(Matter)
        return
    elif option == "4":
        exit()
    else:
        MenuPrincipal(Matter)
    return

def printReport(Matter):
    listPara = Matter.getParameter()
    for i in listPara:
        Action_Parameter(Matter, str(i))
    input()
    MenuPrincipal(Matter)



def exportReport(Matter):
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    file = open(dir_path+"\\reporte.html", "w")
    file.write('<!DOCTYPE html><html><head><link rel="stylesheet" href="style.css"></head><body>')
    listPara = Matter.getParameter()
    for i in listPara:
        Action_Parameter_html(Matter, str(i), file)

    file.close()

def Action_Parameter_html(MatterPar, P, file):
    Par = P
    m = MatterPar.getnameMatter().strip()
    t = MatterPar.getTotalS()
    List_stu = MatterPar.getList()
    if Par == "ASC":
        ListAsc = OrdenamientoAsc(List_stu)
        file.write("<h1>Curso de "+m+".</h1>")
        file.write("<h3> con un total de "+str(t)+" alumnos.</h3>")
        file.write('<table class="styled-table"><thead><tr><td>ID</td><td>Nombre</td><td>Nota</td></tr></thead>')
        file.write("<tbody>")
        for i in ListAsc:
            file.write("<tr><td>"+str(i.getID())+"</td><td>"+i.getName()+"</td><td>"+str(i.getScore())+"</td></tr>")
        file.write("</tbody></table>")
    elif Par == "DESC":
        OrdenamientoDes(List_stu)
        ListDesc = OrdenamientoDes(List_stu)
        file.write("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.\n")
        for i in ListDesc:
            file.write("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    elif Par == "AVG":
        Prome = prom(List_stu)
        file.write("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.\n")
        file.write("==========================================================\n")
        file.write("El promedio del Salon es de "+str(Prome))
    elif Par == "MIN":
        student_min = minScore(List_stu)
        file.write("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.\n")
        file.write("==========================================================\n")
        file.write("El estudiante con la menor nota fue "+student_min.getName()+" con una nota de "+str(student_min.getScore()))
    elif Par == "MAX":
        student_max = maxScore(List_stu)
        file.write("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.\n")
        file.write("==========================================================\n")
        file.write("El estudiante con la menor nota fue "+student_max.getName()+" con una nota de "+str(student_max.getScore()))
    elif Par == "APR":
        ListAprov = aprovedScore(List_stu)
        file.write("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.\n")
        file.write("==========================================================\n")
        file.write("Lista de Aprobados:")
        for i in ListAprov:
            file.write("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    elif Par == "REP":
        ListRepro = reprobateScore(List_stu)
        file.write("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.\n")
        file.write("==========================================================\n")
        file.write("Lista de Reprobados:\n")
        for i in ListRepro:
            file.write("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    else:
        file.write("El parametro no fue detectado\n")
    

    


def Action_Parameter(MatterPar, P):
    Par = P
    m = MatterPar.getnameMatter()
    t = MatterPar.getTotalS()
    List_stu = MatterPar.getList()
    if Par == "ASC":
        ListAsc = OrdenamientoAsc(List_stu)
        print("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.")
        print("==========================================================")
        for i in ListAsc:
            print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    elif Par == "DESC":
        OrdenamientoDes(List_stu)
        ListDesc = OrdenamientoDes(List_stu)
        print("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.")
        print("==========================================================")
        for i in ListDesc:
            print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    elif Par == "AVG":
        Prome = prom(List_stu)
        print("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.")
        print("==========================================================")
        print("El promedio del Salon es de "+str(Prome))
    elif Par == "MIN":
        student_min = minScore(List_stu)
        print("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.")
        print("==========================================================")
        print("El estudiante con la menor nota fue "+student_min.getName()+" con una nota de "+str(student_min.getScore()))
    elif Par == "MAX":
        student_max = maxScore(List_stu)
        print("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.")
        print("==========================================================")
        print("El estudiante con la menor nota fue "+student_max.getName()+" con una nota de "+str(student_max.getScore()))
    elif Par == "APR":
        ListAprov = aprovedScore(List_stu)
        print("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.")
        print("==========================================================")
        print("Lista de Aprobados:")
        for i in ListAprov:
            print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    elif Par == "REP":
        ListRepro = reprobateScore(List_stu)
        print("Curso de "+m+"."+" con un total de "+str(t)+" alumnos.")
        print("==========================================================")
        print("Lista de Reprobados:")
        for i in ListRepro:
            print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    else:
        print("El parametro no fue detectado")
id_m = 0
def IdCount():
    global id_m    
    id_m = id_m + 1
    return id_m

def OrdenamientoAsc(MatterList):
    for N1 in range(len(MatterList)-1,0,-1):
        for i in range(N1):
            if MatterList[i].getScore()>MatterList[i+1].getScore():
                Temp = MatterList[i]
                MatterList[i] = MatterList[i+1]
                MatterList[i+1] = Temp
    return MatterList

def OrdenamientoDes(MatterList):
    for N1 in range(len(MatterList)-1,0,-1):
        for i in range(N1):
            if MatterList[i].getScore()<MatterList[i+1].getScore():
                Temp = MatterList[i]
                MatterList[i] = MatterList[i+1]
                MatterList[i+1] = Temp
    return MatterList
    
def Sumatoria(MatterList):
    Sum = 0
    for N1 in range(len(MatterList)-1,0,1):
        for i in range(N1):
             Sum = Sum + MatterList[i]
        Prom = Sum/i
        return Prom

def prom(MatterList):
    Sum = 0
    Cont = 0
    for N1 in MatterList:
        Cont = Cont + 1
        Sum = Sum + int(N1.getScore())
    prom = Sum/Cont
    return str(prom)

def minScore(MatterList):
    for N1 in range(len(MatterList)-1,0,-1):
        for i in range(N1):
            if MatterList[i].getScore()>MatterList[i+1].getScore():
                Temp = MatterList[i]
                MatterList[i] = MatterList[i+1]
                MatterList[i+1] = Temp
    return MatterList[0]
    
def maxScore(MatterList):
    for N1 in range(len(MatterList)-1,0,-1):
        for i in range(N1):
            if MatterList[i].getScore()<MatterList[i+1].getScore():
                Temp = MatterList[i]
                MatterList[i] = MatterList[i+1]
                MatterList[i+1] = Temp
    return MatterList[0]

def aprovedScore(MatterList):
    aprovedList = []
    for i in MatterList:
        if int(i.getScore())>=61:
            aprovedList.append(i)
    return aprovedList
def reprobateScore(MatterList):
    reprobateList = []
    for i in MatterList:
        if int(i.getScore())<61:
            reprobateList.append(i)
    return reprobateList
def impParameter(m):
    print("Agragada nueva lista del curso "+m)
    input()

def cuesPara(p):
    if p == "ASC":
        par = "Lista Ascendente"
        return par
    elif p == "DESC":
        par = "Lista Descendente"
        return par 
    elif p == "AVG":
        par = "Promedio de notas"
        return par 
    elif p == "MIN":
       par = "Nota minima"
       return par 
    elif p == "MAX":
        par = "Nota maxima"
        return par 
    elif p == "APR":
        par = "Lista de Aprobados"
        return par 
    elif p == "REP":
       par = "Lista de Reprobados"
       return par 
    else:
        print("El parametro no fue detectado")
    
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()
Cover()
    

    

        


