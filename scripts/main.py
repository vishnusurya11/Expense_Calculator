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


def get_expense_options(keyvalue):
    """
    takes the key value of the option to be selected and returns the options related to that key
    """
    try:
        print('please select a option from below : ')
        with open('config/expense_details.json') as f:
            data = json.load(f)
        for key,value in data[keyvalue].items():
            print(key + ' : '+ value)
        return data[keyvalue]
    except Exception as e:
        logging.exception(e)
        return None

def selected_option(keyvalue):
    """
    takes the key value as input and returns value for selected key 
    """
    try:
        options = get_expense_options(keyvalue)
        option_selected = input("selected a option : ")
        return options[option_selected]
    except Exception as e:
        logging.exception(e)
        return None


def write_object_to_file(expense):
    """
    writes the expense object to the json file
    """
    try:
        with open("../data/test.json",'w') as output:
            json.dump(expense,output)
    except Exception as e:
        logging.exception(e)
        return None


def expense_calculator():
    """
    Algorithm
    """
    expense = dict()
    expense["id"] =  int(round(time.time() * 1000)) 
    expense["create_time"] = datetime.now().strftime("%m -%d -%Y  %H:%M:%S PST") 
    expense["expense_type"] = selected_option("expense_type")
    expense["expense_name"] = selected_option("expense_name")
    write_object_to_file(expense)

if __name__ == "__main__":
    expense_calculator()
