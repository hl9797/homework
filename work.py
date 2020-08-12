def multiple_table():
    i = 1
    j = 1
    c = 0
    while i <= 9:
        j = 1
        while j <= i:
            c = i * j
            print("%d*%d=%d" % (j, i, c), end="\t")
            j = j + 1
        print("")
        i = i + 1


multiple_table()