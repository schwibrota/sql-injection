from ._anvil_designer import LoggedInPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LoggedInPage(LoggedInPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def button_back_click(self, **event_args):
    
    if (self.label_ausgabe.text == "Logged in, but no AccountNo passed"):
      open_form("InputPage", checkboxChecked=True)
    else:
      open_form("InputPage", checkboxChecked=False)
    pass