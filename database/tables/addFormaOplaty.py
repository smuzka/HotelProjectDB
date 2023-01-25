def add_forma_oplaty(cur):
    try:
        cur.execute("""
                        INSERT INTO typ_forma_oplaty (nazwa)
                        VALUES ('gotowka');
                        INSERT INTO typ_forma_oplaty (nazwa)
                        VALUES ('przelew');
                        """)
    except:
        print("I can't add new forma oplaty!")
        return 1

