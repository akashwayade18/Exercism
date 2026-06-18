import random
import string

class Robot:
    all_names = set()
    
    def __init__(self):
        self.name = None
        self.reset()

    def generate_name(self):
        while True:
            candidate_name = ''.join(random.choices(string.ascii_uppercase, k = 2)) + ''.join(random.choices(string.digits, k = 3))
            if candidate_name not in Robot.all_names:
                Robot.all_names.add(candidate_name)
                return candidate_name

    def reset(self):
        self.name = self.generate_name()