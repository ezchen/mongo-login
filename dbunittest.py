import unittest
import login
from pymongo import Connection


class testIsInDatabase(unittest.TestCase):
    def setUp(self, names=["1", "2", "3"], dbname="testdb"):
        self.dbname = dbname
        self.names = names
        self.conn = Connection()
        self.db = self.conn[dbname]
        self._createTestDatabase(names)

    def _createTestDatabase(self, names):
        """Set of names
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

    def test_not_in_database(self):
        self.assertEquals(login.isInDatabase("notInDatabaseName",
                                             self.dbname,
                                             "testdatabase"), False)

    def test_in_database(self):
        for name in self.names:
            self.assertEquals(login.isInDatabase(name,
                                                 self.dbname,
                                                 "testdatabase"), True)

    def tearDown(self):
        self.db.testdatabase.drop()


class testAddUser(unittest.TestCase):
    def setUp(self, names=["1", "2", "3"], dbname="testdb"):
        self.dbname = dbname


def main():
        suite = unittest.TestLoader().loadTestsFromTestCase(testIsInDatabase)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
