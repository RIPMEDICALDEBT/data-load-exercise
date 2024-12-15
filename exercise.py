"""Instructions:

You have a data file, it contains a fake sample of medical debt records. We have a donor who wished to purchase and forgive debt in the following states:

AZ, NM, TX, UT, CO

What you need to do:
1. Read the file
2. Design some database tables that will normalize these records (up to you how to do this)
3. Load the file into your tables
4. Run a query/report that tells us how much debt is available to be purchased on the counties in question
5. Design some way to select and assign debt to our donor

identifier(pk): UUID for each debt account
first_name: Name of the debtor
last_name:
date_of_birth: DOB of the debtor
address: Address of the debtor
city: debtor
Zipcode: debtor
State: Debtor residence
ssn: Social security number of the debtor
creditor: The hospital or healthcare facility that charged the account to begin with
account: Identifier of original account at the hospital
current_balance: How much debt is owed
sale_price: How much the account costs for RIP to buy
"""

import pandas as pd
import sqlite3 as sql
import csv


def get_db_connection():
  return sql.connect('test.db')
