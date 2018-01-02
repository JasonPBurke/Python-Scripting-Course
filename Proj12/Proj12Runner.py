import dbm.dumb


print("Jason Burke\n")

# define the run method
def run(dbName):

    #Create keys and values
    keys = b'name',b'age',b'gender'
    values = b'Joe',b'39',b'male'

    dumbDB = dbm.dumb.open(dbName, 'c')#open/create db

    for cnt in range(len(keys)):
        dumbDB[keys[cnt]] = values[cnt]# populate db
    
    dumbDB.close()

