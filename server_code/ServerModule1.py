import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

@anvil.server.callable
def get_account_information(username, password):
  conn = sqlite3.connect(data_files['sqlinject.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT username, AccountNo FROM Users WHERE username = '{username}' AND password = '{password}'"))
  conn.close()
  print(res)
  return res