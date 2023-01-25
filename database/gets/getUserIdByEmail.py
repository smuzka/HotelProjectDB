def getUserIdByEmail(cur, userEmail):


    cur.execute("""
        SELECT uzytkownik_id
        FROM uzytkownik
        WHERE email LIKE '{userEmail}'
    """.format(userEmail=userEmail))

    try:
        return cur.fetchone()[0]
    except:
        pass




