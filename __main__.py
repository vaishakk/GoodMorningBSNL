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
        print("ITPC username and password and exchange codes need to set before starting."
              " PRESS ANY KEY to continue...")
        # _ = input()
        username = input("Enter ITPC Username: ")
        password = input("Enter ITPC password: ")
        make_config.make_config('set_creds', username, password)
        print("Enter circle code, ssa name and exchange codes one-by-one as given in ITPC (Ex: For "
              "Kariyavattom exchange Circle code is KL, SSA name is THIRUVANANTHAPURAM and exchange code is TVMKVT)")
        circle = input('Enter Circle code: ')
        ssa = input('Enter SSA name: ')
        exgs = ''
        exg = ' '
        k = 0
        while exg != '':
            exg = input('Enter exchange code {}: '.format(k+1))
            k += 1
            exgs += exg + ','
        exgs = exgs[:-2] # Remove the blank entry
        make_config.make_config('set_oper', circle, ssa, exgs)
        main()
        return


if __name__ == "__main__":
    main()
    # make_config.make_config('edit_creds', 'B201001415', 'B201001415')
    # make_config.make_config('edit_oper', 'KL', 'THIRUVANANTHAPURAM', ['TVMMNK', 'TVMTPK'])
