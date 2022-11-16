## READ IN CSV DATA
# to install pandas, type in terminal: python -m pip install pandas
# restart vscode, or use idle then you should be able to import/use pandas

import pandas as pd
 
# reading the CSV file
recipes = pd.read_csv("C:\\Users\waliang\Documents\\py_data\\recipes_82k.csv")
 
# displaying the contents of the CSV file
print(recipes)
