import xmlrpc.client

class OdooConnection:
    def __init__(self, url, db, username, password):
        """
        Initialize a connection to an Odoo server.

        Args:
            url (str): URL of the Odoo server.
            db (str): Name of the database to connect to.
            username (str): Username for authentication.
            password (str): Password for the username.

        Returns:
            None
        """

        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.uid = None
        self.models = None
        self.is_conected = None
        self.authenticate()

    # Authentication method for the Odoo server

    def authenticate(self):
        try:
            common = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/common',allow_none=True)
            self.uid = common.authenticate(self.db, self.username, self.password, {})
            if self.uid:
                print(f"Autenticado correctamente. UID: {self.uid}")
                self.models = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/object')
                self.is_conected = True
            else:
                print("Fallo en la autenticación")
                self.is_conected = False
                raise ConnectionError("No se pudo autenticar con el servidor Odoo")       
        except Exception as e:
            print(f"Error durante la autenticación: {str(e)}")
            self.is_conected = False
            raise

    def calling_method(self,model, method, data):
        """
        Call a method from the Odoo server.

        Args:
            method (str): The method to call.
                Calling methods:
                    list - Returns a list of records based on the applied filters.  
                    search_count - Counts the number of records that match the filters.  
                    search - Reads the data of one or more records by their IDs.  
                    fields_get - Returns the available fields of a model and their properties.  
                    search_read - Searches for records that meet certain conditions and returns their IDs.  
                    create - Creates a new record with the provided data.  
                    write - Updates one or more records with the specified data.  
                    unlink - Deletes one or more records by their IDs.
            *args: The arguments to pass to the method.
        """
        if not self.is_conected:
            print("No se puede llamar a un método sin conexión")
            return False
        try:
        # Call the Odoo method via XML-RPC execute_kw
            return getattr(self.models, 'execute_kw')(
                self.db,
                self.uid,
                self.password,
                model,
                method,
                data
            )
        except Exception as e:
            print(f"Error al llamar al método {method}: {str(e)}")
            return False
        
    def __str__(self):
        return f"Conexión a {self.url} - Base de datos: {self.db} - Usuario: {self.username}"
    
    def close(self):
        """Limpia los recursos de la conexión"""
        self.uid = None
        self.models = None
        self.is_conected = False
        print("Conexión cerrada")
        return True


