def getAllComplains(cur):

    cur.execute("""
            SELECT * 
            FROM ComplainsFullView;
    """)
    complains = []

    try:
        while True:
            buffer = cur.fetchone()
            complains.append([buffer[0], buffer[1], buffer[2], buffer[3]])
    except:
        pass

    return complains