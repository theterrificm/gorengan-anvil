from ._anvil_designer import MainNewTemplate
from anvil import *


class MainNew(MainNewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def change_content_panel(self, formToChange):
    print('formToChange')
