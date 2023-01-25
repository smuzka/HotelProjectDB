def create_typ_forma_oplaty(cur):
    try:
        cur.execute("""CREATE TABLE typ_forma_oplaty (
                    typ_forma_oplaty serial NOT NULL,
                    nazwa VARCHAR(30) NOT NULL,
                    CONSTRAINT typ_forma_oplaty_id PRIMARY KEY (typ_forma_oplaty)
                    );""")
    except:
        print("I can't create table: typ_forma_oplaty!")
        return 1


def create_typ_pokoju(cur):
    try:
        cur.execute("""CREATE TABLE typ_pokoju (
                    typ_pokoju_id serial NOT NULL,
                    nazwa VARCHAR(30) NOT NULL,
                    CONSTRAINT typ_pokoju_id PRIMARY KEY (typ_pokoju_id)
                    );""")
    except:
        print("I can't create table: typ_pokoju!")
        return 1

def create_uzytkownik(cur):
    try:
        cur.execute("""CREATE TABLE uzytkownik (
                    uzytkownik_id serial NOT NULL,
                    imie VARCHAR(30) NOT NULL,
                    numer_telefonu VARCHAR(9) NOT NULL,
                    nazwisko VARCHAR(30) NOT NULL,
                    email VARCHAR(30) NOT NULL,
                    CONSTRAINT uzytkownik_id PRIMARY KEY (uzytkownik_id)
                    );""")

        cur.execute("""
                ALTER TABLE uzytkownik
                ADD UNIQUE (email);
                """)
    except:
        print("I can't create table: uzytkownik!")
        return 1

def create_pokoj(cur):
    try:
        cur.execute("""CREATE TABLE pokoj (
                    pokoj_id serial NOT NULL UNIQUE,
                    typ_pokoju_id INTEGER NOT NULL,
                    ilosc_miejsc INTEGER NOT NULL,
                    dzienny_koszt INTEGER NOT NULL,
                    CONSTRAINT pokoj_id PRIMARY KEY (pokoj_id, typ_pokoju_id)
                    );""")
    except:
        print("I can't create table: pokoj!")
        return 1

def create_pobyt(cur):
    try:
        cur.execute("""CREATE TABLE pobyt (
                    pobyt_id serial NOT NULL,
                    data_rozpoczecia DATE NOT NULL,
                    data_zakonczenia DATE NOT NULL,
                    pokoj_id INTEGER NOT NULL,
                    uzytkownik_id INTEGER NOT NULL,
                    CONSTRAINT pobyt_id PRIMARY KEY (pobyt_id)
                    );""")
    except:
        print("I can't create table: pobyt!")
        return 1

def create_skarga(cur):
    try:
        cur.execute("""CREATE TABLE skarga (
                    skarga_id serial NOT NULL,
                    pobyt_id INTEGER NOT NULL,
                    tekst VARCHAR(200) NOT NULL,
                    CONSTRAINT skarga_id PRIMARY KEY (skarga_id, pobyt_id)
                    );""")
    except:
        print("I can't create table: skarga!")
        return 1

def create_gosc(cur):
    try:
        cur.execute("""CREATE TABLE gosc (
                    gosc_id serial NOT NULL,
                    pobyt_id INTEGER NOT NULL,
                    Imie VARCHAR(30) NOT NULL,
                    nazwisko VARCHAR(30) NOT NULL,
                    CONSTRAINT gosc_id PRIMARY KEY (gosc_id, pobyt_id)
                    );""")
    except:
        print("I can't create table: gosc!")
        return 1


def create_oplata(cur):
    try:
        cur.execute("""CREATE TABLE oplata (
                oplata_id serial NOT NULL,
                typ_forma_oplaty INTEGER NOT NULL,
                pobyt_id INTEGER NOT NULL,
                koszt_pobytu INTEGER NOT NULL,
                CONSTRAINT oplata_id PRIMARY KEY (oplata_id, typ_forma_oplaty)
                );""")
    except:
        print("I can't create table: oplata!")
        return 1

def alter_oplata(cur):
    try:
        cur.execute("""ALTER TABLE oplata ADD CONSTRAINT typ_forma_oplaty_oplata_fk
                        FOREIGN KEY (typ_forma_oplaty)
                        REFERENCES typ_forma_oplaty (typ_forma_oplaty)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        NOT DEFERRABLE;
                        """)
    except:
        print("I can't alter table: oplata1!")
        return 1

def alter_pokoj(cur):
    try:
        cur.execute("""ALTER TABLE pokoj ADD CONSTRAINT typ_pokoju_pokoj_fk
                        FOREIGN KEY (typ_pokoju_id)
                        REFERENCES typ_pokoju (typ_pokoju_id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        NOT DEFERRABLE;
                        """)
    except:
        print("I can't alter table: pokoj!")
        return 1

def alter_pobyt(cur):
    try:
        cur.execute("""ALTER TABLE pobyt ADD CONSTRAINT gosc_pobyt_fk
                        FOREIGN KEY (uzytkownik_id)
                        REFERENCES uzytkownik (uzytkownik_id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        NOT DEFERRABLE;
                        """)
    except:
        print("I can't alter table: pobyt!")
        return 1

def alter_pobyt2(cur):
    try:
        cur.execute("""ALTER TABLE pobyt ADD CONSTRAINT pokoj_pobyt_fk
                        FOREIGN KEY (pokoj_id)
                        REFERENCES pokoj (pokoj_id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        NOT DEFERRABLE;
                        """)
    except:
        print("I can't alter table: pobyt!")
        return 1

def alter_oplata2(cur):
    try:
        cur.execute("""ALTER TABLE oplata ADD CONSTRAINT pobyt_oplata_fk
                        FOREIGN KEY (pobyt_id)
                        REFERENCES pobyt (pobyt_id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        NOT DEFERRABLE;
                        """)
    except:
        print("I can't alter table: oplata2!")
        return 1

def alter_gosc(cur):
    try:
        cur.execute("""ALTER TABLE gosc ADD CONSTRAINT pobyt_gosc_fk
                        FOREIGN KEY (pobyt_id)
                        REFERENCES pobyt (pobyt_id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        NOT DEFERRABLE;
                        """)
    except:
        print("I can't alter table: gosc!")
        return 1

def alter_skarga(cur):
    try:
        cur.execute("""ALTER TABLE skarga ADD CONSTRAINT pobyt_skarga_fk
                        FOREIGN KEY (pobyt_id)
                        REFERENCES pobyt (pobyt_id)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        NOT DEFERRABLE;
                        """)
    except:
        print("I can't alter table: skarga!")
        return 1




def create_tables(cur):

    create_typ_forma_oplaty(cur)
    create_typ_pokoju(cur)
    create_uzytkownik(cur)
    create_pokoj(cur)
    create_pobyt(cur)
    create_skarga(cur)
    create_gosc(cur)
    create_oplata(cur)
    alter_oplata(cur)
    alter_pokoj(cur)
    alter_pobyt(cur)
    alter_pobyt2(cur)
    alter_oplata2(cur)
    alter_gosc(cur)
    alter_skarga(cur)

    from database.tables.addTypPokoju import add_typ_pokoju
    from database.tables.addFormaOplaty import add_forma_oplaty
    add_typ_pokoju(cur)
    add_forma_oplaty(cur)
