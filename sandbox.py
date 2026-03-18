
import numpy as np
import pandas as pd

grade = [12, 45, 7, 7, 31, 2, 50, 18, 9, 41, 23, 11, 36, 5, 44, 17, 28, 30, 14, 8, 19, 47, 3, 40, 6, 25, 10, 21, 33, 29]

hours =[3.47, 11.82, 6.15, 2.73, 9.64, 0.91, 10.38, 7.56, 4.29, 11.07,5.88, 8.13, 1.44, 6.92, 9.01, 3.76, 10.94, 2.58, 7.21, 4.83, 11.35, 0.66, 8.74, 6.37, 1.92, 9.48, 3.11, 7.89, 10.12, 5.27]

# create an array with numpy
grades = np.array(grade)
workingHours = np.array(hours)


student_data = np.array([hours,grade])

#print(grades)
#print(grades*2)

#take first element of arry
a = grades[0]

print(a)
print(student_data)

b = student_data[0][0]

print(b)

#calculate avarage study time
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()


print(f'Avarage Study Time: {avg_study}\n Avarage Grade: {avg_grade}')

df_students = pd.DataFrame({'study_hours': student_data[0], 'gardes': student_data[1]})

print(df_students)

c = df_students[df_students.study_hours==11.82]

print(c)

path = "C:\\Users\\Eugen Ewert\\OneDrive\\Eugen Ewert\\03_Studium\\FOM\\01_Semester_01\\04_AI Business Intelligence\\01_DataSets\\"
fileNmae = "student_data_100_rows_with_errors.csv"


df_real_students = pd.read_csv(path + fileNmae)

print(df_real_students)

