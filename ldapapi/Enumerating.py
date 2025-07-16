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
        users_names = []

        for user in group.member:
            users_names.append(CONVERT_CN_TO_FIRSTLAST(user))

        groupsAndMembers.append((group.cn, users_names))

    return groupsAndMembers # Comes out as a list of tuples | exe: [(AvC-Staff, [Jimmy, John, James])]

def get_membership_status(API : LDAPAPI, usercn : str):
    groups_member_is_part_of = []
    member = ""
    groups = get_groups(API)


    for group in groups:
        GroupName = group[0]
        Members = group[1]


        if GroupName not in groups_member_is_part_of:
            for user in Members:
                if usercn.lower() in user.lower():
                    member = user
                    groups_member_is_part_of.append(GroupName)

    return (member, groups_member_is_part_of)
    



