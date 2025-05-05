import pandas as pd
import numpy as np
import os
from pylatex.utils import bold

from pylatex.base_classes import Environment, CommandBase, Arguments
import explanation
import frontpage
import multipleprojectfiles
import tableofcontents
import anlagedaten
import components
import vorwort
import yields21
import yields22
import curtailments
import events
import header
import comparison
import customcommand

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, NewPage, Command, NoEscape, StandAloneGraphic, escape_latex, UnsafeCommand

# main method
if __name__ == "__main__":

    def create_pdf(file):
    # specify basic settings
        geometry_options = {"tmargin": "2cm", "lmargin": "3cm"}
        doc = Document(geometry_options=geometry_options)


        #doc.preamble.append(Command('usepackage', 'tgheros'))

        #doc.preamble.append(Command('usepackage', 'opensans', 'default,oldstyle,scale=0.95')) #set font to Open Sans
        doc.preamble.append(Command('usepackage', 'arev')) #set font to Arev
        #doc.preamble.append(Command('renewcommand',  NoEscape('\\familydefault'),options=None,extra_arguments=NoEscape('\\sfdefault')))#set to thgeros
        #doc.preamble.append(Command('usepackage', 'berasans', 'scaled=0.88')) #set font to berasans
        #doc.preamble.append(Command('renewcommand',  NoEscape('\\familydefault'), options=None, NoEscape('\sfdefault')))#set font to berasans
        doc.preamble.append(Command('usepackage', 'fontenc', 'T1')) #set Arev
        doc.preamble.append(Command('renewcommand',  NoEscape('\contentsname'),options=None,extra_arguments='')) # set ToC Name
        doc.preamble.append(Command('usepackage', 'xcolor', 'dvipsnames')) #to set color
        doc.preamble.append(Command('usepackage', 'tabularx'))  #to set table column width
        doc.preamble.append(Command('usepackage', 'setspace')) #to set space between lines
        doc.preamble.append(Command('usepackage','geometry'))# 'top=0cm, bottom=2cm, outer=0cm, inner=0cm')) #for titlepage
        doc.preamble.append(Command('usepackage','background', 'pages=some')) #background of titlepage
        doc.preamble.append(Command('usepackage','tikz')) #for placement of title
        doc.append(Command('onehalfspacing')) #set onehalfspacing between lines for next chapter
        doc.preamble.append(Command('usepackage', 'fancyhdr'))  # to adjust the pagenumbers
        doc.preamble.append(Command('usepackage', 'titlesec')) #to adjust the style of titles

        #\titleformat{\section}{\normalfont\scshape\Huge}{\thesection}{1em}{}
        #new_comm = UnsafeCommand('newcommand', '\titelformat', options=5,)
        #doc.preamble.append(new_comm)
        #doc.preamble.append(\titelformat(arguments=Arguments('\section', '\normalfont\scshape\Huge', '\thesection', '1em','')))
        #doc.preamble.append()

        # add frontpage
        frontpage.frontpage(doc, file)

        # add page 2
        doc.append(NewPage())

        # add header
        header.generate_header(doc)

        # add Foreword
        vorwort.vorwort(doc, file)

        # add page 2
        doc.append(NewPage())

        # add table of contents
        tableofcontents.tableofcontents(doc)

        # add new page
        doc.append(NewPage())

        # add Plant Data
        anlagedaten.anlagedaten(doc, file)

        # add table of components
        components.components(doc, file)

        # add page 3

        # add table of yields 2021
        yields21.yields21(doc, file)

        # add page 4
        doc.append(NewPage())

        # add table of yields 2022
        yields22.yields22(doc, file)

        # add page 4.5
        doc.append(NewPage())

        # add Explanation
        explanation.explanation(doc)


        comparison.comparison(doc, file)

        # add page 5
        doc.append(NewPage())

        # add table of events
        events.events(doc, file)


        # add table of curtailments
        curtailments.curtailments(doc, file)



        # generate PDF
        path = "/Users/jacobscheer/Desktop/Alle Anlagen Reports/"
        print(file)
        doc.generate_pdf(path + 'report_'+file, clean_tex=False)


    anlagen_path = "/Users/jacobscheer/Desktop/Alle Anlagen"
    multipleprojectfiles.set_working_dir(anlagen_path)
    print("Current working directory " + os.getcwd())
    '''
    x = input("Do you want to create one (one) or multiple reports (multiple)? ")

    if x == "o":'''
    print("one report")
        #file = "Molau.xlsx"
        #create_pdf(file)
    exel_filenames = multipleprojectfiles.get_all_file_names()
        #print(exel_filenames)
    for j in range(len(exel_filenames)):
        print(j,exel_filenames[j])
    i = int(input("Which report number do you want? (0-24) "))
    file = exel_filenames[i]
    print(file)
    create_pdf(file)
'''
    elif x == "m":
        print("multiple reports")
        exel_filenames = multipleprojectfiles.get_all_file_names()
        print(exel_filenames)
        for file in exel_filenames:
            print(file)
            create_pdf(file)
    else:
        print("Not a valid answer")
'''