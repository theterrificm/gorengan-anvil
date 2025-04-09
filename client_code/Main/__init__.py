from ._anvil_designer import MainTemplate
from anvil import *
from ..Contact import Contact
from ..Account import Account
from ..Pricing import Pricing
from ..Login import Login
from ..Home import Home
from ..FAQs import FAQs


forms_to_change = {
  'Contact Us': Contact(),
  'Upgrade': Pricing(),
  'Account': Account(),
  'Login': Login(),
  'Home': Home(),
  'FAQs': FAQs(),
}

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def change_content_panel(self, form_to_change):
    self.content_panel_section.clear()
    self.content_panel_section.add_component(forms_to_change[form_to_change], full_width_row=True)
