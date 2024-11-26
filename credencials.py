import xmlrpc.client

url = 'https://ire-testing-api1.odoo.com/'
db = 'ire-testing-api1'
username = 'enrique.rios@indava.com'
password = 'xmftK$x2yMxN3w*'


# url = 'https://odoo.indava.dev'
# db = 'indava'
# username = 'enrique.rios@indava.com'
# password = 'e8wmaC74l~GU'


def authenticate(url, db, username, password):
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    if uid:
        print("Authenticated UID:", uid)
    else:
        print("Connection failed")
    return uid
