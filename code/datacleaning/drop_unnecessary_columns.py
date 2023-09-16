
#Function to drop specified columns from the dataset

def drop_unnecessary_columns(df, columns):
	'''
	Removes specified columns from a dataframe

	Parameters
	--------------------------
	df = a DataFrame object on which columns will be removed
	columns : a list of columns to be dropped

	Returns:
	pd.DataFrame object with columns removed or original 
	dataframe if the columns are not present.

	'''

	for column in columns:
		if column in df.columns:
			df.drop([column], axis = 1, inplace = True)
			print (f'Column {column} dropped.')
		else:
			print (f'Column {column} not present in df')