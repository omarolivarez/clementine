import eel
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from Clemen import Clemen
import time

eel.init('web')
clem = Clemen()

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
    for i in range(100):
        print(i)
        time.sleep(0.5)



eel.start("index.html", size=(600,600))
