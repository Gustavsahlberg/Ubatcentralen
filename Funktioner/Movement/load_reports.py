from itertools import zip_longest
from Funktioner.Movement.pos_decorator import posDecorator



logger = posDecorator()

class loadReports:
    """Den här klassens syfte är att öppna och läsa alla filer på ett effektift sätt"""
    
    def __init__(self,folder):
        self.files = [f.open("r", encoding="utf-8") for f in folder.iterdir()]
        self.filename = [f.name for f in folder.iterdir()]
        self.pos = {}
        
    
    @logger
    def row_iter(self,rows):
        for i, row in enumerate(rows):
            #print(f"i = {self.filename[i]} och row = {row}")
            xy = self.pos.get(self.filename[i],[0,0])
            row = row.strip()
            if row[0] == "f":
                row = row.replace("forward","").strip()
                xy[1] += int(row)
            elif row[0] == "u":
                row = row.replace("up","").strip()
                xy[0] += int(row)
            else:
                row = row.replace("down","").strip()
                xy[0] -= int(row)
            self.pos[self.filename[i]] = xy
        return self.pos


    def read_files(self):
        for rows in zip_longest(*self.files):
            self.row_iter(rows)

        for f in self.files:
            f.close()


    def get_sub_sn(self):
        return self.filename
    