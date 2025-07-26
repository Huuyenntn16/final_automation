import json

class ConfigReader:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    @staticmethod
    def load_config(path='url.json'):

        with open(path, 'r') as file:
            data = json.load(file)

        return ConfigReader(
            base_url=data["url"],
            username=data["username"],
            password=data["password"],
        )
        
    
    def get_url(self):
        return self.base_url
    
    
    def get_username(self):
        return self.username
    
    
    def get_password(self):
        return self.password
    
    