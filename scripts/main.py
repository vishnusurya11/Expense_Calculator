"""Expense Tracker"""
import logging
import expense_calculation_class_objects
import pickle
import pprint
import json
import time
from datetime import datetime


logging.basicConfig(filename='../log/Error_log.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

def get_the_expense_category():
    """
    
    """
    try:
        print("""
        Select the Expense Catrgory:
        a) Rent
        b) Groceries
        c) Bills 
        d) Other
        """)
        option_selected = input("select a option : ")
    except Exception as e:
        logging.exception(e)

    return option_selected


def write_object_to_file(expense):
    with open("../data/test.json",'w') as output:
        json.dump(expense,output)


def expense_calculator():
    """
    Algorithm
    """
    expense = dict()
    expense["id"] =  int(round(time.time() * 1000)) 
    expense["create_time"] = datetime.now().strftime("%m -%d -%Y  %H:%M:%S PST") 
    expense["expense_type"] = get_the_expense_category()
    write_object_to_file(expense)

if __name__ == "__main__":
    expense_calculator()
    