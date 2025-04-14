from ._anvil_designer import RowTemplate1Template
from anvil import *
from ..EditSignModal import EditSignModal


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def edit_sign_btn_click(self, **event_args):
    alert(EditSignModal(), buttons=None, large=True)
