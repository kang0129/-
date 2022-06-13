import bankk

m = bankk.bankmanager()

while True:
    c = m.displaymainmenu()
    if c == 1:
        if m.login():
            while True:
                c2 = m.displaysubmenu()
                if c2 == 1:
                    m.deposit()
                elif c2 == 2:
                    m.withdraw()
                elif c2 == 3:
                    m.query()
                elif c2 == 4:
                    break
                else:
                    print("Wrong input")

        else:
            print("실패")
    elif c == 2:
        m.join()
    elif c == 3:
        break
    else:
        print("Wrong input")
