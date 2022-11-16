# import csv
 
# # opening the CSV file
# with open('C:\Users\waliang\Documents\py_data\recipes_82k.csv', mode ='r')as file:
   
#   # reading the CSV file
#   csvFile = csv.reader(file)
 
#   # displaying the contents of the CSV file
#   for lines in csvFile:
#         print(lines)

import pandas as pd
 
# reading the CSV file
csvFile = pd.read_csv("C:\\Users\waliang\Documents\\py_data\\recipes_82k.csv")
 
# displaying the contents of the CSV file
print(csvFile)
