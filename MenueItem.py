from utils import Utils

class MenueItem:
    def __init__(self,label,action = ''):
        self.label = label
        self.action = action
    
    def render(self):
        print (self.label)

