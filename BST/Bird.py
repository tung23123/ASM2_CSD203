class Bird:
    def __init__(self, type="", rate=-1,wing = -1):
        self.Type = type
        self.Rate = rate
        self.Wing = wing
    def __repr__(self):
        return f"({self.Type}, {self.Rate}, {self.Wing})"    
