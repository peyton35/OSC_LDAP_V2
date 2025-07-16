

def CONVERT_CN_TO_FIRSTLAST(cn : str):
    #   Takes a cn string and turns it into just a first and last name
    #   exe: "cn=admin,ou=People,dc=s1oursaviorschurch,dc=com" ---> "admin"
    cnonly, therest = cn.split(',ou')
    formated_value = cnonly.replace("cn=", '')
    return formated_value

