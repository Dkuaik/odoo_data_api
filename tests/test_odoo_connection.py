import pytest
from credencials import OdooConnection, db_ire,url_ire,password_ire,username_ire



def test_odoo_connection(db_ire,url_ire,username_ire,password_ire):
    conn = OdooConnection(db=db_ire, url=url_ire, username=username_ire, password=password_ire)
    # conn.authenticate()
    assert conn.is_conected == True


try:
    conn = OdooConnection(url=url_ire, 
                          db=db_ire, 
                          username=username_ire, 
                          password=password_ire)
    print(conn)
except ValueError as e:
    print(e)