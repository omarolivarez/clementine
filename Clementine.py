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
    print("Inside get_csv()")
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
        print("Reps passed:", clem.get_reps_passed()) # NOTE: update this to: completed reps
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
    # NOTE: dump table once the bootstrap is done
    cur.execute(create_table_query)
    return

def set_table_name():
    table_name = "stats" #clem.get_column().upper() + "_" + clem.get_stat.upper() + "S"
    return table_name

@eel.expose
def write_config():
    print("inside write_config()")
    # we need:
    # com, total
    # future work: stat
    config = configparser.ConfigParser()
    config['DEFAULT']['column_name'] = clem.get_column() # create new config
    config['DEFAULT']['completed_reps'] = str(clem.get_reps_passed()) # create new config
    config['DEFAULT']['total_reps'] = str(clem.get_total_reps()) # create new config
    with open('history.ini', 'w') as configfile:    # save
        config.write(configfile)
    return

@eel.expose
def import_history():
    # create the window to select the .ini's file path
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print("This is the selected file path:", file_path)
    root.update()
    root.destroy()

    print("Reading in the .ini file")
    config = configparser.ConfigParser()
    config.read(file_path)

    # get variables from history_path
    col_name = config['DEFAULT']['column_name']
    com_reps = config['DEFAULT']['completed_reps']
    total_reps = config['DEFAULT']['total_reps']
    stat = "Mean"

    # set the values from .ini into clem object
    clem.set_column(col_name)
    clem.set_reps_passed(com_reps)
    clem.set_total_reps(total_reps)
    clem.set_total_reps(stat)

    eel.updateConfigs(col_name, com_reps, total_reps, stat)
    return

eel.start("index.html", size=(600,600))
