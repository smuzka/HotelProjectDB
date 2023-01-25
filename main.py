from datetime import date

from database.adds.addNewComplain import addNewComplain
from database.adds.addNewPobyt import add_new_pobyt
from database.adds.addNewRoom import add_new_room
from database.adds.addNewUser import add_new_user
from database.gets.getAllComplains import getAllComplains
from database.gets.getAllGuests import getAllGuests
from database.gets.getAllRooms import getAllRooms
from database.gets.getAllStays import getAllStays
from database.gets.getAllUsers import getAllUsers
from database.gets.getPaymentType import getPaymentType
from database.gets.getRooms import getRooms
from database.gets.getStaysByUser import getStaysByUser
from database.gets.getUserIdByEmail import getUserIdByEmail
from gui.popopGetData import popup_get_date

if __name__ == '__main__':
    import urllib.parse as up
    import psycopg2
    import PySimpleGUI as sg

    url = up.urlparse("pgsql://hbhtvbpi:p12LwoPHyC8_Txa3PFN_w73sxA2xjmZE@mel.db.elephantsql.com/hbhtvbpi")
    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)

    cur = conn.cursor()

    addUser = [[sg.Text('Imię', size=(10, 1)), sg.Input('', key='userName')],
               [sg.Text('Nazwisko', size=(10, 1)), sg.Input('', key='userNazwisko')],
               [sg.Text('Numer Telefonu', size=(10, 1)), sg.Input('', key='userPhone')],
               [sg.Text('Email', size=(10, 1)), sg.Input('', key='userEmail')],
               [sg.Button('Dodaj użytkownika')]]

    addRoom = [[sg.Text('Ilość miejsc', size=(10, 1)), sg.Input('', key='roomSlots')],
               [sg.Text('Dzienny koszt', size=(10, 1)), sg.Input('', key='roomCost')],
               [sg.OptionMenu(values=('podstawowy', 'komfortowy', 'luksusowy'), k='-OPTION MENU-', key='roomType')],
               [sg.Button('Dodaj pokój')]]

    availableRooms = []
    metaRooms = {}
    for room in getRooms(cur):
        availableRooms.append(
            "Ilość miejsc: {beds}, pokój klasy: {type}, dzienny koszt: {cost}".format(beds=room['beds'],
                                                                                      type=room['type'],
                                                                                      cost=room['cost']))
        metaRooms[availableRooms[-1]] = room['id']
    addStay = [[sg.Text('Email użytkownika', size=(15, 1)), sg.Input('', key='stayUser')],
               [sg.Text('Wybierz pokój', size=(15, 1)),
                sg.OptionMenu(availableRooms, s=(60, 2), key='Wybierz pokój'), ],
               [sg.Text('Wybierz formę opłaty', size=(15, 1)),
                sg.OptionMenu(getPaymentType(cur), s=(60, 2), key='Wybierz formę opłaty'), ],
               [sg.Text(
                   'Dodaj gości, których zabierasz ze sobą. (pola opcjonalne) (Twoje dane zostaną uzupełnione automatycznie)')],
               [sg.Text('Gość nr 1')],
               [sg.Text('Imie', size=(10, 1)), sg.Input('', key='stayFirstGuestName')],
               [sg.Text('Nazwisko', size=(10, 1)), sg.Input('', key='stayFirstGuestSurname')],
               [sg.Text('Gość nr 2')],
               [sg.Text('Imie', size=(10, 1)), sg.Input('', key='staySecondGuestName')],
               [sg.Text('Nazwisko', size=(10, 1)), sg.Input('', key='staySecondGuestSurname')],
               [sg.Text('Gość nr 3')],
               [sg.Text('Imie', size=(10, 1)), sg.Input('', key='stayThirdGuestName')],
               [sg.Text('Nazwisko', size=(10, 1)), sg.Input('', key='stayThirdGuestSurname')],
               [sg.Button('Dodaj początek pobytu')],
               [sg.Button('Dodaj koniec pobytu')],
               [sg.Button('Dodaj pobyt')]]

    stays = [None]
    addComplain = [[sg.Text('Email użytkownika', size=(15, 1)), sg.Input('', key='userEmailComplain')],
                   [sg.Button('Wybierz pobyt')],
                   [sg.OptionMenu(stays, s=(60, 2), key='Wybierz pobyt do skargi')],
                   [sg.Text('Tekst skargi', size=(15, 1)), sg.Input('', key='complainText')],
                   [sg.Button('Zlóż skargę')],
                   ]

    usersData = getAllUsers(cur)
    userHeadings = ["uzytkownik_id", "imie", "nazwisko", "numer_telefonu", "email", "Suma wydanych pieniędzy"]
    showUsers = [[sg.Button('Odśwież użytkowników')],
                 [sg.Table(values=usersData[0:][:], headings=userHeadings, max_col_width=25,
                           auto_size_columns=True,
                           display_row_numbers=False,
                           justification='center',
                           num_rows=20,
                           alternating_row_color='lightblue',
                           key='-userTABLE-',
                           selected_row_colors='red on yellow',
                           enable_events=True,
                           expand_x=False,
                           expand_y=True,
                           vertical_scroll_only=False,
                           enable_click_events=True,
                           )]]

    roomsData = getAllRooms(cur)
    roomsHeadings = ["pokoj_id", "typ_pokoju", "typ_pokoju_nazwa", "ilosc_miejsc", "dzienny_koszt"]
    showRooms = [[sg.Button('Odśwież pokoje')],
                 [sg.Table(values=roomsData[0:][:], headings=roomsHeadings, max_col_width=25,
                           auto_size_columns=True,
                           display_row_numbers=False,
                           justification='center',
                           num_rows=20,
                           alternating_row_color='lightblue',
                           key='-roomsTABLE-',
                           selected_row_colors='red on yellow',
                           enable_events=True,
                           expand_x=False,
                           expand_y=True,
                           vertical_scroll_only=False,
                           enable_click_events=True,
                           )]]

    staysData = getAllStays(cur)
    staysHeadings = ["pobyt_id", "data_rozpoczecia", "data_zakonczenia", "pokoj_id", "dzienny_koszt", "ilosc_miejsc",
                     "typ_pokoju.nazwa", "uzytkownik.email", "koszt_pobytu", "typ_oplaty", "zakwaterowanych goosci"]
    showStays = [[sg.Button('Odśwież pobyty')],
                 [sg.Table(values=staysData[0:][:], headings=staysHeadings, max_col_width=25,
                           auto_size_columns=True,
                           display_row_numbers=False,
                           justification='center',
                           num_rows=20,
                           alternating_row_color='lightblue',
                           key='-staysTABLE-',
                           selected_row_colors='red on yellow',
                           enable_events=True,
                           expand_x=False,
                           expand_y=True,
                           vertical_scroll_only=False,
                           enable_click_events=True,
                           )]]

    complainsData = getAllComplains(cur)
    complainsHeadings = ["skarga_id", "tekst", "pobyt_id", "email użytkownika"]
    showComplains = [[sg.Button('Odśwież skargi')],
                     [sg.Table(values=complainsData[0:][:], headings=complainsHeadings, max_col_width=25,
                               auto_size_columns=True,
                               display_row_numbers=False,
                               justification='center',
                               num_rows=20,
                               alternating_row_color='lightblue',
                               key='-complainsTABLE-',
                               selected_row_colors='red on yellow',
                               enable_events=True,
                               expand_x=False,
                               expand_y=True,
                               vertical_scroll_only=False,
                               enable_click_events=True,
                               )]]

    guestsData = getAllGuests(cur)
    guestsHeadings = ["gosc_id", "gosc.imie", "gosc.nazwisko", "pobyt_id", "uzytkownik.email"]
    showGuests = [[sg.Button('Odśwież gości')],
                  [sg.Table(values=guestsData[0:][:], headings=guestsHeadings, max_col_width=25,
                            auto_size_columns=True,
                            display_row_numbers=False,
                            justification='center',
                            num_rows=20,
                            alternating_row_color='lightblue',
                            key='-guestsTABLE-',
                            selected_row_colors='red on yellow',
                            enable_events=True,
                            expand_x=False,
                            expand_y=True,
                            vertical_scroll_only=False,
                            enable_click_events=True,
                            )]]

    tabgrp = [
        [sg.TabGroup(
            [[sg.Tab('Dodaj użytkownika', addUser, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              sg.Tab('Dodaj pokój', addRoom, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              sg.Tab('Dodaj pobyt', addStay, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              sg.Tab('Dodaj skarge', addComplain, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              sg.Tab('Pokaż użytkowników', showUsers, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              sg.Tab('Pokaż pokoje', showRooms, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              sg.Tab('Pokaż pobyty', showStays, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              sg.Tab('Pokaż skargi', showComplains, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              sg.Tab('Pokaż gości', showGuests, title_color='Red', border_width=10, background_color='Green',
                     element_justification='center'),
              ]],
            tab_location='centertop', title_color='Red', tab_background_color='Purple',
            selected_title_color='Green', selected_background_color='Gray', border_width=5), sg.Button('Zamknij')]]

    window = sg.Window("Hotel", tabgrp)

    startingDate = None
    endingDate = None

    while True:  # Event Loop
        event, values = window.Read()
        if event in (None, 'Zamknij'):
            break
        if event == 'Dodaj użytkownika':
            if (values['userName'] == "" or values['userNazwisko'] == "" or values['userPhone'] == "" or values[
                'userEmail'] == ""):
                sg.popup('Uzupełnij wszystkie pola')
            else:
                add_new_user(cur, values['userName'], values['userNazwisko'], values['userPhone'], values['userEmail'])
                conn.commit()
        if event == 'Dodaj pokój':
            if (values['roomSlots'] == "" or values['roomCost'] == "" or values['roomType'] == ""):
                sg.popup('Uzupełnij wszystkie pola')
            else:
                add_new_room(cur, values['roomSlots'], values['roomCost'], values['roomType'])
                conn.commit()
        if event == 'Dodaj pobyt':
            if (values['stayUser'] == "" or startingDate == None or endingDate == None):
                sg.popup('Uzupełnij wszystkie pola')
            else:
                guests = []
                if (values['stayFirstGuestName'] != '' and values['stayFirstGuestSurname']):
                    guests.append([values['stayFirstGuestName'], values['stayFirstGuestSurname']])
                if (values['staySecondGuestName'] != '' and values['staySecondGuestSurname']):
                    guests.append([values['staySecondGuestName'], values['staySecondGuestSurname']])
                if (values['stayThirdGuestName'] != '' and values['stayThirdGuestSurname']):
                    guests.append([values['stayThirdGuestName'], values['stayThirdGuestSurname']])

                try:
                    add_new_pobyt(cur, values['stayUser'], startingDate, startingDatePythonFormat, endingDate,
                                  endingDatePythonFormat, guests,
                                  metaRooms[values['Wybierz pokój']], values['Wybierz formę opłaty'])
                    conn.commit()
                except TypeError:
                    print("Asdasdasdsad")
                    sg.popup('Nie znaleziono uzytkownika o tym emailu')
        if event == 'Dodaj początek pobytu':
            startingDate = popup_get_date()
            startingDatePythonFormat = date(startingDate[2], startingDate[0], startingDate[1])
            try:
                if endingDatePythonFormat:
                    if (endingDatePythonFormat - startingDatePythonFormat).days < 0:
                        sg.popup('Data zakończenia pobytu została podana wcześniejsza niż data rozpoczęcia')
            except:
                sg.popup('Data zakończenia pobytu nie została podana')
            sg.popup('Data rozpoczęcia pobytu: {date}'.format(date=startingDate))
        if event == 'Dodaj koniec pobytu':
            endingDate = popup_get_date()
            endingDatePythonFormat = date(endingDate[2], endingDate[0], endingDate[1])
            try:
                if startingDatePythonFormat:
                    if (endingDatePythonFormat - startingDatePythonFormat).days < 0:
                        print((endingDatePythonFormat - startingDatePythonFormat).days)
                        sg.popup('Data zakończenia pobytu została podana wcześniejsza niż data rozpoczęcia')
            except:
                sg.popup('Data rozpoczęcia pobytu nie została podana')
            sg.popup('Data zakończenia pobytu: {date}'.format(date=endingDate))

        if event == 'Wybierz pobyt':
            if values['userEmailComplain'] != '':
                userIdToComplain = getUserIdByEmail(cur, values['userEmailComplain'])
                if userIdToComplain != None:
                    stays = getStaysByUser(cur, userIdToComplain)
                    staysToPrint = []
                    metaStays = {}
                    for stay in stays:
                        staysToPrint.append(
                            "data rozpoczęcia: {begin}, data zakończenia: {end}, id_pokoju: {roomId}".format(
                                begin=stay[1], end=stay[2], roomId=stay[3]))
                        metaStays[staysToPrint[-1]] = stay[0]
                    window.read(timeout=0)
                    window.find_element('Wybierz pobyt do skargi').update(values=staysToPrint, size=(60, 1))
                    window.read(timeout=0)
        if event == 'Zlóż skargę':
            if values['complainText'] != "":
                addNewComplain(cur, metaStays[values['Wybierz pobyt do skargi']], values['complainText'])
                conn.commit()
        if event == "Odśwież użytkowników":
            window.read(timeout=0)
            window.find_element('-userTABLE-').update(values=getAllUsers(cur)[0:][:])
            window.read(timeout=0)
        if event == "Odśwież pokoje":
            window.read(timeout=0)
            window.find_element('-roomsTABLE-').update(values=getAllRooms(cur)[0:][:])
            window.read(timeout=0)
        if event == "Odśwież pobyty":
            window.read(timeout=0)
            window.find_element('-staysTABLE-').update(values=getAllStays(cur)[0:][:])
            window.read(timeout=0)
        if event == "Odśwież skargi":
            window.read(timeout=0)
            window.find_element('-complainsTABLE-').update(values=getAllComplains(cur)[0:][:])
            window.read(timeout=0)
        if event == "Odśwież gości":
            window.read(timeout=0)
            window.find_element('-guestsTABLE-').update(values=getAllGuests(cur)[0:][:])
            window.read(timeout=0)

    conn.close()
    cur.close()
    window.close()
