"""Expense Tracker"""
import logging




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


def expense_caldulator():
    """
    Algorithm
    """
    get_the_expense_category()


if __name__ == "__main__":
    expense_caldulator()