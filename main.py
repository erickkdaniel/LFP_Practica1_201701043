from os import name, pardir
import os
line_student1 = [] #Separa nombre de curso
line_student2 = [] #Separa estudiantes y parametro
line_student3 = [] #Serpara y enlista a los estudiantes
id_m = 0
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
        self.firstlist = []
    def NewStudent(self, Student):
        self.list_student.append(Student)
        self.firstlist.append(Student)
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
    def getFirstList(self):
        return self.firstlist
def Cover():
    print("PRACTICA 1 LFP")
    print("Erick Daniel Ajche Hernadez")
    print("201701043")
    input()
    clearConsole()
    MenuPrincipal2()
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
    clearConsole()
    print("Ingrese el nombre del archivo:")
    dx1 = input()
    dx = dx1+".lfp"
    doc = open(dx)
    text = doc.read()
    line_student1 = text.split("=")#Nombre curso
    name_matter = str(line_student1[0])
    line_student12 =  line_student1[1].split("{")
    line_student2 = line_student12[1].split("}")#Parametro
    parameters = line_student2[1].replace(" ","")
    listParameters = parameters.split(",")
    line_student3 = line_student2[0].split(",")#Estudiantes
    id_matter = IdCount()
    Matter_ = Matter(id_matter, name_matter, listParameters)
    id = 0
    for n in line_student3:
        line1 = n.split("<")
        line2 = line1[1].split(">")
        for_score = []
        for_score = line2[0].split(";")#Separa Estudiantes
        for_name = []
        for_name = for_score[0].split('"')
        for_score[1] = for_score[1].replace(" ","")
        if for_score[1].isnumeric():
            if int(for_score[1])>0 :
                id=id+1
                new_student= Student(id, int(for_score[1]),for_name[1])
                Matter_.NewStudent(new_student)
        else:
            print("Error del alumnos: "+for_name[1])
    Matter_.setTotalS(id)
    global firstliststu
    firstliststu = Matter_.getFirstList()
    input()
    clearConsole()
    impParameter(name_matter)
    clearConsole()
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
        clearConsole()
        AnalysisText()
    elif option == "2":
        clearConsole()
        printReport(Matter)
    elif option == "3":
        clearConsole()
        exportReport(Matter)
    elif option == "4":
        clearConsole()
        exit()
    else:
        MenuPrincipal(Matter)
def printReport(Matter):
    listPara = Matter.getParameter()
    m = Matter.getnameMatter()
    t = Matter.getTotalS()
    ListStudent = Matter.getFirstList()
    print("Nombre del Curso: "+m)
    print("Numero de alumnos: "+str(t))
    print("==========================================================")
    print("Lista de Estudiantes")
    print("==========================================================")
    for i in ListStudent:
        print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    for i in listPara:
        Action_Parameter(Matter, str(i))
    input()
    clearConsole()
    MenuPrincipal(Matter)
def exportReport(Matter):
    ListStudent = Matter.getFirstList()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path+"\\"+Matter.getnameMatter()+".html", "w")
    file.write('<!DOCTYPE html><html><head><link rel="stylesheet" href="style.css"></head><body>')
    listPara = Matter.getParameter()
    m = Matter.getnameMatter().strip()
    t = Matter.getTotalS()
    file.write("<h1>Curso de "+m+".</h1>")
    file.write("<h3>Con un total de "+str(t)+" alumnos.</h3>")
    file.write("<h3>Lista Estudiantes</h3>")
    file.write('<table class="styled-table"><thead><tr><td>ID</td><td>Nombre</td><td>Nota</td></tr></thead>')
    file.write("<tbody>")
    for i in ListStudent:
        if int(i.getScore())<61:
            file.write('<tr><td>'+str(i.getID())+"</td><td>"+i.getName()+'</td><td><B><FONT COLOR="red">'+str(i.getScore())+'</FONT><br></td></tr>')
        else:
            file.write('<tr><td>'+str(i.getID())+"</td><td>"+i.getName()+'</td><td><B><FONT COLOR="blue">'+str(i.getScore())+'</FONT><br></td></tr>')
    file.write("</tbody></table>")
    for i in listPara:
        Action_Parameter_html(Matter, str(i), file)
    file.close()
    MenuPrincipal(Matter)
def Action_Parameter_html(MatterPar, P, file):
    Par = P
    m = MatterPar.getnameMatter().strip()
    t = MatterPar.getTotalS()
    List_stu = MatterPar.getList()
    if Par == "ASC":
        ListAsc = OrdenamientoAsc(List_stu)
        file.write("<h3>Lista Ascendente</h3>")
        file.write('<table class="styled-table"><thead><tr><td>ID</td><td>Nombre</td><td>Nota</td></tr></thead>')
        file.write("<tbody>")
        for i in ListAsc:
            if int(i.getScore())<61:
                file.write('<tr><td>'+str(i.getID())+"</td><td>"+i.getName()+'</td><td><B><FONT COLOR="red">'+str(i.getScore())+'</FONT><br></td></tr>')
            else:
                file.write('<tr><td>'+str(i.getID())+"</td><td>"+i.getName()+'</td><td><B><FONT COLOR="blue">'+str(i.getScore())+'</FONT><br></td></tr>')
        file.write("</tbody></table>")
    elif Par == "DESC":
        ListDesc = OrdenamientoDes(List_stu)
        file.write("<h3>Lista Desscendente</h3>")
        file.write('<table class="styled-table"><thead><tr><td>ID</td><td>Nombre</td><td>Nota</td></tr></thead>')
        file.write("<tbody>")
        for i in ListDesc:
            if int(i.getScore())<61:
                file.write('<tr><td>'+str(i.getID())+"</td><td>"+i.getName()+'</td><td><B><FONT COLOR="red">'+str(i.getScore())+'</FONT><br></td></tr>')
            else:
                file.write('<tr><td>'+str(i.getID())+"</td><td>"+i.getName()+'</td><td><B><FONT COLOR="blue">'+str(i.getScore())+'</FONT><br></td></tr>')
        file.write("</tbody></table>")
    elif Par == "AVG":
        Prome = prom(List_stu)
        file.write("<h3>Promedio: "+str(Prome)+"</h3>")
    elif Par == "MIN":
        student_min = minScore(List_stu)
        file.write("<h3>El estudiante con la menor nota fue "+student_min.getName()+" con una nota de "+str(student_min.getScore())+"</h3>")
    elif Par == "MAX":
        student_max = maxScore(List_stu)
        file.write("<h3>El estudiante con la mayor nota fue "+student_max.getName()+" con una nota de "+str(student_max.getScore())+"</h3>")
    elif Par == "APR":
        file.write("<h3>Lista de Aprobados</h3>")
        file.write('<table class="styled-table"><thead><tr><td>ID</td><td>Nombre</td><td>Nota</td></tr></thead>')
        file.write("<tbody>")
        ListAprov = aprovedScore(List_stu)
        for i in ListAprov:
            file.write('<tr><td>'+str(i.getID())+"</td><td>"+i.getName()+'</td><td><B><FONT COLOR="blue">'+str(i.getScore())+'</FONT><br></td></tr>')
        file.write("</tbody></table>")
    elif Par == "REP":
        file.write("<h3>Lista de Reprobados</h3>")
        file.write('<table class="styled-table"><thead><tr><td>ID</td><td>Nombre</td><td>Nota</td></tr></thead>')
        file.write("<tbody>")
        ListRepro = reprobateScore(List_stu)
        for i in ListRepro:
            file.write('<tr><td>'+str(i.getID())+"</td><td>"+i.getName()+'</td><td><B><FONT COLOR="red">'+str(i.getScore())+'</FONT><br></td></tr>')
        file.write("</tbody></table>")
    else:
        file.write("<h3>El parametro no fue detectado "+Par+"</h3>")
def Action_Parameter(MatterPar, P):
    Par = P
    m = MatterPar.getnameMatter()
    t = MatterPar.getTotalS()
    List_stu = MatterPar.getList()
    if Par == "ASC":
        ListAsc = OrdenamientoAsc(List_stu)
        print("==========================================================")
        print("Lista Ascendente")
        print("==========================================================")
        for i in ListAsc:
            print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    elif Par == "DESC":
        OrdenamientoDes(List_stu)
        ListDesc = OrdenamientoDes(List_stu)
        print("==========================================================")
        print("Lista Ascendente")
        print("==========================================================")
        for i in ListDesc:
            print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    elif Par == "AVG":
        Prome = prom(List_stu)
        print("==========================================================")
        print("El promedio del Salon es de "+str(Prome))
    elif Par == "MIN":
        student_min = minScore(List_stu)
        print("==========================================================")
        print("El estudiante con la menor nota fue "+student_min.getName()+" con una nota de "+str(student_min.getScore()))
    elif Par == "MAX":
        student_max = maxScore(List_stu)
        print("==========================================================")
        print("El estudiante con la menor nota fue "+student_max.getName()+" con una nota de "+str(student_max.getScore()))
    elif Par == "APR":
        ListAprov = aprovedScore(List_stu)
        print("==========================================================")
        print("Lista de Aprobados")
        print("==========================================================")
        for i in ListAprov:
            print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    elif Par == "REP":
        ListRepro = reprobateScore(List_stu)
        print("==========================================================")
        print("Lista de Reprobados")
        print("==========================================================")
        for i in ListRepro:
            print("ID: "+str(i.getID())+" Nombre: "+i.getName()+" Nota: "+str(i.getScore()))
    else:
        print("==========================================================")
        print("El parametro no fue detectado "+Par)
def IdCount():
    global id_m    
    id_m = id_m + 1
    return id_m
def OrdenamientoAsc(m):
    MatterList = m
    for N1 in range(len(MatterList)-1,0,-1):
        for i in range(N1):
            if MatterList[i].getScore()>MatterList[i+1].getScore():
                Temp = MatterList[i]
                MatterList[i] = MatterList[i+1]
                MatterList[i+1] = Temp
    return MatterList
def OrdenamientoDes(m):
    MatterList = m
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
    prome = Sum/Cont
    prom = round(prome,2)
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
Cover()#C:\Users\danie\Desktop\Ejemplo