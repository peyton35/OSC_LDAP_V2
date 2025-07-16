# OSC_LDAP_V2
---
##  ldapapi Package details
---
### `__init__.py` 

- Class LDAPAPI
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

    #### Use & Description
    This defines the package ldapapi (name in progress) and initializes the LDAPAPI class. In order to call this and initialize it, you would call the `LDAPAPI` class with the required variables
---
### `Enumerating.py`

#### Functions:

- `get_users(API : LDAPAPI)` 
  1. Must pass LDAPAPI object as parameter
  2. returns a list of tuples which include the users First and Last name, and their email
  <pan>
    users = get_users(API)
    users ---> `[("First Last", "first.last@s1osc.com")]`
  </pan>  
  
- `get_groups(API : LDAPAPI)`
  1. Must pass LDAPAPI object as paramter
  2. returns a list of tuples which includes the group name with the second index being a list of members

  groups = get_groups(API)
  groups ---> `[ ("AvC-Staff", ["Jimmy", "Peyton", "Gerald"]) ]`

    