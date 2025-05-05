# PV-Report Generator

Dieses Projekt erstellt automatisierte, professionelle PDF-Berichte für Photovoltaikanlagen. Es liest Anlagendaten aus Excel-Dateien und generiert detaillierte Berichte mit Informationen zu Erträgen, Ereignissen und Anlagenkomponenten.

[📄 Beispielreport direkt anzeigen](https://raw.githubusercontent.com/Jacody/PV-Report/main/Beispielreporting_2022_Securenergy.pdf)


## Funktionen

- Automatische Erstellung von PV-Anlagenberichten
- Verarbeitung von Excel-Dateien mit Anlagendaten
- Generierung von Berichten mit folgenden Inhalten:
  - Titelseite und Inhaltsverzeichnis
  - Anlagendaten und Komponentenübersicht
  - Ertragsanalysen für 2021 und 2022
  - Vergleichsanalysen
  - Auflistung von besonderen Ereignissen
  - Kürzungsanalysen

## Installation

1. Stellen Sie sicher, dass Python 3.x installiert ist
2. Erforderliche Abhängigkeiten installieren:

```bash
pip install pandas numpy pylatex
```

## Verwendung

1. Passen Sie die Pfade in `report.py` entsprechend Ihrer Verzeichnisstruktur an
2. Führen Sie das Hauptskript aus:

```bash
python report.py
```

3. Wählen Sie, ob ein einzelner Bericht oder mehrere Berichte erstellt werden sollen
4. Bei einzelnen Berichten: Wählen Sie die entsprechende Anlagennummer

## Projektstruktur

- `report.py`: Hauptskript zur Berichtserstellung
- `anlagedaten.py`: Verarbeitung der Anlagendaten
- `components.py`: Generierung der Komponentenübersicht
- `comparison.py`: Erstellung von Vergleichsanalysen
- `curtailments.py`: Verarbeitung von Kürzungsdaten
- `events.py`: Verarbeitung besonderer Ereignisse
- `explanation.py`: Erläuterungen und Erklärungen
- `frontpage.py`: Erstellung der Titelseite
- `header.py`: Definition von Kopfzeilen
- `yields21.py`: Ertragsanalysen für 2021
- `yields22.py`: Ertragsanalysen für 2022
- `tableofcontents.py`: Erstellung des Inhaltsverzeichnisses
- Verschiedene Bilddateien für Design-Elemente

## Hinweise

- Die Pfade sind standardmäßig auf den Entwicklungscomputer konfiguriert und müssen angepasst werden
- Ein Beispielbericht (`Beispielreporting_2022_Securenergy.pdf`) ist im Repository enthalten 