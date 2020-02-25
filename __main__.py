import configparser
import ListPreparation
import itpc_utils
from ITPCBrowser import ITPCBrowser
import make_config


def main():
    config = configparser.RawConfigParser()
    files = config.read('config.ini')
    if len(files):
        username = config['CREDENTIALS']['username']
        password = config['CREDENTIALS']['password']
        circle = config['OPERATIONAL PARAMETERS']['circle']
        ssa = config['OPERATIONAL PARAMETERS']['ssa']
        exgs = config['OPERATIONAL PARAMETERS']['Exchanges'].split(',')
        print(exgs)

        browser = ITPCBrowser(username, password)
        browser.set_params(circle=circle, ssa=ssa, exgs=exgs)
        browser.pipeline()
        ListPreparation.write_list(exgs=exgs)
    else:
        print("Username and password not set. Run python make_config.py <username> <password>")
        return


if __name__ == "__main__":
    #main()
    make_config.make_config('edit_creds', 'B201001415', 'B201001415')
    #make_config.make_config('edit_oper', 'KL', 'THIRUVANANTHAPURAM', ['TVMMNK', 'TVMTPK'])
