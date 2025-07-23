import ldapapi.enumeration_tools
import streamlit as st

def refresh_table():
    return enum.get_users()

def change_user_mail(previous_mail, new_mail):
    pass



def display_user_table():

    users = refresh_table()

    with st.container(key="UsersEditContainer", border=True, height=650):

        search_filer = st.text_input("Search:")
        memberships = []

        for idx, user in enumerate(users):

            membership = enum.get_memberships(str(user[0]))
            print(membership)

            if search_filer.lower() in str(user[0]).lower() or search_filer.lower() in str(user[1]).lower():
                with st.container(key=f"UserCon{idx}", border=True, height=125):
                
                    col1, col2, col3 = st.columns(3, gap="small")

                    with col1:
                        st.text(user[0])
                    with col2:
                        st.text(user[1])
                    with col3:
                        with st.popover(f"Edit User") as editbox:
                            with st.form(f"UserEditForm{idx}"):
                                #   Title
                                st.subheader(f"{user[0]}")

                                #   Options
                                user_mail = st.text_input("User's Email", value=str(user[1]))
                                st.write(membership)

                                if st.form_submit_button("Submit"):
                                    change_user_mail(str(user[1]), user_mail)

    


if __name__ == "__main__":
    # This block only runs when you execute main.py directly,
    # and not when you import it as a module elsewhere.    

    enum = ldapapi.enumeration_tools.Emumerator(hostname="ubuntu-s1-osc", adminuser="admin", adminpass="s1adminpassword", basedn="dc=s1oursaviorschurch,dc=com")
    dirman = enum.dir_manipulation

    memberships = []
    users = enum.get_users()

    for user in users:
        membership = enum.get_memberships(user)
        memberships.append(membership)

    print(memberships)

    

