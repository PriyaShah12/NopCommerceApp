import configparser

config=configparser.RawConfigParser()
config.read(".//Configurations//config.ini")

class configRead:
    @staticmethod
    def ReadUrl():
        url=config.get('common Info', 'base_url')
        return url
    @staticmethod
    def ReadUsername():
        username=config.get('common Info', 'username')
        return username
    @staticmethod
    def Readpassword():
        password=config.get('common Info', 'password')
        return password



