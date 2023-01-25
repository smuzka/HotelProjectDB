def staysView(cur):
    cur.execute("""
        CREATE VIEW GuestsFullView AS
                SELECT gosc_id,
                        gosc.imie,
                        gosc.nazwisko,
                        gosc.pobyt_id,
                        uzytkownik.email
        FROM gosc
        JOIN pobyt ON gosc.pobyt_id = pobyt.pobyt_id
        JOIN uzytkownik ON pobyt.uzytkownik_id = uzytkownik.uzytkownik_id;

    """)