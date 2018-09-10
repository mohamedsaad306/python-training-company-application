from utils import Utils
from menuItem import menuItem


class menu:
    meneItems = []
    selectedSection = None

    def __init__(self, actionsItems, menuTitle='Select Option'):
        self.menuTitle = menuTitle
        self.actionsItems = actionsItems

    def activateMenu(self):
        Utils.clear()
        while self.selectedSection != 0:
            print(self.menuTitle)
            for actionsItem in self.actionsItems:
                self.actionsItems[actionsItem].render()

            selectedSection = int(
                input('Select option or enter (0) to Exit: '))
            if selectedSection != 0:
                self.actionsItems[selectedSection].action()
                Utils.clear()
            elif selectedSection == 0:
                self.selectedSection = 0
                print('End.')
