import ldap3
import ldap3.abstract


# ldapapi
print("Loading ldapapi...")
version = "0.2.0"


class LDAPAPI:

    #   Set initial Vars for connection
    #   Create Server and Connection

    def __init__(self, hostname: str,adminuser : str, adminpass : str, basedn: str):
        
        # ------ Connection Details ------ 
        self.LDAP_HOSTNAME = hostname
        self.LDAP_PORT = 389
        self.LDAP_ADMIN_USER = adminuser
        self.LDAP_ADMIN_PASSWORD = adminpass
        self.LDAP_BASE_DN = basedn

        # ------ Initialize Connection ------ 
        try:
            self.server = ldap3.Server(
                host=self.LDAP_HOSTNAME,
                port=self.LDAP_PORT,
                get_info=ldap3.ALL,
                use_ssl=False
            )

            self.conn = ldap3.Connection(
                self.server,
                user=f'cn={self.LDAP_ADMIN_USER},{self.LDAP_BASE_DN}',
                password=adminpass,
                auto_bind=True
            )
        except Exception as e:
            print('Error occured while connecting!!')
            print(f'[ERR] - {e}')

        print(f"Joined as {self.LDAP_ADMIN_USER}")

    
