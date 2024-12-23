from ._anvil_designer import InitPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..InputPage import InputPage

class InitPage(InitPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    open_form('InputPage')
    # Any code you write here will run before the form opens.
