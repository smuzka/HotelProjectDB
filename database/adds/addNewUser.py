def add_new_user(cur, name, surname, phone, email):
    try:
        cur.execute("""
                        INSERT INTO uzytkownik (imie, numer_telefonu, nazwisko, email)
                        VALUES ('{name}', '{phone}', '{surname}', '{email}');
                        """.format(name=name, surname=surname, phone=phone, email=email))
    except:
        print("I can't add new user!")
        return 1

