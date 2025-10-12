import pandas as pd
file_path = 'data/iris_data.csv'

# import data
data = pd.read_csv(file_path)

# print a few rows
print(data.iloc[:5])

# different delimiter - tab separated file (.tsv)
data = pd.read_csv(file_path, sep='\t')

# different delimiter - space separated file
data = pd.read_csv(file_path, delim_whitespace=True)

# don't use first row for column names
data = pd.read_csv(file_path, header=None)

# specify column names
data = pd.read_csv(file_path, names=['name1', 'name2', 'name3', 'name4', 'name5'])

# custom missing value representation
data = pd.read_csv(file_path, na_values=['NA', '99'])