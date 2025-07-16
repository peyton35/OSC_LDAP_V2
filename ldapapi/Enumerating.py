from . import LDAPAPI
from .devtools import CONVERT_CN_TO_FIRSTLAST


def StartAPI():
    api = LDAPAPI(hostname="ubuntu-s1-osc", adminuser="admin", adminpass="s1adminpassword", basedn="dc=s1oursaviorschurch,dc=com")
    return api

def get_users(API : LDAPAPI):
    """
    Return all inetOrgPerson entries (with cn and mail).
    """

    base_dn = f'ou=People,{API.LDAP_BASE_DN}'
    API.conn.search(base_dn, '(objectClass=inetOrgPerson)', attributes=['cn', 'mail'])
    entries = API.conn.entries
    userData = []

    for user in entries:
        userData.append((user.cn, user.mail))
    return userData     #   Returns as a list of doules  exe: [('First Last', 'mail@example.com'), ('Test User', 'email@test.com')]

def get_groups(API : LDAPAPI):
    """Return a list of all group CNs in the LDAP server."""
    base_dn = 'ou=Groups,dc=s1oursaviorschurch,dc=com'
    API.conn.search(base_dn, '(objectClass=groupOfNames)', attributes=['cn', 'member'])

    groupsAndMembers = []  

    for group in API.conn.entries:
        groupsAndMembers.append((group.cn, group.member))

    return groupsAndMembers # Comes out as a list of tuples | exe: [(AvC-Staff, [Jimmy, John, James])]




