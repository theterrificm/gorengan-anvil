from ._anvil_designer import AccountTemplate
from anvil import *


class Account(AccountTemplate):
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

