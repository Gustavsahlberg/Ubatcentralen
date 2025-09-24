import unittest
from pathlib import Path
from Funktioner.sensor_analysis import SensorFileAnalyzer
import logging

class TestSensorFileAnalyzer(unittest.TestCase):

    def setUp(self):
        
        self.test_dir = Path(__file__).parent
        self.test_files = list(self.test_dir.glob("*.txt"))


    def test_analyze_and_summary(self):
        for file_path in self.test_files:
            analyzer = SensorFileAnalyzer(file_path)
            analyzer.analyze()
            summary = analyzer.summary()

            
            self.assertEqual(summary["submarine_id"], file_path.stem)

            
            self.assertGreater(summary["total_rows"], 0, f"{file_path.stem} har inga rader")

            
            avg = summary["avg_failures_per_row"]
            self.assertGreaterEqual(avg, 0)
            self.assertLessEqual(avg, 208)

            
            unique = summary["unique_patterns"]
            self.assertGreaterEqual(unique, 1)
            self.assertLessEqual(unique, summary["total_rows"])

           
            pattern, count = summary["most_common_pattern"]
            self.assertIsInstance(pattern, str)
            self.assertIsInstance(count, int)
            self.assertGreaterEqual(count, 1)

    def test_invalid_lines_logged(self):
        """Testa att ogiltiga rader loggas korrekt."""
        
        invalid_file = self.test_dir / "invalid_test.txt"
        with invalid_file.open("w") as f:
            f.write("11111\n")          
            f.write("000011112222\n")   
            f.write("0" * 208 + "\n")  

        analyzer = SensorFileAnalyzer(invalid_file)

        with self.assertLogs(level='WARNING') as log:
            analyzer.analyze()

       
        self.assertTrue(any("Ogiltig rad" in message for message in log.output))

        
        invalid_file.unlink()

