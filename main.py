import ldapapi.Enumerating


def main():
    enum = ldapapi.Enumerating
    api = enum.StartAPI()
    groups = enum.list_groups(api)

    for pair in groups:
        print(pair[0])

        for member in pair[1]:
            print(f'\t{member}')
    
    



if __name__ == "__main__":
    # This block only runs when you execute main.py directly,
    # and not when you import it as a module elsewhere.    
    main()



