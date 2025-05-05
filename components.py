import einlesen
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, NewPage, LongTabu


#define function "components"
def components(doc, file):

# read in Sheet
    c = einlesen.readcomponents(file)

    with doc.create(LongTabu("X[l] X[l] X[l] X[l]")) as data_table:
        data_table.add_hline()
        header_row1 = ["Element", "Typ", "Leistung", "Seriennummer"]
        data_table.add_row(header_row1)
        data_table.add_empty_row()
        data_table.add_hline()
        data_table.add_empty_row()
        data_table.end_table_header()


    for i in range(len(c)):
        row = [c.at[i, 'Element'], c.at[i, 'Typ'], str(c.at[i, 'Leistung']).replace("nan",""), str(c.at[i, 'Seriennummer']).replace("nan","")]
        data_table.add_row(row)
