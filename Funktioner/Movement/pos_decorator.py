



class posDecorator:

    """Den här klassen main funktion är att logga potensiela krockar som händer under ubåtarnas resa"""

    def __init__(self):
        self.log = []
        self.time_stamp = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.time_stamp += 1
            check = func(*args, **kwargs)
            positions = {}
            for key , value in check.items():
                value_key = tuple(value)
                positions[value_key] = positions.get(value_key,[]) + [f"{key}"]
            dups = {}
            for val,keys in positions.items():
                if len(keys) > 1:
                    dups[val] = keys
            if len(dups) > 0:
                self.log.append((f"Timestamp:{self.time_stamp}, Position:{dups}"))
            return check
        return wrapper
    
    def get_log(self):
        return(self.log)