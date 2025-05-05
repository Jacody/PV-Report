
from pylatex.utils import bold
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, NewPage, Command




def explanation (doc):
    doc.append(Command("color", "White"))
    doc.append(" .")
    doc.append(Command("color", "Black"))
    doc.append("\n")
    doc.append("\n")
    doc.append("\n")
    doc.append("\n")
    doc.append(bold("*Prognose: "))
    doc.append("Die Prognose wurde mittels PVSol durchgeführt.")
    doc.append("\n")
    doc.append("\n")
    doc.append(bold("*Ertrag: "))
    doc.append("Die Ertragsdaten wurden vom installierten Datenloggern bezogen. Aufgrund von Kommunikationsproblemen, sowie elektrischen Verlusten und anderen technischen Gründen, können die Werte von den Ertragswerten des Netzbetreibers und Energievermarkters abweichen.")
    doc.append("\n")
    doc.append("\n")
    doc.append(bold("*Performance: "))
    doc.append("Ist hierbei das Verhältnis von Ertrag zu Prognose.")
