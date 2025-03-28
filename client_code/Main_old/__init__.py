from ._anvil_designer import Main_oldTemplate
from anvil import *


class Main_old(Main_oldTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
