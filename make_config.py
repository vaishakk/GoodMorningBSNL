import cli.app
import configparser

config = configparser.RawConfigParser()


def save_config():
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


@cli.app.CommandLineApp
def make_config(app):
    print(app.params.username)
    config.add_section('CREDENTIALS')
    config.set('CREDENTIALS', 'username', app.params.username)
    config.set('CREDENTIALS', 'password', app.params.password)
    config.add_section('OPERATIONAL PARAMETERS')
    config.set('OPERATIONAL PARAMETERS','Exchanges',app.params.exchanges)
    save_config()


make_config.add_param("username", help="ITPC user name", default='', type=str)
make_config.add_param("password", help="ITPC password", default='', type=str)
make_config.add_param("exchanges", help="List of exchanges", default=[], type=str)
if __name__ == "__main__":
    make_config.run()
