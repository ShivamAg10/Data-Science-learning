import pandas as pd 

'''
    # Filling Null Values
        df = df.fillna(value = <value>)
    
    # Filling Null values with previous values (row wise)
        df = df.fillna(method = "pad")
    
    # Filling Null values with next values (row wise)
        df = df.fillna(method = "bfil")
    
    # Filling Null values with previous values (column wise)
        df = df.fillna(method = "pad", axis = 1)
    
    # Filling Null values with next values (column wise)
        df = df.fillna(method = "bfil", axis = 1)
    
    # Filling Null values with different values in different columns
        df = df.fillna({"col1" : "val1", "col2" : "val2"})
    
    # Filling Null values with Mean, Mox or Min of a columns
        df = df.fillna(value = df['balcony'].mean())
'''