# Import required library

import pandas as pd

# Read data from CSV file

csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

# Print first five rows of the dataframe
print(df.head())
print('_________________________________________________________________________________')

# Access to the column Length
x = df[['Length']]
print(x)
print('_________________________________________________________________________________')

# Get the column as a series
x = df['Length']
print(x)
print('_________________________________________________________________________________')

# Get the column as a dataframe
x = type(df[['Artist']])
print(x)
print('_________________________________________________________________________________')

# Access to multiple columns
y = df[['Artist', 'Length', 'Genre']]
print(y)
print('_________________________________________________________________________________')

# Access the value on the first row and the first column
print(df.iloc[0, 0])
# Access the value on the second row and the first column
print(df.iloc[1,0])
# Access the value on the first row and the third column
print(df.iloc[0,2])
# Access the column using the name
print(df.loc[0, 'Artist'])
# Access the column using the name
print(df.loc[1, 'Artist'])
# Access the column using the name
print(df.loc[0, 'Released'])
# Access the column using the name
print(df.loc[1, 'Released'])
print('_________________________________________________________________________________')

# Slicing the dataframe
print(df.iloc[0:2, 0:3])
# Slicing the dataframe using name
print(df.loc[0:2, 'Artist':'Released'])
print('_________________________________________________________________________________')