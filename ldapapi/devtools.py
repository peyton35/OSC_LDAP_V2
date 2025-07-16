

def CONVERT_CN_TO_FIRSTLAST(cn : str):
    #   Takes a cn string and turns it into just a first and last name
    #   exe: "cn=admin,ou=People,dc=s1oursaviorschurch,dc=com" ---> "admin"
    
    cnonly = cn.replace(",dc=s1oursaviorschurch,dc=com", "")
    formattedcn = cnonly.replace("cn=", "")

    if "ou" in formattedcn:
        formattedcn = formattedcn.replace(",ou=People", "")

    return formattedcn
