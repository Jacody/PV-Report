from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, \
    MediumText, LineBreak, simple_page_number, Figure
from pylatex.utils import bold
import os
from pylatex import Command, StandAloneGraphic
from pylatex.utils import bold, NoEscape

def generate_header(doc):
    # Bilder importieren

    #print(os.path.dirname(__file__))
    image_filename = os.path.join(os.path.dirname(__file__), 'firmenlogogrey.jpg')

    # Add document header
    header = PageStyle("header")

# Create left header
    with header.create(Head("C")) as header_center:
        with header_center.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                           pos='c', align="c")) as logo_wrapper:
            logo_file = os.path.join(os.path.dirname(__file__),
                                     'firmenlogo.jpg')
            logo_wrapper.append(StandAloneGraphic(image_options="width=120px",
                                                  filename=logo_file))

    # Create center header
    with header.create(Head("L")):
        header.append(Command('scriptsize'))
        header.append(Command('color', 'Black'))
        header.append("JAHRESREPORT 21/22")
        header.append(LineBreak())
        header.append("Portfolio SeCon 11")

    # Create right header
    with header.create(Head("R")):
        header.append(Command('scriptsize'))
        header.append(Command('color', 'Black'))
        header.append(bold("secur"))
        header.append("energy GmbH")
        header.append(LineBreak())
        header.append("monitoring@securenergy.de")
        header.append(LineBreak())
        header.append(" +49 30 868 00 10 70")

    # Create right footer
    with header.create(Foot("C")):
        header.append(NoEscape(r' \thepage\  '))

    doc.preamble.append(header)
    doc.change_document_style("header")

    # Add Heading
    with doc.create(MiniPage(align='c')):
        doc.append(LargeText(bold(" ")))
        doc.append(LineBreak())
        doc.append(MediumText(bold(" ")))


