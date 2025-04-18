from ._anvil_designer import HeaderTemplate
from anvil import *


class Header(HeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def nav_link_click(self, **event_args):
    form_to_update = event_args['sender'].text if event_args['sender'].text != '' else 'Home'
    self.parent.parent.change_content_panel(form_to_update)
