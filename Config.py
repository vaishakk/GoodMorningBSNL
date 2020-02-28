import configparser


class Config:

    def __init__(self, config_file):
        self.username = ''
        self.password = ''
        self.circle = ''
        self.ssa = ''
        self.exchanges = ''
        self.file = config_file

    def save_config(self):
        config = configparser.RawConfigParser()
        config.add_section('CREDENTIALS')
        config.set('CREDENTIALS', 'username', self.username)
        config.set('CREDENTIALS', 'password', self.password)
        config.add_section('OPERATIONAL PARAMETERS')
        config.set('OPERATIONAL PARAMETERS', 'circle', self.circle)
        config.set('OPERATIONAL PARAMETERS', 'ssa', self.ssa)
        config.set('OPERATIONAL PARAMETERS', 'Exchanges', self.exchanges)
        with open(self.file, 'w') as configfile:
            config.write(configfile)

    def set_creds(self, username, password):
        self.username = username
        self.password = password

    def set_oper(self, circle, ssa, exgs):
        self.circle = circle
        self.ssa = ssa
        self.exchanges = exgs

    def read_config(self):
        config = configparser.RawConfigParser()
        files = config.read(self.file)
        if len(files):
            self.username = config['CREDENTIALS']['username']
            self.password = config['CREDENTIALS']['password']
            self.circle = config['OPERATIONAL PARAMETERS']['circle']
            self.ssa = config['OPERATIONAL PARAMETERS']['ssa']
            self.exchanges = config['OPERATIONAL PARAMETERS']['Exchanges'].split(',')
            return True
        else:
            return False
