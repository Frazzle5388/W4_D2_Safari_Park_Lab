import pdb
from models.staff import Staff

import repositories.staff_repository as staff_repository

staff_repository.delete_all()

staff1 = Staff("Jackie Bird", "01/04/2020", "Marketing", 4)
staff_repository.save(staff1)
staff2 = Staff("Leonardo", "01/01/2019", "Entertainment", 5)
staff_repository.save(staff2)
staff3 = Staff("Raphael", "06/05/1980", "Animal Welfare", 1)
staff_repository.save(staff3)
staff4 = Staff("Donatello", "06/05/1980", "Food & Drink", 2)
staff_repository.save(staff4)
