import pandas as pd
import os
import einlesen
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, NewPage, LongTabu, Command
import customcommand
from pylatex.base_classes import Environment, CommandBase, Arguments

# Function Anlage Daten
def anlagedaten(doc, file):

# read in Sheet
    b = einlesen.stammdaten(file)

# save Variables
    Stadt= b.at[2, 'Data']
    Anlagenleistung=str(b.at[15,'Data']).replace(".",",")+" kWp"
    InbetriebsetzungDC=b.at[16,'Data']
    InbetriebsetzungAC=b.at[17,'Data']
    EEGSchlüssel=b.at[18,'Data']
    Netzbetreiber=b.at[19,'Data']
    Direktvermarkter=b.at[20,'Data']
    Vergütung=str(b.at[21,'Data']).replace(".",",")+" EUR"
    Anlagennummer=b.at[22,'Data']

#\newgeometry{⟨options⟩}
# create Section Plant Data
    doc.append(Command("color", "White"))
    doc.append(" .")
    doc.append("\n")
    doc.append(Command("color", "Black"))

    with doc.create(Section("Anlagendaten"+" - "+Stadt ,numbering=False)):
        doc.append(customcommand.ExampleCommand(arguments=Arguments('toc', 'subsection', 'Anlagendaten')))
        doc.append("\n")
        doc.append(Command("color", "Black"))
# create Table Head
    with doc.create(LongTabu("X[l] X[l]")) as data_table:
        data_table.add_empty_row()
        data_table.end_table_header()

# fill table
    data_table.add_row('Anlagenleistung', Anlagenleistung)
    data_table.add_row('Standort', Stadt)
    data_table.add_row('Inbetriebsetzung DC', InbetriebsetzungDC)
    if InbetriebsetzungAC != '-':
        data_table.add_row('Inbetriebsetzung AC', InbetriebsetzungAC)
    data_table.add_row('EEG-Schlüssel', EEGSchlüssel)
    data_table.add_row('Netzbetreiber', Netzbetreiber)
    if Direktvermarkter != '-':
        data_table.add_row('Direktvermarkter', Direktvermarkter)
    if Vergütung != '-':
        data_table.add_row('Vergütung', Vergütung)
    data_table.add_row('Anlagennummer', Anlagennummer)


