import eel
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from Clemen import Clemen
import time
import bstrap as bs
import sqlite3

eel.init('web')
clem = Clemen()
done = False

@eel.expose
def get_csv():
    print("start")
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    root.update()
    root.destroy()
    print("before pandas read")
    d = pd.read_csv(file_path)
    clem.set_df(df)
    columns = list(d)
    clem.set_columns(columns)
    print(columns)

    return columns

@eel.expose
def initialize_clemen(df):
    print("I am in initialize_clemen!")

    columns_list = []
    return(columns_list)

@eel.expose
def bootstrap(col, stat, reps, com):
    print(col, stat, reps, com)
    clem.set_column(col)
    clem.set_stat(stat)
    clem.set_reps_passed(com)
    clem.set_total_reps(reps)
    clem.set_df(clem.get_df[clem.get_column])
    create_db()
    sample()

def sample():
    series = clem.get_df
    s = series.sample(series.size, replace = True) # gets sample same size as the series
	# and samples with replacement
	m = s.mean()
    sql = ''' INSERT INTO stats(statistic)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, m)
    conn.commit()

    # passing the completed reps back to JS
    clem.set_reps_passed = clem.get_reps_passed + 1
    # convert to a integer percent
    perc = round(( clem.get_reps_passed / clem.get_total_reps ) * 100)
    return perc

def create_db():
    con = sqlite3.connect("clementine.db")
    cur = con.cursor()
    print("CREATE TABLE()")
    tbl_name = set_table_name()
    create_table_query = "CREATE TABLE IF NOT EXISTS stats (statistic INTEGER);" #"CREATE TABLE IF NOT EXISTS " + tbl_name + " (statistic INTEGER);"
    print(create_table_query)
    cur.execute(create_table_query)
    return
    # make a function that takes one sample
    # inserts the sample into the db
    # updates com by 1
    # updates the progress bar with com
    # makes the function call again

def set_table_name(self):
    table_name = clem.get_column().upper() + "_" + clem.get_stat.upper() + "S"
    return table_name


eel.start("index.html", size=(600,600))
