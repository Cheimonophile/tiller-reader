import sqlite3
import pandas as pd
import datetime as dt

from .constants import *


def tiller_to_db():
    transactions = pd.read_excel(TILLER_PATH, sheet_name='Transactions', parse_dates=['Date', 'Month','Week','Date Added'])
    categories = pd.read_excel('../Tiller.xlsx', sheet_name='Categories')
    transactions = transactions.merge(categories[['Category','Group','Type']], how='left')
    transactions.columns = transactions.columns.str.lower().str.replace(' ', '_').str.replace('#','no')
    transactions = transactions.set_index('transaction_id').reset_index()
    transactions['amount'] = transactions['amount'].mul(100).astype(int)
    transactions[['date', 'month', 'week', 'date_added']] = transactions[['date', 'month', 'week', 'date_added']].astype(str)
    transactions.to_csv(TILLER_LOGS_DIR / f"tiller-{dt.date.today()}.csv", index=False)
    with sqlite3.connect(DB_PATH) as conn:
        sql = f"""INSERT OR REPLACE INTO transactions VALUES ({', '.join(f":{c}" for c in transactions.columns)});"""
        rows = [
            {c: row[c] for c in transactions.columns}
            for _, row in transactions.iterrows()
        ]
        conn.executemany(sql, rows)


def get_transactions() -> pd.DataFrame:
    tiller_to_db()
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql("SELECT * FROM transactions;", conn, parse_dates=['date', 'month','week','date_added'])
        df['amount'] = df['amount'].div(100).round(2)
    return df
