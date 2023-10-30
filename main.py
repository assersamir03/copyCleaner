import os


def main():
    names = []
    try:
        Dir = input("enter the directory: ")
        for i in os.listdir(Dir):
            names += [i]
    except:
        print(f"there is no such directory as {Dir} ")
        main()
    names = list(filter(lambda i: "- Copy" in i, names))
    if not names:
        print("there is no copies to delete XD")
        main()
    areYouSure = input("Are you sure you want to delete y/n: ").lower()
    if areYouSure == 'y':
        for i in os.listdir(Dir):
            if i in names:
                os.remove(f"{Dir}\\{i}")
    elif areYouSure == 'n':
        print("k have a nice day <3")
        exit()
    main()


main()
