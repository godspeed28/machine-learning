import pandas as pd
file_path = 'data/iris_data.json'

# read json files as dataframes
data = pd.read_json(file_path)

# write dataframe to json file
data.to_json('data/outputfile.json')
