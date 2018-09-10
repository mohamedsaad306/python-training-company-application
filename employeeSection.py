from baseSection import baseSection
from menu import menu
from menuItem import menuItem
from employeeLogic import employeeLogic


class employeeSection(baseSection):
    empLogic = None
    actions = None

    def __init__(self):
        self.empLogic = employeeLogic() 
        self.actions = {
            1: menuItem('(1) New Employee', self.empLogic.newEmployee)
        }
        self.employeeSectionActivate()

    def employeeSectionActivate(self):
        empMenu = menu(
            self.actions, '===== Employees Management Section =====')
        empMenu.activateMenu()
