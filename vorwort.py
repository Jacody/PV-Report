import pandas as pd
import numpy as np
import os
from pylatex.utils import bold
import einlesen
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, NewPage, Command, NoEscape
import customcommand
from pylatex.base_classes import Environment, CommandBase, Arguments

# Funktion Vorwort

def vorwort(doc, file):

    # Sheet einlesen
    b = einlesen.stammdaten(file)

    # Variablen abspeichern
    Anrede= b.at[0, 'Data']
    EigentümerIn= b.at[1, 'Data']
    Anlagenname= b.at[2, 'Data']
    Straße= b.at[3, 'Data']
    Hausnummer= b.at[4, 'Data']
    Postleitzahl= b.at[5, 'Data']
    Stadt= b.at[6, 'Data']


    # Bilder importieren
    image_filename = os.path.join(os.path.dirname(__file__), 'firmenlogo.jpg')
    image_filename2 = os.path.join(os.path.dirname(__file__), 'signature.jpg')
    # set space
    doc.append(Command('begin','doublespace')) #set doublespace between lines for next chapter
    # Vorwort
    doc.append(Command("pagenumbering","arabic")) #switch on page numbering



    with doc.create(Section("Vorwort", numbering=False)):
        doc.append(customcommand.ExampleCommand(arguments=Arguments('toc', 'subsection', 'Vorwort')))
        doc.append(Anrede + ",")
        doc.append("\n")
        doc.append("\n anbei erhalten Sie den Jahresreport Ihrer Photovoltaikanlage mit der Adresse")
        doc.append("\n" + Straße + " " + str(Hausnummer) + " in " + str(Postleitzahl) + " " + Stadt + ".")
        doc.append("\n Wir bedanken uns für Ihr Vertrauen und hoffen auf ein ertragreiches Jahr 2023.")
        doc.append("\n Bei Fragen stehen wir Ihnen gerne zur Verfügung. ")
        doc.append("\n")
        doc.append("\n")
        doc.append("\n Mit sonnigen Grüßen")
        doc.append("\n")
        doc.append("\n")
        with doc.create(Figure(position='h!')) as signature_pic:
            signature_pic.add_image(image_filename2, width='120px', placement=" ")
        doc.append(Command('end', 'doublespace'))  # end doublespace between lines for  chapter
        doc.append(Command("color", "White"))
        doc.append(" .")
        doc.append(Command("color", "Black"))
        doc.append("\n Nicole Wiedmann (M.Sc.)")
        doc.append(Command('small'))
        doc.append("\n Technische Betriebsführung Photovoltaik")
        doc.append("\n")
        doc.append(Command('normalsize'))
        doc.append("\n")
        doc.append(bold("secur"))
        doc.append("energy GmbH")
        doc.append("\n Goerzallee 299")
        doc.append("\n 14167 Berlin")
        doc.append("\n")
        doc.append("\n Tel.: +49 (0)30 868 00 10 70")
        doc.append("\n Mob.: +49 (0)174 1866 075")
        doc.append("\n Mail: nicole.wiedmann@securenergy.de")
        doc.append(Command('small'))
        doc.append("\n")
        doc.append("\n")
        doc.append("\n")
        doc.append("\n")
        # frimenlogo einfügen
        with doc.create(Figure(position='h!')) as firmenlogo_pic:
            firmenlogo_pic.add_image(image_filename, width='180px', placement="")
