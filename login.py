"""Module used for dealing with database stuff"""
from pymongo import Connection


def login(name, dbname="users", dbCollectionName="people"):
    """sets authenticated to True for a given user"""
    updateUser(name, True, dbname, dbCollectionName)


def logout(name, dbname="users", dbCollectionName="people"):
    """sets authenticated to False for a given user"""
    updateUser(name, False, dbname, dbCollectionName)


def updateUser(name, authenticated, dbname="users", dbCollectionName="people"):
    """string name, Boolean authenticated, string dbname, string dbCollectioName
Logs the user in if authenticated is True
Logs the user out if authenticated is False

Returns True if successful or False if not successful"""
    success = True

    if (isInDatabase(name, dbname, dbCollectionName)):
        # update methods I don't know how to do...
        pass
    else:
        success = False

    return success


def addUser(name, password, dbname="users", dbCollectionName="people"):
    """string name, string password, string dbname, string dbCollectionName
adds user to the database and returns False is username already exists

automatically logs the user in after creating the account"""
    success = True

    conn = Connection()
    db = conn[dbname]

    if (not isInDatabase(name, dbname, dbCollectionName)):
        # Jsonifies the User, authenticated True means the user is logged in
        user = {'name': name,
                'password': password,
                'authenticated': True}
        people = db[dbCollectionName]
        people.insert(user)
    else:
        success = False

    return success


def isInDatabase(name, dbname="users", dbCollectionName="people"):
    """takes string name, string dbname, string dbCollectionName
checks if user is already in the database and returns False if username
already exists"""
    conn = Connection()
    db = conn[dbname]

    # returns collection of users
    people = db[dbCollectionName]

    # there should be at most one instance of the user in the database
    success = (people.find({'name': name}).count() >= 1)

    return success


def main():
    pass

if __name__ == '__main__':
    main()
