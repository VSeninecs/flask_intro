FILE_NAME = "DATA.txt"

def pievienot(rindina):
    f = open(FILE_NAME, "a", encoding="utf-8")
    print(len(rindina))
    for rinda in rindina:
        f.write(rinda + "\n")

    f.write("Ziņas beigas" + "\n")
    f.close()
