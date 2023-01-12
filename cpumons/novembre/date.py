def verif(d):
    date = d.split("/")

    if date[0] <= "31" and date[1] <= "12":
        dt = date[0] + date[1] + date[2]
        if dt <= "08112022":
            print("Date valide")
        else:
            print('Vous ne pouvez pas être né dans le futur')
    else:
        print("Date invalide")


verif("09/11/2023")
