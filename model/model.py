from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        lista_automobili = []
        cnx = get_connection()
        cursor  = cnx.cursor(dictionary=True)
        query_read = """SELECT * FROM automobile"""
        cursor.execute(query_read)
        for row in cursor:
            auto = Automobile(row["codice"],row["marca"],row["modello"],row["anno"],row["posti"],row["disponibile"])
            lista_automobili.append(auto)
        cursor.close()
        cnx.close()
        return lista_automobili
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        lista_automobili2 = []
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query_read = """SELECT * FROM automobile WHERE modello LIKE %s"""
        cursor.execute(query_read,(f"%{modello}%",))
        for row in cursor:
            auto = Automobile(row["codice"], row["marca"], row["modello"], row["anno"], row["posti"],row["disponibile"])
            lista_automobili2.append(auto)
        cursor.close()
        cnx.close()
        return lista_automobili2

        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """