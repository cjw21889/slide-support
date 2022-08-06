import sqlite3

conn = sqlite3.connect('soccer.sqlite')
# conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute("SELECT * FROM Country WHERE Country.id = 1")

rows = c.fetchone()
print(rows)
