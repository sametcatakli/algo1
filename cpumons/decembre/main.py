def dif(p1, p2):
    res = []
    for i in range(len(p1)):
        if i <= len(p2):
            if p1[i] != p2[i]:
                res.append((i, p1[i], p2[i]))
    if not res:
        print("Identique")
    else:
        print(res)


str1 = "je suis une longue phrase qui n’a aucun sens"
str2 = "je suis une longue phrose qii n’a aucun senz"
dif(str1, str2)
