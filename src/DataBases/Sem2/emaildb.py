import sqlite3
conn = sqlite3.connect('orgsdb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (orgs TEXT, count INTEGER)''')
fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    orgs = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE orgs = ? ', (orgs,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (orgs, count)
                VALUES (?, 1)''', (orgs,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE orgs = ?',
                    (orgs,))
# https://www.sqlite.org/lang_select.html
conn.commit()
sqlstr = 'SELECT orgs, count FROM Counts ORDER BY count DESC LIMIT 10'
suma = 0
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    suma += int(row[1])
print(suma)
cur.close()
