import pandas as pd
import os


def set_working_dir(path):
    os.chdir(path)


def get_all_file_names():
    # you should do a error test here
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    return files



