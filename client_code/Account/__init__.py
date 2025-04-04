from ._anvil_designer import AccountTemplate
from anvil import *
from .AddSignModal import AddSignModal
from .SettingsModal import SettingsModal


class Account(AccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_new_sign_click(self, **event_args):
    # alert()
    alert(AddSignModal(), large=True)

  def settings_btn_click(self, **event_args):
    alert(SettingsModal(), large=True)

