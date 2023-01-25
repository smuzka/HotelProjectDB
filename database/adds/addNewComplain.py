def addNewComplain(cur, stayId, text):

    try:
        cur.execute("""
                        INSERT INTO skarga (pobyt_id, tekst)
                        VALUES ({stayId}, '{text}');
                        """.format(stayId=stayId, text=text))
    except:
        print("I can't add new complain!")
        return 1

