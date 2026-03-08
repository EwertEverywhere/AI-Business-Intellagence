
import pandas as pd
import matplotlib.pyplot as plt
import cv2


#read file
class FileReader:
    
    
    # Read csv
    def readCSV(self,path,fileName):
        df = pd.read_csv(path + fileName)
        return df 

    #Read Excel
    def readExcel(self,path,fileName):
        df = pd.read_csv(path + fileName)
        return df 




#main code
pfad = "C:\\Users\\Eugen Ewert\\OneDrive\\Eugen Ewert\\03_Studium\\FOM\\01_Semester_01\\04_AI Business Intelligence\\01_DataSets\\"
fileName ="data_five.csv"

reader = FileReader()
df = reader.readCSV(pfad,fileName)

df = df["X2"]
#Face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print(df.head())




#"C:\Users\Eugen Ewert\OneDrive\Eugen Ewert\03_Studium\FOM\01_Semester_01\04_AI Business Intelligence\01_DataSets\data_five.csv"

