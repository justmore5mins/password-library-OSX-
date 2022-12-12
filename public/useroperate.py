from useful_code.encode_and_decode import irreversible_encrypt

class add_del_user:
    def add_user(username:str,password:str):
        file = open("system_datas/useragent.csv","a+")
        file.write(username+","+irreversible_encrypt.sha_family.sha_family_encode_all(password,username,1000)+"\n")
        