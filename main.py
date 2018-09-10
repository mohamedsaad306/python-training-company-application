from utils import Utils
from menu import menu
from menuItem import menuItem
from employeeSection import employeeSection

sections = {
    1: menuItem('(1) Employees', employeeSection),
}
employees = {}

sectionsMenu = menu(sections, '== Company ==')
sectionsMenu.activateMenu()
