

from utils import Utils
from MenueItem import MenueItem 
from Employee import EmployeeSection

sections = {
    0:MenueItem('(0) Employees',EmployeeSection()),
    1:MenueItem('(1) Departments') 
    }

for section in  sections:
    section.render()

# selectedSection = int(input('Select Section: '))
# if  selectedSection == 1:
#     section[1]