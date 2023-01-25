def getAllRooms(cur):

    cur.execute("""
        SELECT pokoj_id, pokoj.typ_pokoju_id, typ_pokoju.nazwa, ilosc_miejsc, dzienny_koszt
        FROM pokoj
        JOIN typ_pokoju ON pokoj.typ_pokoju_id = typ_pokoju.typ_pokoju_id
    """)
    rooms = []

    try:
        while True:
            buffer = cur.fetchone()
            rooms.append([buffer[0], buffer[1], buffer[2], buffer[3], buffer[4]])
    except:
        pass

    return rooms