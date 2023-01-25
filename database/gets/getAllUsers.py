def getAllUsers(cur):


    cur.execute("""
        SELECT uzytkownik.uzytkownik_id, imie, nazwisko, numer_telefonu, email, SUM(oplata.koszt_pobytu)
        FROM uzytkownik
        LEFT JOIN pobyt ON uzytkownik.uzytkownik_id = pobyt.uzytkownik_id
        LEFT JOIN oplata ON pobyt.pobyt_id = oplata.pobyt_id
        GROUP BY uzytkownik.uzytkownik_id, imie, nazwisko, numer_telefonu, email
    """)
    users = []

    try:
        while True:
            buffer = cur.fetchone()
            users.append([buffer[0], buffer[1], buffer[2], buffer[3], buffer[4], buffer[5]])
    except:
        pass

    return users