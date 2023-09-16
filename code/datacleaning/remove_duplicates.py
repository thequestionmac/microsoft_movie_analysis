def remove_duplicates(data):
    '''
    Checks for, displays and drops all duplicate values in the dataset
    '''
    number_of_duplicates = data.duplicated().sum()
    
    if number_of_duplicates > 0:
        print (f'This dataset has {number_of_duplicates} duplicated values')
        print ('Below is a sample of duplicates: ')
        print (data.iloc[df.duplicated()].sort_values(by = 'title').head(10))
        data.drop_duplicated(inplace = True)
        print ('Duplicate values removed')
    else:
        print ('No duplicate values')
