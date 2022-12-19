import hashlib


def crack_sha1_hash(input_hash, use_salts=False):
    if not use_salts:
        with open('top-10000-passwords.txt') as f:
            lines = f.readlines()
            for line in lines:
                hashed_pass = hashlib.sha1(line.replace("\n", "").encode()).hexdigest()
                if hashed_pass == input_hash:
                    print(line.replace("\n", ""))
    else:
        with open('known-salts.txt') as f:
            salts = f.readlines()
            for salt in salts:
                salt = salt.replace('\n', '')
                with open('top-10000-passwords.txt') as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.replace('\n', '')
                        line = salt + line + salt
                        hashed_pass = hashlib.sha1(line.replace("\n", "").encode()).hexdigest()
                        if hashed_pass == input_hash:
                            print(line.replace("\n", ""))


crack_sha1_hash('da5a4e8cf89539e66097acd2f8af128acae2f8ae', use_salts=True)
