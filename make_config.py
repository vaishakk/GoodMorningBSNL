import configparser

config = configparser.RawConfigParser()


def save_config():
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def make_config(task, *argv):
    """
    Usage: make_config(task, list_of_args)
    task: 1. set_creds - Set ITPC username and password.
             Usage: make_config('set_creds', <username>, <password>)
             Ex: make_config('set_creds', 'B20xxxxxxx', 'B20xxxxxxx')
          2. set_oper - Set operational parameters like Circle, SSA and Exchanges.
             Usage: make_config('set_oper', <Circle code>, <SSA name>, <List of exchanges>)
             Ex: make_config('set_oper', 'KL', 'THIRUVANANTHAPURAM', ['TVMKVT', 'TVMTPK'])
          3. edit_creds - Change ITPC username and password.
             Usage: make_config('set_creds', <username>, <password>)
             Ex: make_config('set_creds', 'B20xxxxxxx', 'B20xxxxxxx')
          4. edit_oper - Change operational parameters like Circle, SSA and Exchanges.
             Usage: make_config('set_oper', <Circle code>, <SSA name>, <List of exchanges>)
             Ex: make_config('set_oper', 'KL', 'THIRUVANANTHAPURAM', ['TVMKVT', 'TVMTPK'])
    """
    if task == 'set_creds':
        config.add_section('CREDENTIALS')
        config.set('CREDENTIALS', 'username', argv[0])
        config.set('CREDENTIALS', 'password', argv[1])
    elif task == 'set_oper':
        config.add_section('OPERATIONAL PARAMETERS')
        config.set('OPERATIONAL PARAMETERS', 'circle', argv[0])
        config.set('OPERATIONAL PARAMETERS', 'ssa', argv[1])
        config.set('OPERATIONAL PARAMETERS', 'Exchanges', argv[2])
    save_config()


if __name__ == "__main__":
    pass
