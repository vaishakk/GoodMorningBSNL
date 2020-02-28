import ListPreparation
import itpc_utils
from ITPCBrowser import ITPCBrowser
from make_config import Config
import os


download_dir = os.path.join(os.path.expanduser('~')+'\.GM\Downloads')
config_file = os.path.join(os.path.expanduser('~')+'\.GM\config.ini')


def main():
    os.rmdir(download_dir)  # Clear all previous files
    config = Config(config_file)
    if config.read_config():
        browser = ITPCBrowser(config.username, config.password)
        browser.set_params(circle=config.circle, ssa=config.ssa, exgs=config.exgs)
        browser.pipeline()
        ListPreparation.write_list(exgs=config.exgs, download_dir=download_dir)
    else:
        print("ITPC username and password and exchange codes need to set before starting."
              " PRESS ANY KEY to continue...")
        # _ = input()
        username = input("Enter ITPC Username: ")
        password = input("Enter ITPC password: ")
        config.set_creds(username, password)
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
        config.set_oper(circle, ssa, exgs)
        main()
        return


if __name__ == "__main__":
    main()
    # make_config.make_config('edit_creds', 'B201001415', 'B201001415')
    # make_config.make_config('edit_oper', 'KL', 'THIRUVANANTHAPURAM', ['TVMMNK', 'TVMTPK'])
