from database_connection import get_database_connection

class InputOutput:
    """I/O-luokka, joka hoitaa keskitetysti tietokannan kirjoitus- ja lukutoiminnot

    Attributes:
        connection: tietokantayhteys, joka haetaan database_connection-moduulista.
        cursor: tietokantayhteyden cursor-olio, ks. sqlite3.Cursor tarkempia tietoja varten.
    """

    def __init__(self):
        self.connection = get_database_connection()
        self.cursor = self.connection.cursor()

    def read(self, query, variables=False):
        """Lukumetodi, lukee tietokantaa.

        Args:
            query: suoritettava tietokantakysely.
            variables: tietokantakyselyn muuttujat, vapaaehtoinen.

        Returns:
            Palauttaa tulokset listana sqliten Row-olioita, tai poikkeuksen sattuessa errorin.
        """

        try:
            with self.connection:
                if variables is False:
                    results = self.connection.execute(query).fetchall()
                else:
                    results = self.connection.execute(query,[variables]).fetchall()

                return results

        except self.connection.Error as error:
            return error

    def write(self, query, values, single=True):
        """Kirjoitusmetodi, joka kirjoittaa tietokantaan.

        Args:
            query: suoritettava tietokantakomentosarja.
            values: komentosarjan muuttujat.
            single: boolean, joka kertoo metodille, suoritetaanko yhden, vai useamman rivin
            kirjoitus tietokantaan. Oletuksena yhden rivin kirjoitus, eli True.

        Returns:
            Palauttaa yhden rivin tapauksessa tietokantarivin saaman id:n. Muuten palauttaa Nonen.
            Virheen sattuessa palauttaa error-olion tapahtuneen virheen mukaan.
        """

        try:
            with self.connection:
                if single:
                    self.cursor.execute(query, values)
                    self.connection.commit()

                    return self.cursor.lastrowid

                if not single:
                    self.cursor.executemany(query, values)
                    self.connection.commit()

                return None

        except self.connection.Error as error:
            return error

    def run_command(self, command):
        """Metodi, jolla voi suorittaa muita tietokantakomentoja, esimerkiksi tyhjentää taulun.

        Args:
            command: suoritettava tietokantakomento.

        Returns:
            Palauttaa joko Nonen merkiksi onnistuneesta suorituksesta, tai error-olion virheestä.
        """

        try:
            with self.connection:
                self.cursor.execute(command)
                self.connection.commit()

            return None

        except self.connection.Error as error:
            return error
