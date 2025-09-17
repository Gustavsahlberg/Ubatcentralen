import unittest
from Funktioner.get_files import gather




class Testing(unittest.TestCase):

    def setUp(self):

        self.g = gather("test_files")

    
    def test_crash_log(self):
        log = (self.g.get_log("movement_test_0.txt"))
        self.assertEqual(log[0],{'timestamp': 1, 'xy': (0, 11)})



    def test_get_clerance(self):
        up, down ,forward = self.g.get_clerance("movement_test_0.txt")
        self.assertIs(up,False)
        self.assertIs(down, True)
        self.assertIs(forward,True)