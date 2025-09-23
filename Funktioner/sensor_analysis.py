from pathlib import Path
from collections import defaultdict
import logging

logging.basicConfig(
    filename="sensor_analysis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class SensorFileAnalyzer:
    """Analyserar sensorloggar från en ubåt (208 sensorer per rad)."""

    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.submarine_id = filepath.stem
        self.pattern_counts = defaultdict(int)
        self.failures_per_row = []

    def analyze(self):
        """Streama filen rad för rad och räkna fel."""
        with self.filepath.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()

                
                if len(line) != 208 or not set(line) <= {"0", "1"}:
                    logging.warning(f"{self.submarine_id} - Ogiltig rad vid {line_no}")
                    continue

               
                failures = line.count("0")
                self.failures_per_row.append(failures)

                
                self.pattern_counts[line] += 1

    def summary(self):
        """Returnera en sammanfattning av analysen."""
        return {
            "submarine_id": self.submarine_id,
            "total_rows": len(self.failures_per_row),
            "avg_failures_per_row": (
                sum(self.failures_per_row) / len(self.failures_per_row)
                if self.failures_per_row else 0
            ),
            "unique_patterns": len(self.pattern_counts),
            "most_common_pattern": max(
                self.pattern_counts.items(),
                key=lambda kv: kv[1],
                default=(None, 0)
            )
        }
