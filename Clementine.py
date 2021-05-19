import eel
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from Clemen import Clemen
import time
import bstrap as bs
import sqlite3
import configparser

eel.init('web')
clem = Clemen()
done = False
con = sqlite3.connect("clementine.db")
cur = con.cursor()

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
    clem.set_df(d) # NOTE: change this to set_data
    columns = list(d)
    clem.set_column(columns)
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
    clem.set_column(col) # NOTE: change this to set_column_name()
    clem.set_stat(stat)
    clem.set_reps_passed(com)
    clem.set_total_reps(reps)
    clem.set_df(clem.get_df()[clem.get_column()]) # NOTE: change this to set_series
    create_db()
    sample()

@eel.expose
def sample():
    if int(clem.reps_passed) < int(clem.total_reps):
        series = clem.get_df() #NOTE: change this to get_series
        s = series.sample(series.size, replace = True) # gets sample same size as the series
    	# and samples with replacement
        m = s.mean()
        print("mean", m)
        sql = ''' INSERT INTO stats(statistic)
                  VALUES(?) '''
        #cur = conn.cursor()
        cur.execute(sql, (str(m),))
        con.commit()
        # passing the completed reps back to JS
        clem.set_reps_passed(int(clem.get_reps_passed()) + 1)
        print("Reps passed:", clem.get_reps_passed())
        # convert to a integer percent
        perc = round(( int(clem.get_reps_passed()) / int(clem.get_total_reps()) ) * 100)
        perc = str(perc) + "%"
        print("percent:", perc)
        print("------------------------")
        time.sleep(0.05)

        eel.updateProgressAndCallSample(perc)
    else:
        print("you is done!")
        eel.endProgress()

def create_db():
    print("CREATE TABLE()")
    tbl_name = set_table_name()
    create_table_query = "CREATE TABLE IF NOT EXISTS stats (statistic REAL);" #"CREATE TABLE IF NOT EXISTS " + tbl_name + " (statistic INTEGER);"
    print(create_table_query)
    cur.execute(create_table_query)
    return
    # make a function that takes one sample
    # inserts the sample into the db
    # updates com by 1
    # updates the progress bar with com
    # makes the function call again

def set_table_name():
    table_name = "stats" #clem.get_column().upper() + "_" + clem.get_stat.upper() + "S"
    return table_name

@eel.expose
def write_config(col_name, com, total):
    print("inside write_config()")
    # we need:
    # com, total
    # future work: stat
    config = configparser.ConfigParser()
    config['DEFAULT']['column_name'] = col_name # create new config
    config['DEFAULT']['completed_reps'] = com # create new config
    config['DEFAULT']['total_reps'] = total # create new config
    with open('history.ini', 'w') as configfile:    # save
        config.write(configfile)


eel.start("index.html", size=(600,600))
