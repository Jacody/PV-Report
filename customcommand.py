from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex import Document, Section, UnsafeCommand
from pylatex.utils import NoEscape



class ExampleCommand(CommandBase):
    """
    A class representing a custom LaTeX command.

   This class represents a custom LaTeX command named
    ``exampleCommand``.
    """

    _latex_name = 'addcontentsline'
