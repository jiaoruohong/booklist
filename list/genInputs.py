from os import listdir
from os.path import isfile, join

path2dir = "./part"

if __name__ == "__main__":

    books = [f for f in listdir(path2dir) if isfile(join(path2dir, f))]

    books.sort()
    books = [join(path2dir, f) for f in books]

    with open("./assets/files/inputs.tex", "w") as fopt:
        for f in books:
            fopt.write("\\input{" + f + "}"+"\n")
            print("\\input{" + f + "}")
