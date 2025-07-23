from ldap3 import MODIFY_ADD, MODIFY_DELETE, MODIFY_REPLACE
from . import password_maker
from .enumeration_tools import Emumerator
import getpass

class Manipulator:

    def add_user(self, cn: str,email : str = "none"):
        
        user_is_in, user_cn = self.ENUM.check_for_user(cn)

        if not user_is_in:
            mail_addr = ""
            dn = f'cn={cn},ou=People,{self.ENUM.API.LDAP_BASE_DN}'
            first, last = cn.split(" ")
            if email == "none":
                mail_addr = f'{first}.{last}@s1osc.com'
            else:
                mail_addr = email
            
            objectClasses = ['inetOrgPerson', 'organizationalPerson', 'person', 'top']
            attributes = {'sn': last, 'givenName': first, 'mail': mail_addr}

            user_added = self.ENUM.API.conn.add(dn, objectClasses, attributes)

            if user_added:
                print(f"User '{cn}' added!!")
            else:
                print(f'User {cn} unable to be added.')
            
    def remove_user(self, cn : str):

        if not self.ENUM.API.check_for_user(cn):
            dn = f'cn={cn},ou=People,{self.ENUM.API.LDAP_BASE_DN}'

            try:
                self.ENUM.API.conn.delete(dn)
            except Exception as e:
                print(f'[ERR] - An error occured removing user...')
                print(e)

            if not self.ENUM.API.check_for_user(cn):
                print(f'User {cn} removed successfully!!')

        else:
            print(f"User {cn} doesn't exists...")

    def set_user_email(self, cn: str, newemail : str):
        
        if self.ENUM.API.check_for_user(self.ENUM.API, cn):
            dn = f'cn={cn},ou=People,{self.ENUM.API.LDAP_BASE_DN}'
            if self.ENUM.API.conn.modify(dn, {'mail': [(MODIFY_REPLACE, [newemail])]}):
                print(f"User's email changed to {newemail}")
            else:
                print(f"email invalid")

    def add_group(self, groupcn : str, member_dns : list = []):
    
        group_exists = False
        groupdn = f'cn={groupcn},ou=Groups,dc=s1oursaviorschurch,dc=com'
        if self.ENUM.API.conn.search(groupdn, '(objectClass=*)'):
            group_exists = True

        if group_exists:
            print("Group already exists...")
        else:
            objectClasses = ['groupOfNames', 'top']
            attributes = {'cn': groupcn, 'member': member_dns}

            self.ENUM.API.conn.add(groupdn, objectClasses, attributes)
            print(f"Added {groupcn} successfully!")

    def remove_group(self, groupcn : str):
        
        group_dn = f'cn]{groupcn},ou=Groups,{self.ENUM.API.LDAP_BASE_DN}'
        if self.ENUM.API.conn.search(group_dn, '(objectClass=*)'):
            return False
        
        return self.ENUM.API.conn.delete(group_dn)

    def set_user_password(self, usercn : str, newpass : str):
        
        encrypted_password = ""
        dn = f'cn={usercn},ou=People,{self.ENUM.API.LDAP_BASE_DN}'

        if newpass.lower() == "ask":
            firstask = getpass.getpass("Enter New Password: ")
            verifyask = getpass.getpass("Verify: ")

            if firstask == verifyask:
                encrypted_password = password_maker.make_ssha_password(verifyask)
            
        else:
                encrypted_password = password_maker.make_ssha_password(newpass)

        try:
            success = self.ENUM.API.conn.modify(dn, {'userPassword': [(MODIFY_REPLACE, [encrypted_password])]})
            print("Success!")
            return success   
        except Exception as e:
            print("[ERR] -\n")
            print(e)
            return False

    def add_member_to_group(self, usercn : str, groupcn : str):
        
        #   Constants
        group_dn = f'cn={groupcn},ou=Groups,{self.ENUM.API.LDAP_BASE_DN}'
        user_dn = f'cn={usercn},ou=Peoplem,{self.ENUM.API.LDAP_BASE_DN}'

        #   Check if user already is in group
        if self.ENUM.API.check_for_member_in_group(usercn, groupcn):
            print("User already exists")
            return False
        else:
            #   If users doesn't exist, prompt for adding user
            uinput = f"User {usercn} does not exist...\nWould you like to create this user? - [Y/n]: "

            if uinput.lower() == "y":
                self.add_user(usercn)
                print("User added! Remember to change the user's email!!!\n")
            else:
                print("Cancelling member add...")
                return False
            
            print("Success!")
            return self.ENUM.API.conn.modify(group_dn, {'member': [(MODIFY_ADD, [user_dn])]})

    def remove_member_from_group(self, usercn : str, groupcn : str):
        #   Check if user is not in group
        if not self.ENUM.API.check_for_member_in_group(usercn, groupcn):
            print(f"User doesn't exists in {groupcn}")
            return False
        else:
            group_dn = f'cn={groupcn},ou=Groups,{self.ENUM.API.LDAP_BASE_DN}'
            user_dn = f'cn={usercn},ou=Peoplem,{self.ENUM.API.LDAP_BASE_DN}'
            print("Success!")
            return self.ENUM.API.conn.modify(group_dn, {'member': [(MODIFY_DELETE, [user_dn])]})

    def __init__(self, ENUM : Emumerator):
        self.ENUM = ENUM

