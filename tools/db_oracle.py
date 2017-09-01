'''
Created on 2017年7月18日

@author: wei.wang7

1. set up environment variable: 
ORACLE_HOME E:\Program Files\instantclient_11_1
2. add to PATH environment variable:
E:\Program Files\instantclient_11_1
3. download cx_Oracle: https://pypi.python.org/pypi/cx_Oracle/5.3, then install
'''

import cx_Oracle

#con=cx_Oracle.connect(user='yffb', password='ccddbb', dsn='10.71.79.244:57777/pboc')
dsn_tns=cx_Oracle.makedsn('10.71.79.244', '57777', 'pboc')
conn=cx_Oracle.connect(user='yffb', password='ccddbb', dsn=dsn_tns)

print(conn.version)

cursor=conn.cursor()
cursor.execute('select asn from tbl_card where card_status=7 and cardstore_status=2 and storelocation_id=100241')
row=cursor.fetchall()
for x in row:
    print(x)
    
cursor.close()
conn.close()
