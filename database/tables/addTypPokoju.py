def add_typ_pokoju(cur):
    try:
        cur.execute("""
                        INSERT INTO typ_pokoju (nazwa)
                        VALUES ('podstawowy');
                        INSERT INTO typ_pokoju (nazwa)
                        VALUES ('komfortowy');
                        INSERT INTO typ_pokoju (nazwa)
                        VALUES ('luksusowy');
                        """)
    except:
        print("I can't add new typ pokoju!")
        return 1

