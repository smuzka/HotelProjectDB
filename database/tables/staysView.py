def staysView(cur):

    cur.execute("""
        CREATE VIEW StaysFullView AS
                SELECT pobyt.pobyt_id, 
                data_rozpoczecia, 
                data_zakonczenia,
                pobyt.pokoj_id, 
                pokoj.dzienny_koszt,
                pokoj.ilosc_miejsc,
                typ_pokoju.nazwa as pokojNazwa,
                uzytkownik.email,
                oplata.koszt_pobytu,
                typ_forma_oplaty.nazwa,
                COUNT(gosc_id)
        FROM uzytkownik
        JOIN pobyt ON uzytkownik.uzytkownik_id = pobyt.uzytkownik_id
        JOIN pokoj ON pobyt.pokoj_id = pokoj.pokoj_id
        JOIN typ_pokoju ON pokoj.typ_pokoju_id = typ_pokoju.typ_pokoju_id
        JOIN oplata ON pobyt.pobyt_id = oplata.pobyt_id
        JOIN typ_forma_oplaty ON oplata.typ_forma_oplaty = typ_forma_oplaty.typ_forma_oplaty
        LEFT JOIN gosc ON pobyt.pobyt_id = gosc.pobyt_id
        GROUP BY pobyt.pobyt_id, 
                data_rozpoczecia, 
                data_zakonczenia,
                pobyt.pokoj_id, 
                pokoj.dzienny_koszt,
                pokoj.ilosc_miejsc,
                pokojNazwa,
                uzytkownik.email,
                oplata.koszt_pobytu,
                typ_forma_oplaty.nazwa;
        
    """)