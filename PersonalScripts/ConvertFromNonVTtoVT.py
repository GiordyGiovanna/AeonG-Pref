import sys

def main(file : str):
    res = []
    res2 = []
    try:
        with open(file, "r") as f:
            content = f.read()
        dati = ["\"-INF\"", "\"1980-01-01T00:00:00\"", "\"1984-07-01T00:00:00\"", "\"1989-01-01T00:00:00\"", "\"1993-07-01T00:00:00\"", "\"1998-01-01T00:00:00\"", "\"2002-07-01T00:00:00\"", "\"2007-01-01T00:00:00\"", "\"2011-07-01T00:00:00\"", "\"2016-01-01T00:00:00\"", "\"2020-07-01T00:00:00\""]
        dati2 = ["\"1980-01-01T00:00:00\"", "\"1984-07-01T00:00:00\"", "\"1989-01-01T00:00:00\"", "\"1993-07-01T00:00:00\"", "\"1998-01-01T00:00:00\"", "\"2002-07-01T00:00:00\"", "\"2007-01-01T00:00:00\"", "\"2011-07-01T00:00:00\"", "\"2016-01-01T00:00:00\"", "\"2020-07-01T00:00:00\"", "\"+INF\""]

        for l, i in zip(content.split("\n"), range(20000000000000000000000)):
            if(l.startswith("CREATE")):
                res.append(l.replace(";", f" FOR VT FROM {dati[i % 10]} TO {dati2[i % 10]};\n"))
            else:
                res2.append(l + "\n")
       
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with open("indexNewVertex.Cypher", "w") as newFile:
            newFile.write(''.join(res))
        with open("indexNewEdges.Cypher", "w") as newFile:
            newFile.write(''.join(res2))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fileName = sys.argv[1]  # First argument after script name
    else:
        fileName = "./index.cypher"
    print(f"Correcting: {fileName}!")

    main(fileName)
    print(f"Created: ./indexNew.Cypher!")