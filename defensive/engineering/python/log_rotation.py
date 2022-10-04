#!/bin/python3

import shutil
from datetime import datetime

naming = "_LT_completed.csv"
path_rotation = "/home/scripting/LOG_ROTATION/"
data = "/home/scripting/Zzz.csv"

def get_date():
    
    current = datetime.now().date()
    str_date = str(current) 
    return str_date

def log_rotation():
    
    date = get_date()
    file_compose = path_rotation + date + naming
    
    shutil.move(data,file_compose)

def main():
    LR = log_rotation
    LR()

main()

