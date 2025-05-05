import pandas as pd
import os

# read in sheet "yields" from Exel file
def readyields(file):
    workbook = pd.read_excel(
        os.path.join(file),
        engine='openpyxl',
        sheet_name=0
    )
    a = workbook
    return a

# read in sheet "stammdaten" from Exel file
def stammdaten(file):
    workbook = pd.read_excel(
        os.path.join(file),
        engine='openpyxl',
        sheet_name=1,
    )
    b = workbook
    return b

'''def stammdaten():
    workbook = pd.read_excel(
        os.path.join("0Molau.xlsx"),
        engine='openpyxl',
        sheet_name=1,
    )
    b = workbook
    return b'''

# read in sheet "components" from Exel file
def readcomponents(file):
    workbook = pd.read_excel(
        os.path.join(file),
        engine='openpyxl',
        sheet_name=2,
    )
    c = workbook
    return c

# read in sheet "curtailments" from Exel file
def readcurtailments(file):
    workbook = pd.read_excel(
        os.path.join(file),
        engine='openpyxl',
        sheet_name=3,
    )
    d = workbook
    return d

def readevents(file):
    workbook = pd.read_excel(
        os.path.join(file),
        engine='openpyxl',
        sheet_name=4,
    )
    e = workbook
    return e
