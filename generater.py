import json,os,requests
import urllib.parse, pyperclip

class obj():   
    username=""
    password=""
    def login(self):
        '''登陆'''
        password_enc = self.password_encrypt(self.password,
                                             "123 4567890")
        payload = {
            "action": "login",
            "username": self.username_encrypt(self.username),
            "password": password_enc,
            "mac": "14%3af6%3ad8%3ab5%3aa9%3a5f",
            "ac_id": 1,
            "drop": 0,
            "pop": 1,
            "type": 2,
            "n": 117,
            "mbytes": 0,
            "minutes": 0,
        }
        
        username1 = urllib.parse.quote(self.username_encrypt(self.username))
        pass1 = urllib.parse.quote(password_enc)
        command = 'curl --interface eth0.3 -d "action=login&username=' + username1 + '&password='+pass1+'&drop=0&pop=0&type=2&n=117&mbytes=0&minutes=0&ac_id=2&mac=00%3a2b%3a67%3a5b%3a56%3a2e" http://172.16.154.130/cgi-bin/srun_portal'
        print(command)
        pyperclip.copy(command)

    @staticmethod
    def username_encrypt(username):
        result = '{SRUN3}\r\n'
        return result + ''.join([chr(ord(x) + 4) for x in username])

    @staticmethod
    def password_encrypt(password, key='1234567890'):
        result = ''
        for i in range(len(password)):
            ki = ord(password[i]) ^ ord(key[len(key) - i % len(key) - 1])
            _l = chr((ki & 0x0F) + 0x36)
            _h = chr((ki >> 4 & 0x0F) + 0x63)

            if i % 2 == 0:
                result += _l + _h
            else:
                result += _h + _l
        return result   
    

obj().login()
