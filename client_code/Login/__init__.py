from ._anvil_designer import LoginTemplate
from anvil import *


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
  def contact_us_link_click(self, **event_args):
    open_form('Contact')

  def upgrade_page_link_click(self, **event_args):
    open_form('Pricing')

  def account_page_link_click(self, **event_args):
    open_form('Account')

  def login_page_link_click(self, **event_args):
    open_form('Login')

  def link_1_click(self, **event_args):
    open_form('Homepage')
