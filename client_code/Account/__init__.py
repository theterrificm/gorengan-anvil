from ._anvil_designer import AccountTemplate
from anvil import *
from .AddSignModal import AddSignModal
from .SettingsModal import SettingsModal


data = [
        {"id": 1, "name": "John Doe", "email": "john.doe@example.com", },
        {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", },
        {"id": 3, "name": "Alice Johnson", "email": "alice.johnson@example.com",},
      ]

class Account(AccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = data
    # Any code you write here will run before the form opens.

  def add_new_sign_click(self, **event_args):
    # alert()
    alert(AddSignModal(), large=True, buttons=None)

  def settings_btn_click(self, **event_args):
    alert(SettingsModal(), large=True)

