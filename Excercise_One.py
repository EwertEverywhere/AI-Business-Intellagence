
#import all libraries needed
import pandas as pd


#read csv file
def CsvReader(path,fileName):
    df = pd.read_csv(path + fileName)
    return df


# conut the elements



#


#main code
path = "C:\\Users\\Eugen Ewert\\OneDrive\\Eugen Ewert\\03_Studium\\FOM\\01_Semester_01\\04_AI Business Intelligence\\01_DataSets\\Learning_Panda\\"
fileName = "words.csv"

df = CsvReader(path,fileName)

# df.info() - Infomation about dataset
print(df.info())

# df.shape - alternative Information about dataset
print(df.shape)

# df.loc["value"] - index selection

df = df.loc["aahs"] 
print(df.head())