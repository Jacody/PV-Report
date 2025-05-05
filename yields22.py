import pandas as pd
import numpy as np
import os
import einlesen

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, LongTabu, HFill, Command

from pylatex.utils import bold, NoEscape
import customcommand
from pylatex.base_classes import Environment, CommandBase, Arguments

# define function yields
def yields22(doc, file):

# read in yields
    a = einlesen.readyields(file)

# read in master data
    b = einlesen.stammdaten(file)

# save Plant Name
    Stadt = b.at[2, 'Data']

#Spezial Fall Miltern
    if ((a.at[0, 'Ertrag22']) == 0):
        a.at[12, 'Prognose'] = a.at[14, 'Prognose']
# import yield graph
    pic = str(str(Stadt) + str(2))
    image_filename = os.path.join('/Users/jacobscheer/Graphen/', pic)

# create section Plant yield
    doc.append(Command("color", "White"))
    doc.append(" .")
    doc.append(Command("color", "Black"))
    doc.append("\n")
    with doc.create(Section("Ertragsübersicht 2022" + " - " + Stadt,numbering=False)):
        doc.append(customcommand.ExampleCommand(arguments=Arguments('toc', 'subsection', 'Ertragsübersicht 2022')))
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
        row = [a.at[i, 'Monat'], str(format(round(a.at[i, 'Prognose'],1), ",.1f")).replace(".","b").replace(",",".").replace("b",","), str(format(round(a.at[i, 'Ertrag22'],1), ",.1f")).replace(".","b").replace(",",".").replace("b",",").replace("nan"," ").replace("0,0"," "), (" "+(str(round(100*a.at[i, 'Performance22']))+'%')).replace(" 0%"," ")]
        data_table.add_row(row)

    data_table.add_hline()
    data_table.add_empty_row()

# fill table with cumulated data
    row = [bold(a.at[12, 'Monat']), str(format(round(a.at[12, 'Prognose'],1), ",.1f")).replace(".","b").replace(",",".").replace("b",","), str(format(round(a.at[12, 'Ertrag22'],1), ",.1f")).replace(".","b").replace(",",".").replace("b",","), bold(str(round(100*a.at[12, 'Performance22']))+'%')]
    data_table.add_row(row)

# add graph
    with doc.create(Figure(position='h!')) as Ertrag22:
        Ertrag22.add_image(image_filename, width='400px', )
