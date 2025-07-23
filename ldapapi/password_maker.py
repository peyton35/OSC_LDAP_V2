import os
import hashlib
import base64

def make_ssha_password(password: str, salt_length: int = 6) -> str:
    """
    Generate an SSHA-hashed password suitable for LDAP’s {SSHA} scheme.

    :param password: The clear-text password.
    :param salt_length: Number of random salt bytes to append (4–8 is typical).
    :return: A string like "{SSHA}nXb…salt…==" ready to store in LDAP.
    """
    # 1) Generate a random salt
    salt = os.urandom(salt_length)

    # 2) Compute the SHA-1 digest of password+salt
    sha1_digest = hashlib.sha1(password.encode('utf-8') + salt).digest()

    # 3) Base64-encode the concatenation of digest + salt
    digest_salt = sha1_digest + salt
    b64 = base64.b64encode(digest_salt).decode('ascii')

    # 4) Prefix with the {SSHA} tag
    return f"{{SSHA}}{b64}"
