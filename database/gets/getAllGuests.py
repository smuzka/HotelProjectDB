def getAllGuests(cur):

    cur.execute("""
            SELECT * 
            FROM GuestsFullView ;
    """)
    guests = []

    try:
        while True:
            buffer = cur.fetchone()
            guests.append([buffer[0], buffer[1], buffer[2], buffer[3], buffer[4]])
    except:
        pass

    return guests