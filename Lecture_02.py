
import pandas as pd
import matplotlib.pyplot as plt

def printDataFormTable():
    path = "C:\\Users\\Eugen Ewert\\OneDrive\\Eugen Ewert\\03_Studium\\FOM\\01_Semester_01\\04_AI Business Intelligence\\01_DataSets\\"
    fileName = "Titanic-Dataset.csv"

    df = pd.read_csv(path + fileName)
    return df
    
# Zeile
# einestieg in Data Science mit python
#Grundlagen für verarbeitung, Analyse und Interpretation der Datenmänge
# Tools und mehtoden
# DS als Process verstehen.

#80% - des Aufwandes
#Datenerfassung
#Datenverarbeitung

#20% - des Aufwandes
#Datenanalyse
#Datenvisualisierung

# Verschiedene Technologien und Mehtoden (Statistik, ML)
# Identifikation von Mustern und Trens
# Hilfreich für Eentscheidungsfindungen.

# Statistik Literacy ist eine Voraussetzuung für KI Kompetenz.



print ('hello world')

print(printDataFormTable().head())

# Grundlagen der datenstrukturen




def datenstrukturen():
    #lists[]
    list = [1,2,3]

    
    
    # stes{} - ungeordnete einzigartige elemnete
    # array[] - elemente desselben typs, sind operabel
    # dataFrame{} - tabellarische datenstruktur
    # stack[] - liniare datenstrukturen 


    return list


df = printDataFormTable()

print(df.head())

object = df.Pclass[1:5]

print(object)

new_Object = object*2

print(new_Object)


#typel

new_tupel = (1,2,3,"female","male")

print(new_tupel)

# ein tupel multipliziert mal zei wir alle elemente des tupels wiederholen also anzahl der elemenen.
print(new_tupel*2)


#stacks



new_stack = [1,2,3]
print(new_stack)

new_stack.append(4)
print(new_stack)

#new_new_stack = new_stack.pop
 
#print(new_new_stack)


