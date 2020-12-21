"""Expense Tracker"""




def display_options():
    """"""
    print("""
    Select the option:
      a) Rent
      b) Groceries
      c) Bills 
    """)
    option_selected = input("selected option : ")
    return option_selected




if __name__ == "__main__":
    print("hello")
    display_options()