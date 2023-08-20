import sqlite3
import pandas as pd
import datetime as dt

from .constants import *


def get_transactions() -> pd.DataFrame:
    transactions = pd.read_excel(TILLER_PATH, sheet_name='Transactions', parse_dates=['Date', 'Month','Week','Date Added'])
    categories = pd.read_excel(TILLER_PATH, sheet_name='Categories')
    transactions = transactions.merge(categories[['Category','Group','Type']], how='left')
    return transactions
