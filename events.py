import pandas as pd
import numpy as np
import os
import numpy
from pandas import DataFrame
import einlesen

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, LongTabu, HFill, Command, UnsafeCommand, ColumnType
from pylatex.utils import italic, bold
import customcommand
from pylatex.base_classes import Environment, CommandBase, Arguments

def events(doc, file):

# read in yields
    e = einlesen.readevents(file)

# read in master data
    b = einlesen.stammdaten(file)

# save Plant Name
    Stadt = b.at[2, 'Data']


    doc.append(Command("color", "White"))
    doc.append(" .")
    doc.append(Command("color", "Black"))
    doc.append("\n")
    with doc.create(Section("Ereignisse"+" "+Stadt,numbering=False)):
        doc.append(customcommand.ExampleCommand(arguments=Arguments('toc', 'subsection', 'Ereignisse')))
        doc.append("\n")


    #doc.append(UnsafeCommand(ColumnType("Y", "C", parameters=None)[source]))
    with doc.create(LongTabu('p{10,5cm}p{2,5cm}')) as data_table:
        data_table.add_hline()
        header_row1 = ["Ereignisse", "Datum"]
        data_table.add_row(header_row1, strict=False)
        data_table.add_empty_row()
        data_table.add_hline()
        data_table.end_table_header()


    for i in range(len(e)):
        #data_table.add_hline()
        row = [ e.at[i, 'Ereignisse'], str(e.at[i, 'Beginn'])[8:10]+"."+str(e.at[i, 'Beginn'])[5:7]+"."+str(e.at[i, 'Beginn'])[2:4]]
        data_table.add_row(row, strict=False)
        data_table.add_empty_row()

