import pandas as pd
import numpy as np
import os
import einlesen

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, LongTabu, HFill, Command, NewPage

from pylatex.utils import bold, NoEscape

import customcommand
from pylatex.base_classes import Environment, CommandBase, Arguments

# define function yields
def yields21(doc, file):

# read in yields
    a = einlesen.readyields(file)

# read in master data
    b = einlesen.stammdaten(file)

# save Plant Name
    Stadt = b.at[2, 'Data']
    if ((a.at[0, 'Ertrag21'])==0):
        a.at[12, 'Prognose']=a.at[14, 'Prognose']
    if (a.at[11, 'Ertrag21']!=0):
        doc.append(NewPage())



# import yield graph
        pic=str(str(Stadt)+str(1))
        image_filename = os.path.join('/Users/jacobscheer/Graphen/', pic)
        #image_filename = os.path.join(os.path.dirname(__file__), '0-2021.jpg')


        doc.append(Command("color", "White"))
        doc.append(" .")
        doc.append(Command("color", "Black"))
        doc.append("\n")

# create section Plant yield
        with doc.create(Section("Ertragsübersicht 2021" + " - " + Stadt, numbering=False)):
            doc.append(customcommand.ExampleCommand(arguments=Arguments('toc', 'subsection', 'Ertragsübersicht 2021')))
            doc.append("\n")
# create Table
        with doc.create(LongTabu("X[l] X[r] X[r] X[r]")) as data_table:
            header_row1 = ["Monat", "Prognose [kWh]*", "Ertrag [kWh]*", "Performance [%]*"]
            data_table.add_hline()
            data_table.add_row(header_row1)
            data_table.add_empty_row()
            data_table.add_hline()
            data_table.end_table_header()

# fill table with monthly data
        for i in range(12):
            row = [a.at[i, 'Monat'], str(format(round(a.at[i, 'Prognose'],1), ",.1f")).replace(".","b").replace(",",".").replace("b",","), str(format(round(a.at[i, 'Ertrag21'],1), ",.1f")).replace(".","b").replace(",",".").replace("b",",").replace("0,0"," "), (" "+str(+round(100*a.at[i, 'Performance21']))+'%').replace(" 0%"," ")]
            data_table.add_row(row)

        data_table.add_hline()
        data_table.add_empty_row()

# fill table with cumulated data
        row = [bold(a.at[12, 'Monat']), str(format(round(a.at[12, 'Prognose'],1), ",.1f")).replace(".","b").replace(",",".").replace("b",","), str(format(round(a.at[12, 'Ertrag21'],1), ",.1f")).replace(".","b").replace(",",".").replace("b",","), bold(str(round(100*a.at[12, 'Performance21']))+'%')]
        data_table.add_row(row)

# add graph
        with doc.create(Figure(position='h!')) as Ertrag21:
            Ertrag21.add_image(image_filename, width='400px', )

