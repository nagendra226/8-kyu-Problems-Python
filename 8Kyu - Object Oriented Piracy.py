class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    def is_worth_it(self):
        if(self.draft == 0 and self.crew ==0):
            return False
        else:
            return self.draft - self.crew * 1.5 > 20
