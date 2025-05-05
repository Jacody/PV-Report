import os
import einlesen
from pylatex import Document, Section, Subsection, Command, NoEscape, Figure, NewPage
from pylatex.utils import bold, italic
from datetime import datetime
import uuid

def certficat(doc, file):
    # Neue Seite für das Zertifikat
    doc.append(NewPage())
    
    # Überschrift für das Zertifikat
    with doc.create(Section('Leistungszertifikat', numbering=False)):
        doc.append(NoEscape(r'\vspace{0.5cm}'))
        
        # Anlagendaten einlesen
        anlagedaten = einlesen.stammdaten(file)
        ertraege = einlesen.readyields(file)
        
        # Zertifikatsnummer generieren
        zertifikatsnr = f"PV-CERT-{datetime.now().strftime('%Y')}-{str(uuid.uuid4())[:8].upper()}"
        
        # Rahmen für das Zertifikat erstellen
        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'\begin{tikzpicture}'))
        doc.append(NoEscape(r'\node[draw=RoyalBlue, line width=2pt, rounded corners=5pt, inner sep=1.5cm] {'))
        doc.append(NoEscape(r'\begin{minipage}{0.9\textwidth}'))
        
        # Zertifikatstitel
        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'{\Large\scshape\textcolor{RoyalBlue}{Bestätigung der Anlagenleistung}\\[0.3cm]}'))
        doc.append(NoEscape(r'{\large\textcolor{RoyalBlue}{' + anlagedaten['Anlagenname'][0] + r'}}\\[1cm]'))
        doc.append(NoEscape(r'\end{center}'))
        
        # Zertifikatstext
        doc.append(NoEscape(r'Dieses Zertifikat bestätigt, dass die Photovoltaikanlage:'))
        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'\textbf{' + anlagedaten['Anlagenname'][0] + '}\\'))
        doc.append(NoEscape(r'am Standort ' + str(anlagedaten['Ort'][0]) + ', ' + str(anlagedaten['Bundesland'][0]) + '\\'))
        doc.append(NoEscape(r'mit einer Nennleistung von ' + str(anlagedaten['Nennleistung (kWp)'][0]) + ' kWp'))
        doc.append(NoEscape(r'\end{center}'))
        
        # Leistungsdaten
        doc.append(NoEscape(r'im Berichtszeitraum folgende Kennzahlen erreicht hat:'))
        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'\begin{tabular}{lr}'))
        doc.append(NoEscape(r'Spezifischer Jahresertrag: & \textbf{' + f"{float(ertraege['Spezifischer Jahresertrag'][0]):.2f}" + ' kWh/kWp} \\'))
        doc.append(NoEscape(r'Performance Ratio: & \textbf{' + f"{float(ertraege['Performance Ratio'][0]*100):.1f}" + '\%} \\'))
        doc.append(NoEscape(r'Technische Verfügbarkeit: & \textbf{' + f"{float(ertraege['Verfügbarkeit'][0]*100):.2f}" + '\%} \\'))
        doc.append(NoEscape(r'\end{tabular}'))
        doc.append(NoEscape(r'\end{center}'))
        
        # Bestätigungstext
        doc.append(NoEscape(r'\vspace{0.5cm}'))
        doc.append(NoEscape(r'Diese Werte wurden gemäß den anerkannten Branchenstandards ermittelt und dokumentiert. Die Anlage erfüllt die Anforderungen für eine effiziente und nachhaltige Stromerzeugung aus Sonnenenergie.'))
        
        # Datum und Unterschriftszeile
        doc.append(NoEscape(r'\vspace{1cm}'))
        doc.append(NoEscape(r'\begin{minipage}{0.45\textwidth}'))
        doc.append(NoEscape(r'Ausstellungsdatum:\\'))
        doc.append(NoEscape(datetime.now().strftime(r'%d.%m.%Y')))
        doc.append(NoEscape(r'\end{minipage}'))
        doc.append(NoEscape(r'\hfill'))
        doc.append(NoEscape(r'\begin{minipage}{0.45\textwidth}'))
        doc.append(NoEscape(r'Zertifikatsnummer:\\'))
        doc.append(NoEscape(zertifikatsnr))
        doc.append(NoEscape(r'\end{minipage}'))
        
        # Unterschrift und Stempel Bereich
        doc.append(NoEscape(r'\vspace{1.5cm}'))
        doc.append(NoEscape(r'\begin{center}'))
        
        # Bild für die Unterschrift einfügen
        doc.append(NoEscape(r'\includegraphics[width=4cm]{signature.jpg}'))
        
        doc.append(NoEscape(r'\\[0.3cm]\hrulefill\\'))
        doc.append(NoEscape(r'Unterschrift und Stempel'))
        doc.append(NoEscape(r'\end{center}'))
        
        # Abschluss des Rahmens
        doc.append(NoEscape(r'\end{minipage}'))
        doc.append(NoEscape(r'};'))
        doc.append(NoEscape(r'\end{tikzpicture}'))
        doc.append(NoEscape(r'\end{center}'))
        
        # Kleingedrucktes
        doc.append(NoEscape(r'\vspace{0.5cm}'))
        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'{\footnotesize Dieses Zertifikat ist Teil des offiziellen Anlagenberichts. Die vollständigen Daten und Analysen finden Sie im Hauptteil des Berichts.}'))
        doc.append(NoEscape(r'\end{center}'))


