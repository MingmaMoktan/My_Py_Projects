import json

lib_data = []

def ld_lib():
    global lib_data
    try:
        with open('./resources/library.json', 'r') as fl:
            lib_data = json.load(fl)
    except FileNotFoundError:
        lib_data = []

def sv_lib():
    with open('./resources/library.json', 'w') as fl:
        json.dump(lib_data, fl, indent=4)

def sh_bks():
    if not lib_data:
        print("Library empty.")
    else:
        for bk in lib_data:
            print(f"Title: {bk['title']}, Writer: {bk['author']}")

def ad_bk():
    t = input("Book title: ")
    a = input("Writer name: ")
    lib_data.append({'title': t, 'author': a})
    print("Book added.")

def dl_bk():
    t = input("Book title to remove: ")
    global lib_data
    lib_data = [bk for bk in lib_data if bk['title'] != t]
    print("Book removed.")

def main():
    ld_lib()

    while True:
        print("\nLib System")
        print("1. Show Books")
        print("2. Insert Book")
        print("3. Remove Book")
        print("4. Save & Exit")

        ch = input("Choice: ")

        if ch == '1':
            sh_bks()
        elif ch == '2':
            ad_bk()
        elif ch == '3':
            dl_bk()
        elif ch == '4':
            sv_lib()
            print("Saved. Bye!")
            break
        else:
            print("Wrong. 1-4 only.")

if __name__ == "__main__":
    main()
