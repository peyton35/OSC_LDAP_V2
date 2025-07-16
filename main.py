import ldapapi.Enumerating


def main():
    enum = ldapapi.Enumerating
    api = enum.StartAPI()
    members = enum.get_membership_status(api, "Renee")
    
    print(members)
    

if __name__ == "__main__":
    # This block only runs when you execute main.py directly,
    # and not when you import it as a module elsewhere.    
    main()



