import pandas as pd

# UCI Cars data set - url location
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

# Column names from UCI repository documentation
column_names = [
	"symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors",
	"body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height",
	"curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore",
	"stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"
]

# Read data into pandas dataframe
df = pd.read_csv(data_url, header=None, names=column_names)

print(df.head()) # print 5 rows
# print(df) # print all rows
