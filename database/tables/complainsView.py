def staysView(cur):
    cur.execute("""
        CREATE VIEW ComplainsFullView AS
                SELECT skarga_id,
                        tekst,
                        pobyt.pobyt_id,
                        email
        FROM skarga
        JOIN pobyt ON skarga.pobyt_id = pobyt.pobyt_id
        JOIN uzytkownik ON pobyt.uzytkownik_id = uzytkownik.uzytkownik_id;

    """)