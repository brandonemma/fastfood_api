import unittest
from routes import orderList



class TestApi(unittest.TestCase):
    def test_get(self):
        orderLists = orderList()
        request = orderLists.get()

if __name__=="__main__":
    unittest.main()

