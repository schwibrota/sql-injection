from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_anmelden_click(self, **event_args):
    userdata = anvil.server.call('get_account_information', self.text_box_username.text, self.text_box_pw.text)
    print(f"Userdata: {userdata}")
    self.label_ergebnis.text = f"Hallo, {userdata[0][1]}! Dein Kontostand beträgt {userdata[0][3]}"
    pass

