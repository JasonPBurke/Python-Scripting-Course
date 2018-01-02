import dbm.dumb


print("Jason Burke\n")

# define the populateIt method
def run(keys, values, dbName):
    
    dumbDB = dbm.dumb.open(dbName, 'c')

    for cnt in range(len(keys)):
        dumbDB[keys[cnt]] = values[cnt]
    
    dumbDB.close()

