from os import listdir
from os.path import isfile, join

path2dir = "./part"
pathSplit="/"

if __name__ == "__main__":

    books = [f for f in listdir(path2dir) if isfile(pathSplit.join([path2dir, f]))]
    
    books.sort()
    books = [pathSplit.join([path2dir, f]) for f in books]
    print(books)

    with open("./assets/files/inputs.tex", "w", encoding="utf8") as fopt:
        for f in books:
            fopt.write("\\input{" + f + "}"+"\n")
            print("\\input{" + f + "}")
