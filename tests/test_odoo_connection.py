import pytest
from credencials import OdooConnection, db_ire,url_ire,password_ire,username_ire



def test_odoo_connection():
    conn = OdooConnection(db=db_ire, url=url_ire, username=username_ire, password=password_ire)
    # conn.authenticate()
    assert conn.is_conected == True


try:
    conn = OdooConnection(url='https://edu-tcmc.odoo.com/', db='edu-tcmc', username='enrique.rios@indava.com', password='8f506a004b5c824e68cd771c0213018b6aabaa53')
    print(conn)
except ValueError as e:
    print(e)