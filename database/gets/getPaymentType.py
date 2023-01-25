def getPaymentType(cur):


    cur.execute("""
        SELECT typ_forma_oplaty, nazwa
        FROM typ_forma_oplaty
    """)
    paymentType = []

    try:
        while True:
            buffer = cur.fetchone()
            paymentType.append(buffer[1])
    except:
        pass

    return paymentType