def add_new_pobyt(cur, userEmail, startingDate, startingDateFormated, endingDate, endingDateFormated, guests, roomId, paymentType):
    paymentTypeId = 1
    if paymentType == 'gotowka':
        paymentTypeId = 1
    elif paymentType == 'przelew':
        paymentTypeId = 2

    stayDays = (endingDateFormated - startingDateFormated).days
    print(stayDays)

    formatedStartingDate = "{year}-{month}-{day}".format(year=startingDate[2], month=startingDate[0],
                                                         day=startingDate[1])
    formatedEndingDate = "{year}-{month}-{day}".format(year=endingDate[2], month=endingDate[0], day=endingDate[1])

    # gets user id
    cur.execute("""
        SELECT uzytkownik_id
        FROM uzytkownik
        WHERE uzytkownik.email LIKE '{email}'
    """.format(email=userEmail))
    userId = cur.fetchone()[0]

    # check if room is taken during selected days
    cur.execute("""
        SELECT pobyt_id
        FROM pobyt
        WHERE data_rozpoczecia = '{formatedStartingDate}' AND
                data_zakonczenia = '{formatedEndingDate}' AND
                pokoj_id = '{roomId}';
    """.format(formatedStartingDate=formatedStartingDate, formatedEndingDate=formatedEndingDate, roomId=roomId))

    try:
        pobytId = cur.fetchone()[0]
    except:
        cur.execute("""
            INSERT INTO pobyt (data_rozpoczecia, data_zakonczenia, pokoj_id, uzytkownik_id)
            VALUES ('{formatedStartingDate}', '{formatedEndingDate}', '{roomId}', {userId})

        """.format(formatedStartingDate=formatedStartingDate, formatedEndingDate=formatedEndingDate, roomId=roomId,
                   userId=userId))

        cur.execute("""
                    SELECT pobyt_id 
                    FROM pobyt
                    ORDER BY pobyt_id DESC
                    LIMIT 1;
                """)
        stayId = cur.fetchone()[0]

        # gets daily cost of the room
        cur.execute("""
                    SELECT dzienny_koszt
                    FROM pokoj
                    WHERE pokoj_id = {roomId}
                """.format(roomId=roomId))
        dailyCost = cur.fetchone()[0]

        # adds payment coresponding to stay
        cur.execute("""
            INSERT INTO oplata (typ_forma_oplaty, pobyt_id, koszt_pobytu)
            VALUES ({paymentTypeId}, {stayId}, {cost})
        """.format(paymentTypeId=paymentTypeId, stayId=stayId, cost=dailyCost*stayDays))

        # adds guests
        for guest in guests:
            cur.execute("""
                INSERT INTO gosc (pobyt_id, imie, nazwisko)
                VALUES ({stayId}, '{name}', '{surname}')
            """.format(stayId=stayId, name=guest[0], surname=guest[1]))
