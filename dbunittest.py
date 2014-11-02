import unittest
import login
from pymongo import Connection


collectionName = "testdatabase"
dbname = "testdb"


class defaultTest(unittest.TestCase):
    """Class for default setUp and tearDown methods for testing"""
    def setUp(self, names=["1", "2", "3"], dbname="testdb"):
        self.dbname = dbname
        self.names = names
        self.conn = Connection()
        self.db = self.conn[dbname]
        self._createTestDatabase(names)

    def _createTestDatabase(self, names):
        """iter(names)
        creates collection testdatabase from the list of names"""
        for name in names:
            self.db.testdatabase.insert(self._jsonify(name, "password", False))

    def _jsonify(self, name, password, authenticated):
        """string name, string password, boolean authenticated

        returns a dictionary in the form of json
        to insert into a mongo collection"""
        user = {'name': name,
                'password': password,
                'authenticated': True}
        return user

    def tearDown(self):
        self.db.testdatabase.drop()


class testIsInDatabase(defaultTest):
    def test_not_in_database(self):
        self.assertEquals(login.isInDatabase("notInDatabaseName",
                                             self.dbname,
                                             "testdatabase"), False)

    def test_in_database(self):
        for name in self.names:
            self.assertEquals(login.isInDatabase(name,
                                                 self.dbname,
                                                 "testdatabase"), True)


class testAddUser(defaultTest):
    def test_name_already_in_database(self):
        """Should return false and not add it into the database"""
        login.addUser("testingname", "password", self.dbname, "testdatabase")
        self.assertEquals(login.addUser("testingname",
                                        "password",
                                        self.dbname,
                                        "testdatabase"), False)

    def test_add_name_success(self):
        """Should return True and add user into the database"""
        self.assertEquals(login.addUser("testingname4",
                                        "password2",
                                        self.dbname,
                                        "testdatabase"), True)
        self.assertEquals(login.isInDatabase("testingname4",
                                             self.dbname,
                                             "testdatabase",), True)


class testUpdateUser(defaultTest):
    pass


def main():
        suite = unittest.TestLoader().loadTestsFromTestCase(testIsInDatabase)
        unittest.TextTestRunner(verbosity=2).run(suite)
        suite = unittest.TestLoader().loadTestsFromTestCase(testAddUser)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()
