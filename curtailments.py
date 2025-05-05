import pandas as pd
import numpy as np
import os
import numpy
from pandas import DataFrame
import einlesen

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, LongTabu, HFill, Command,  NewPage
from pylatex.utils import italic, bold
import customcommand
from pylatex.base_classes import Environment, CommandBase, Arguments

def curtailments(doc, file):

# read in yields
    d = einlesen.readcurtailments(file)

# read in master data
    b = einlesen.stammdaten(file)

# save Plant Name
    if (len(d)) > 0:
        Stadt = b.at[2, 'Data']
        doc.append(NewPage())
        doc.append(Command("color", "White"))
        doc.append(" .")
        doc.append(Command("color", "Black"))
        doc.append("\n")
        with doc.create(Section("Abregelungen"+" "+Stadt,numbering=False)):
            doc.append(customcommand.ExampleCommand(arguments=Arguments('toc', 'subsection', 'Abregelungen')))
            doc.append("\n")



        with doc.create(LongTabu('p{8cm}p{2,5cm}p{2,5cm}')) as data_table:
            data_table.add_hline()
            header_row1 = ["Abregelungen", "Beginn", "Ende"]
            data_table.add_row(header_row1)
            data_table.add_empty_row()
            data_table.add_hline()
            data_table.end_table_header()


        for i in range(len(d)):
            row = [ d.at[i, 'Abregelungen'], str(d.at[i, 'Beginn'])[8:10]+"."+str(d.at[i, 'Beginn'])[5:7]+"."+str(d.at[i, 'Beginn'])[2:4]+" "+str(d.at[i, 'Beginn'])[-8:-3], str(d.at[i, 'Ende'])[8:10]+"."+str(d.at[i, 'Ende'])[5:7]+"."+str(d.at[i, 'Ende'])[2:4]+" "+str(d.at[i, 'Ende'])[-8:-3]]
            data_table.add_row(row)

        doc.append("\n")
        doc.append(bold("NB: "))
        doc.append("Abregelungen durch den Netzbetreiber (NB)")
        doc.append("\n")
        doc.append(bold("DV: "))
        doc.append("Abregelungen durch den Direktvermarkter (DV)")