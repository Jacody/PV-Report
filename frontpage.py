import pandas as pd
import numpy as np
import os
from pylatex.utils import bold
import einlesen
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, NewPage, Command, NoEscape

# Funktion frontpage

def frontpage(doc,file):
    # Sheet einlesen
    b = einlesen.stammdaten(file)
    Anlagenname = b.at[2, 'Data']
    EigentümerIn=b.at[1, 'Data']
    InbetriebsetzungDC=b.at[16, 'Data']
    #image_filename2 = '/Users/jacobscheer/PycharmProjects/FirstPythonProject/titelseite.jpg'
    #image_filename2 = os.path.join('/Users/jacobscheer/PycharmProjects/FirstPythonProject/', 'titelseite.jpg')
    image_filename2 = os.path.join(os.path.dirname(__file__), 'titelseite.jpg')

    #doc.append(Command('begin', 'titlepage'))
    doc.append(Command('newgeometry', "top=4cm, left=2cm"))
    Backgroundsettings=NoEscape("scale=1,color=black,opacity=1,angle=0,contents={\includegraphics[width=\paperwidth,height=\paperheight]{/Users/jacobscheer/PycharmProjects/FirstPythonProject/titelseite.jpg}}")
    doc.append(Command('backgroundsetup', Backgroundsettings))
    doc.append(Command('BgThispage'))
    doc.append(Command('clearpage'))
    doc.append(Command('thispagestyle','empty')) #remove header and footer
    doc.append(Command('pagenumbering', 'gobble')) #switch off page numbering



    doc.append(Command("color", "SkyBlue"))
    doc.append(".")
    doc.append("\n")
    doc.append("\n")
    doc.append("\n")
    doc.append(Command("color", "Black"))
    doc.append(Command('Huge'))
    if Anlagenname=="Miltern":
        doc.append("JAHRESREPORT 2022")
    else:
        doc.append("JAHRESREPORT 2021/2022")
    doc.append("\n")
    doc.append("\n")
    doc.append("\n")
    doc.append("\n")
    doc.append(Command('huge'))
    doc.append('PVA '+Anlagenname)
    doc.append("\n")
    doc.append("\n")
    doc.append("\n")
    doc.append(Command('Large'))
    doc.append(EigentümerIn)
    doc.append("\n")
    doc.append("\n")
    doc.append("\n")
    doc.append("IBN: "+InbetriebsetzungDC)
    doc.append(Command('normalsize'))
    doc.append(Command('restoregeometry'))
    doc.append(NewPage())
    #doc.append(Command('end', 'titlepage'))
