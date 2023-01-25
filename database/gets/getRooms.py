def getRooms(cur):


    cur.execute("""
        SELECT typ_pokoju_id, nazwa
        FROM typ_pokoju
    """)
    roomTypes = {}

    try:
        while True:
            buffer = cur.fetchone()
            roomTypes[buffer[0]] = buffer[1]
    except:
        pass

    cur.execute("""
        SELECT pokoj_id, typ_pokoju_id, ilosc_miejsc, dzienny_koszt
        FROM pokoj
    """)

    rooms = []
    try:
        while True:
            buffer = cur.fetchone()
            myDict = {
                'id': buffer[0],
                'type': roomTypes[buffer[1]],
                'beds': buffer[2],
                'cost': buffer[3],
            }
            rooms.append(myDict)

    except:
        pass


    return rooms