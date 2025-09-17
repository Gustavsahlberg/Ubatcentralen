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


    def test_min_max(self):
        min_max_list = self.g.min_max()

        self.assertEqual(min_max_list[0][0],"movement_test_4.txt") #max_up
        self.assertEqual(min_max_list[1][0],"movement_test_1.txt") #min_up
        self.assertEqual(min_max_list[2][0],"movement_test_0.txt") #max_forward
        self.assertEqual(min_max_list[3][0],"movement_test_1.txt") #min_forward