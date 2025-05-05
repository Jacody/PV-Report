import pandas as pd
import numpy as np
import os
import einlesen

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, LongTabu, HFill, Command, NewPage

from pylatex.utils import bold, NoEscape
import customcommand
from pylatex.base_classes import Environment, CommandBase, Arguments


def comparison(doc, file):
        # read in master data
    b = einlesen.stammdaten(file)
    a = einlesen.readyields(file)
    # sonderfall Miltern ausschließen
    if (a.at[11, 'Ertrag21'] != 0):

        Stadt = b.at[2, 'Data']
        pic = str(str(Stadt) + str(3))
        image_filename = os.path.join('/Users/jacobscheer/Graphen/', pic)
        b = einlesen.stammdaten(file)
        Stadt = b.at[2, 'Data']


        doc.append(NewPage())
        # create section Plant yield
        doc.append(Command("color", "White"))
        doc.append(" .")
        doc.append(Command("color", "Black"))
        doc.append("\n")
        with doc.create(Section("Jahresvergleich" + " - " + Stadt, numbering=False)):
            doc.append(customcommand.ExampleCommand(arguments=Arguments('toc', 'subsection', 'Jahresvergleich')))
            doc.append("\n")

        doc.append("\n In der folgenden Grafik sind die Erträge der vergangenen zwei Jahre über die prognostizierte")
        doc.append("\n Ertragskursve gelegt.")
        doc.append("\n")
        doc.append("\n")
        with doc.create(Figure(position='h!')) as Ertrag22:
            Ertrag22.add_image(image_filename, width='400px', )