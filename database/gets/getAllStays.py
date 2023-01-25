def getAllStays(cur):

    cur.execute("""
            SELECT * 
            FROM StaysFullView;
    """)
    stays = []

    try:
        while True:
            buffer = cur.fetchone()
            stays.append([buffer[0], buffer[1], buffer[2], buffer[3], buffer[4], buffer[5], buffer[6], buffer[7], buffer[8], buffer[9], buffer[10]+1])
    except:
        pass

    return stays