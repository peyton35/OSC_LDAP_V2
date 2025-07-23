# OSC_LDAP_V2
## ldapapi Package Details
### `__init__.py` 

*   Class LDAPAPI
    #### Variables:
    <pre>
        (required) LDAP_HOSTNAME - hostname/ip address of ldap server 
        (required) LDAP_PORT - port that the server is listening on 
         (required)LDAP_ADMIN_USER - user used to log in to database 
        (required) LDAP_ADMIN_PASSWORD - password for user to log in to database 
        (requried) LDAP_BASE_DN - base dn used for ldap query 
        The two below are made from the variables above
        server - ldap server configuration object (pointer to ldap server)
        conn - connection for server (used for server interaction like searching).
    </pre>

    #### Use & Description:
    This defines the package ldapapi (name in progress) and initializes the LDAPAPI class. In order to call this and initialize it, you would call the `LDAPAPI` class with the required variables.
### `Enumerating.py`

#### Functions:

*   `get_users(API : LDAPAPI)`
  1. Must pass LDAPAPI object as parameter
  2. returns a list of tuples which include the users First and Last name, and their email
*   `get_groups(API : LDAPAPI)`
  1. Must pass LDAPAPI object as paramter
  2. returns a list of tuples which includes the group name with the second index being a list of members

### `dir_manipulation.py`

#### Functions:

*   `add_user(self, cn: str,email : str = "none")`
    *   Adds a new user to the LDAP server
    *   If email is not provided, it will be generated based on the username

*   `remove_user(self, cn : str)`
    *   Removes an existing user from the LDAP server

*   `set_user_email(self, cn: str, newemail : str)`
    *   Updates the email address of an existing user in the LDAP server

### `password_maker.py`

#### Functions:

*   `make_ssha_password(password: str, salt_length: int = 6) -> str`
    *   Generates an SSHA-hashed password suitable for LDAP’s {SSHA} scheme
    *   The clear-text password is hashed with a random salt and encoded in base64

### `enumeration_tools.py`

#### Functions:

*   `get_users(self)`
    *   Returns a list of tuples containing user information (first name, last name, and email)

*   `get_groups(self)`
    *   Returns a list of tuples containing group information (group name and members)

## API Documentation

### LDAPAPI Class

The LDAPAPI class provides methods for interacting with the LDAP server.

#### Methods:

*   `__init__(self, hostname: str, adminuser : str, adminpass : str, basedn: str)`
    *   Initializes the LDAPAPI object
    *   Sets the host name, administrator user, password, and base DN of the LDAP server

### Emumerator Class

The Emurator class provides methods for interacting with the LDAP server.

#### Methods:

*   `__init__(self, hostname, adminuser, adminpass, basedn)`
    *   Initializes the Emumerator object
    *   Sets the host name, administrator user, password, and base DN of the LDAP server

*   `get_users(self) -> list`
    *   Returns a list of tuples containing user information (first name, last name, and email)

*   `get_groups(self) -> list`
    *   Returns a list of tuples containing group information (group name and members)

## Usage

To use the ldapapi package, create an instance of the LDAPAPI class or the Emurator class, passing in the required parameters.

```python
from ldapapi import LDAPAPI

ldap_api = LDAPAPI("hostname", "adminuser", "adminpass", "basedn")
```

You can then call methods on the object to interact with the LDAP server.

```python
users = ldap_api.get_users()
groups = ldap_api.get_groups()
```

Note: This is a basic example and you should adjust the code to fit your specific needs.
