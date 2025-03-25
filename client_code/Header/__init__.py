from ._anvil_designer import HeaderTemplate
from anvil import *


class Header(HeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def contact_us_link_click(self, **event_args):
    self.parent.contact_us_clicked()
    
