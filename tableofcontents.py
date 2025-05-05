import pandas as pd
import numpy as np
import os
from pylatex.utils import bold
import einlesen
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, NewPage, Command, NoEscape
import customcommand
from pylatex.base_classes import Environment, CommandBase, Arguments



def tableofcontents(doc):
    doc.append(Command("color", "White"))
    doc.append(" .")
    doc.append(Command("phantomsection"))
    doc.append(Command("color", "Black"))

    with doc.create(Section("Inhaltsverzeichnis", numbering=False)):
        doc.append(Command("phantomsection"))
        doc.append(customcommand.ExampleCommand(arguments=Arguments('toc', 'subsection', 'Inhaltsverzeichnis')))
        doc.append(Command('doublespacing'))
        doc.append(NoEscape('\\tableofcontents'))
        doc.append(Command('onehalfspacing'))