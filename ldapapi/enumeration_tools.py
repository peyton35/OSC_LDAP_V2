from . import LDAPAPI
from .devtools import ToolBox


class Emumerator(LDAPAPI):
    """
    Provides methods to interact with the LDAP server.
    """

    def __init__(self, hostname, adminuser, adminpass, basedn):
        """Initializes the object with the provided parameters."""
        from .dir_manipulation import Manipulator
        self.dir_manipulation = Manipulator(self)
        self.API = LDAPAPI(hostname, adminuser, adminpass, basedn)
        self.tools = ToolBox()
        
    def get_users(self) -> list:
        """
        Returns a list of tuples containing user CNs and email addresses.
        """
        base_dn = f'ou=People,{self.API.LDAP_BASE_DN}'
        self.API.conn.search(base_dn, '(objectClass=inetOrgPerson)', attributes=['cn', 'mail'])
        entries = self.API.conn.entries
        return [(user.cn, user.mail) for user in entries]

    def get_groups(self) -> list:
        """
        Returns a list of tuples containing group CNs and their members.
        """
        base_dn = f'ou=Groups,{self.API.LDAP_BASE_DN}'
        self.API.conn.search(base_dn, '(objectClass=groupOfNames)', attributes=['cn', 'member'])
        groupsAndMembers = []
        for group in self.API.conn.entries:
            users_names = [self.tools.CONVERT_CN_TO_FIRSTLAST(user) for user in group.member]
            groupsAndMembers.append((group.cn, users_names))
        return groupsAndMembers

    def get_memberships(self, usercn: str) -> list:
        """
        Returns a list of groups that the specified user is a member of.
        """
        groups = self.get_groups()
        return [(group[0], group[1]) for group in groups if usercn.lower() in [user.lower() for user in group[1]]]

    def check_for_user(self, usercn: str) -> tuple:
        """
        Checks if the specified user exists in the LDAP server.

        Returns a tuple containing a boolean indicating whether the user is present and the user's entry attributes if found.
        """
        base_dn = f'ou=People,{self.API.LDAP_BASE_DN}'
        self.API.conn.search(base_dn, f'(cn={usercn})', attributes=['*'])
        entries = self.API.conn.entries
        if entries:
            return (True, dict([(attr, value) for attr, value in entries[0].entry_attributes_map.items()]))
        else:
            return (False, None)

    def check_for_group(self, groupcn: str) -> bool:
        """
        Checks if the specified group exists in the LDAP server.

        Returns True if the group is found and False otherwise.
        """
        base_dn = f'ou=Groups,{self.API.LDAP_BASE_DN}'
        self.API.conn.search(base_dn, f'(cn={groupcn})', attributes=['*'])
        entries = self.API.conn.entries
        return len(entries) > 0

    def check_for_member_in_group(self, usercn: str, groupcn: str) -> bool:
        """
        Checks if the specified user is a member of the specified group.

        Returns True if the user is found in the group and False otherwise.
        """
        base_dn = f'ou=Groups,{self.API.LDAP_BASE_DN}'
        self.API.conn.search(base_dn, f'(cn={groupcn})', attributes=['member'])
        entries = self.API.conn.entries
        if entries:
            members = [user for user in entries[0].member]
            return usercn.lower() in [user.lower() for user in members]
        else:
            return False

    def get_user_attributes(self, usercn: str) -> dict:
        """
        Returns a dictionary containing the specified user's attributes.
        """
        base_dn = f'ou=People,{self.API.LDAP_BASE_DN}'
        self.API.conn.search(base_dn, f'(cn={usercn})', attributes=['*'])
        entry = self.API.conn.entries[0]
        return {attr: value for attr, value in entry.entry_attributes_map.items()}

    def get_group_attributes(self, groupcn: str) -> dict:
        """
        Returns a dictionary containing the specified group's attributes.
        """
        base_dn = f'ou=Groups,{self.API.LDAP_BASE_DN}'
        self.API.conn.search(base_dn, f'(cn={groupcn})', attributes=['*'])
        entry = self.API.conn.entries[0]
        return {attr: value for attr, value in entry.entry_attributes_map.items()}
