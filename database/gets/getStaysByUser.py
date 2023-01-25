def getStaysByUser(cur, userId):


    cur.execute("""
        SELECT pobyt_id, data_rozpoczecia, data_zakonczenia, pokoj_id
        FROM pobyt
        WHERE uzytkownik_id = {userId}
    """.format(userId=userId))
    stays = []

    try:
        while True:
            buffer = cur.fetchone()
            stays.append([buffer[0], buffer[1], buffer[2], buffer[3]])
    except:
        pass




    return stays