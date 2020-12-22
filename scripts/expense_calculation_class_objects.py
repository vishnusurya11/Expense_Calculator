"""Expense Calculator Objects"""

import logging
import time
from datetime import datetime

class ExpenseRecord():

    def __init__(self):
       self.expense_id = int(round(time.time() * 1000)) 
       self.create_time = datetime.now().strftime("%m -%d -%Y  %H:%M:%S PST") 
    
    expense_type = None