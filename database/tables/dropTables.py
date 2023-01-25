def dropTables(cur):
    cur.execute("""
        DROP TABLE typ_pokoju CASCADE;
        DROP TABLE pokoj CASCADE;
        DROP TABLE pobyt CASCADE;
        DROP TABLE gosc CASCADE;
        DROP TABLE skarga CASCADE;
        DROP TABLE uzytkownik CASCADE;
        DROP TABLE oplata CASCADE;
        DROP TABLE typ_forma_oplaty CASCADE;
                    """)


