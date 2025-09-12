def file():
    try:
        file1 = open('sample.txt', 'r')

        count = 1
        for line in file1:
            f = line.strip()
            print("Line ", count, ":", f)
            count = count + 1

        file1.close()

    except:
        print("The file 'sample.txt' was not found.")

r = file()
