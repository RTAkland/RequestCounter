import base64
from PIL import Image
import os
import sqlite3


conn = sqlite3.connect('../assets/theme.db')
cursor = conn.cursor()

file_list = os.listdir('../assets/themes/')
for i in file_list:
    img = Image.open(f'../assets/themes/{i}/0.gif')
    w = img.width
    h = img.height
    img.close()
    for n in range(0, 10):
        with open(f'../assets/themes/{i}/{n}.gif', 'rb') as f:
            base64_data = base64.b64encode(f.read())
            base64_code = f'data:image/gif;base64,' + base64_data.decode('utf-8')

            try:
                cursor.execute('insert into %(name)s values(?, ?, ?, ?)' % {'name': i}, (n, base64_code, w, h))
                conn.commit()
            except Exception:
                cursor.execute('create table %(name)s (k text, v text, w integer, h integer)' % {'name': i})