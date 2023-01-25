def add_new_room(cur, slots, cost, type):
    if(type == 'podstawowy'):
        finalType = 1
    elif(type == 'komfortowy'):
        finalType = 2
    else:
        finalType = 3

    try:
        cur.execute("""
                        INSERT INTO pokoj (typ_pokoju_id, ilosc_miejsc, dzienny_koszt)
                        VALUES ({finalType}, {slots}, {cost});
                        """.format(finalType=finalType, slots=slots, cost=cost))
    except:
        print("I can't add new room!")
        return 1

