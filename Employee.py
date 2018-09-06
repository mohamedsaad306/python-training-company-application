from BaseSection import BaseSection
from MenueItem import MenueItem

class EmployeeSection (BaseSection):
    actions = [MenueItem('(0) New Employee'),MenueItem('(1) Edit Employee')]
    
    def __init__(self):
        self.clear()
        print('Emp Section initiated. ')
        # for action in actions:
        #     print (action.render())
