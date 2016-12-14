from profile import Profile

class SocialNet(): #how would it inherit dict?

    def __init__(self,label='None', profiles = {}):
        self.label = label
        self.profiles = profiles

    def add(self, Prof):
        self.profiles[Prof.name] = Prof.getFriends()

    def lookup(self, name):
        if name in self.profiles:
            return True
        else:
            return False
        


