import dbm.dumb


print("Jason Burke\n")

# define the populateIt method
def populateIt(keys, values, dbName):
    
    dumbDB = dbm.dumb.open(dbName, 'c')

    for cnt in range(len(keys)):
        dumbDB[keys[cnt]] = values[cnt]
    
    dumbDB.close()


# define the printIt method
def printIt(keys, values, dbName):
    
    dumbDB = dbm.dumb.open(dbName, 'r')# open the db for reading          
    
    for i, j in dumbDB.items():
        print('key: ' + str(i) , 'value: ' + str(j))

    dumbDB.close()
