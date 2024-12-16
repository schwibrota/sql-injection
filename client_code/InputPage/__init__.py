from ._anvil_designer import InputPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
import re
import anvil.http
from ..LoggedInPage import LoggedInPage
from anvil.tables import app_tables


class InputPage(InputPageTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    if ("checkboxChecked" in properties):
      if (properties["checkboxChecked"]):
        self.check_box_lvl1.checked = "true"
    if (self.check_box_lvl1.checked != "true"):
      self.level = 1
    if (self.check_box_lvl1.checked == "true"):
      self.level = 2
    
  def button_anmelden_click(self, **event_args):
    if (self.level == 1):
      userdata = anvil.server.call('get_account_information', self.text_box_username.text, self.text_box_pw.text)
      # test input
      sonderzeichen_muster = r"['-]"
      if (self.check_box_sql_inject.checked):
        if (bool(re.search(sonderzeichen_muster, self.text_box_pw.text))):
          anzuzeigendertext = "Hallo, Räuber! Kein Zugriff!"
          pass
        elif (bool(re.search(sonderzeichen_muster, self.text_box_username.text))):
          anzuzeigendertext = "Hallo, Räuber! Kein Zugriff!"
          pass
        else:
          print(f"Userdata: {userdata}")
          anzuzeigendertext = f"Hallo, {userdata[0][1]}! Dein Kontostand beträgt {userdata[0][3]}\nSELECT Users.AccountNo, Users.username, Users.password, Balances.balance FROM Users JOIN Balances ON Users.AccountNo = Balances.AccountNo WHERE Users.username = '{self.text_box_username.text}' AND Users.password = '{self.text_box_pw.text}';"
          pass
      else:
        if (len(userdata) == 1):    
          print(f"Userdata: {userdata}")
          anzuzeigendertext = f"Hallo, {userdata[0][1]}! Dein Kontostand beträgt {userdata[0][3]}\nSELECT Users.AccountNo, Users.username, Users.password, Balances.balance FROM Users JOIN Balances ON Users.AccountNo = Balances.AccountNo WHERE Users.username = '{self.text_box_username.text}' AND Users.password = '{self.text_box_pw.text}';"
          pass
        elif (len(userdata) < 1):
          anzuzeigendertext = f"User nicht vorhanden!\nSELECT Users.AccountNo, Users.username, Users.password, Balances.balance FROM Users JOIN Balances ON Users.AccountNo = Balances.AccountNo WHERE Users.username = '{self.text_box_username.text}' AND Users.password = '{self.text_box_pw.text}';"
        else:
          anzuzeigendertext = f"Logged in, but no AccountNo passed\nSELECT Users.AccountNo, Users.username, Users.password, Balances.balance FROM Users JOIN Balances ON Users.AccountNo = Balances.AccountNo WHERE Users.username = '{self.text_box_username.text}' AND Users.password = '{self.text_box_pw.text}';"
          self.level = 2
          
      loggedIn = LoggedInPage()
      loggedIn.label_ausgabe.text = anzuzeigendertext
      open_form(loggedIn)
      

    elif (self.level == 2):
      userdata = anvil.server.call('get_account_information', self.text_box_username.text, self.text_box_pw.text)
      resp = anvil.http.request(url="",
                    method="GET",
                    headers= {
                      "Authentication": f"{userdata[0]}",
                    })
      print(f"{resp.content_type}: RESPONSE")

      pass
    else:
      pass
    