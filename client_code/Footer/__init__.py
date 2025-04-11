from ._anvil_designer import FooterTemplate
from anvil import *
from ..PrivacyPolicy import PrivacyPolicy


class Footer(FooterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def nav_link_click(self, **event_args):
    form_to_update = event_args['sender'].text if event_args['sender'].text != '' else 'Home'
    self.parent.parent.change_content_panel(form_to_update)

  def link_3_click(self, **event_args):
    alert(PrivacyPolicy(), large=True, buttons=None)
