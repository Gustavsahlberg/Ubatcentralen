import unittest
from Funktioner.Movement.load_reports import loadReports
from pathlib import Path





class Testing(unittest.TestCase):

    def setUp(self):
        self.folder = Path("test_files")
        self.folder.mkdir(exist_ok=True)
        crash = False
        for x in range(5):
            file = self.folder / f"movement_test_{x}.txt"
            if not file.exists():
                if crash:
                    file.write_text(f"forward {7+x}\nup {9+x}\n", encoding="utf-8")
                else:
                    file.write_text(f"forward {11}\nup {11}\n", encoding="utf-8")
                    crash = True

            
        self.load = loadReports(self.folder)

    def test_files(self):


        self.load.read_files()
        pos = self.load.pos
        
        self.assertEqual(pos["movement_test_1.txt"],[10,8])
        self.assertEqual(pos["movement_test_4.txt"],[13,11])

    def test_name(self):
        file_names = self.load.get_sub_sn()
        self.assertEqual("movement_test_1.txt",file_names[1])

    def test_crash_log(self): #Testar decarator
        self.load.read_files()
        log = self.load.get_crash_log()
        self.assertIn(log["movement_test_0.txt"][0],[{"timestamp": 1, "xy": (0, 11)}])
        self.assertIn(log["movement_test_4.txt"][0],[{"timestamp": 1, "xy": (0, 11)}])


    def test_get_loc(self):
        self.load.read_files()
        horizontal, vertical, log = self.load.get_loc()
        self.assertEqual(horizontal[11],[11, 13])
        self.assertEqual(vertical[10],[8])




if __name__ == "__main__":
    unittest.main()