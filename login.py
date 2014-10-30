"""Module used for dealing with database stuff"""
from pymongo import Connection


def addUser(dbname="users", name="", password=""):
    """Takes string dbname, string name, string password

    adds user to the database and returns False is username already exists

    automatically logs the user in after creating the account"""
    success = True

    conn = Connection()
    db = conn[dbname]

    if (isInDatabase(dbname, name)):
        # Jsonifies the User, authenticated True means the user is logged in
        user = {'name': name,
                'password': password,
                'authenticated': True}
        db.people.insert(user)
    else:
        success = False

    return success


def isInDatabase(dbname="users", name=""):
    """takes string dbname, string name
    checks if user is already in the database and returns False if username
    already exists"""
    conn = Connection()
    db = conn[dbname]

    # returns collection of users
    people = db.people

    # there should be at most one instance of the user in the database
    success = (people.find({'name': name}).count() == 1)

    return success


def main():
    pass

if __name__ == '__main__':
    main()
