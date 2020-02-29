import ListPreparation
import itpc_utils
from ITPCBrowser import ITPCBrowser
from Config import Config
import os
import shutil
import time
import sys
import select
import msvcrt


download_dir = os.path.join(os.path.expanduser('~')+'\.GM\Downloads')
config_file = os.path.join(os.path.expanduser('~')+'\.GM\config.ini')


def change_config():
    config = Config(config_file)
    _ = config.read_config()
    print('Select Option')
    print('1. Change username and passowrd')
    print('2. Change Circle, SSA and Exchanges')
    print('3. Change SSA and Exchanges')
    print('4. Change Exchanges')
    print('5. Add Exchanges')
    print('6. View current settings')
    print('7. Exit')
    option = input('Option: ')
    if option == '1':
        username = input("Enter ITPC Username: ")
        password = input("Enter ITPC password: ")
        config.set_creds(username, password)
        config.save_config()
    elif option == '2':
        circle = input('Enter Circle code: ')
        ssa = input('Enter SSA name: ')
        exgs = ''
        exg = ' '
        k = 0
        while exg != '':
            exg = input('Enter exchange code {}: '.format(k + 1))
            k += 1
            exgs += exg + ','
        exgs = exgs[:-2]  # Remove the blank entry
        config.set_oper(circle, ssa, exgs)
        config.save_config()
    elif option == '3':
        ssa = input('Enter SSA name: ')
        exgs = ''
        exg = ' '
        k = 0
        while exg != '':
            exg = input('Enter exchange code {}: '.format(k + 1))
            k += 1
            exgs += exg + ','
        exgs = exgs[:-2]  # Remove the blank entry
        config.set_oper(config.circle, ssa, exgs)
        config.save_config()
    elif option == '4':
        exgs = ''
        exg = ' '
        k = 0
        while exg != '':
            exg = input('Enter exchange code {}: '.format(k + 1))
            k += 1
            exgs += exg + ','
        exgs = exgs[:-2]  # Remove the blank entry
        config.set_oper(config.circle, config.ssa, exgs)
        config.save_config()
    elif option == '5':
        exgs = ''
        exg = ' '
        k = 0
        while exg != '':
            exg = input('Enter exchange code {}: '.format(k + 1))
            k += 1
            exgs += exg + ','
        exgs = exgs[:-2]  # Remove the blank entry
        config.set_oper(config.circle, config.ssa, config.exchanges + ',' + exgs)
        config.save_config()
    elif option == '6':
        config.show_config()
    elif option == '7':
        return
    else:
        print('Invalid option')
        change_config()



def main():
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)  # Clear all previous files
    config = Config(config_file)
    if config.read_config():
        #option = input('Press s to go to settings. Press any other key to continue running.')
        print('Press s to go to settings. Press any other key to continue running.')
        option = msvcrt.getch()
        if option == b's' or option == b'S':
            change_config()
            main()
        else:
            browser = ITPCBrowser(config.username, config.password)
            browser.set_params(circle=config.circle, ssa=config.ssa, exgs=config.exchanges)
            browser.pipeline()
            ListPreparation.write_list(exgs=config.exchanges.split(','), download_dir=download_dir)
    else:
        os.mkdir(os.path.join(os.path.expanduser('~')+'\.GM'))
        print("ITPC username and password and exchange codes need to set before starting.")
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
        config.save_config()
        main()
        return


if __name__ == "__main__":
    main()
    # make_config.make_config('edit_creds', 'B201001415', 'B201001415')
    # make_config.make_config('edit_oper', 'KL', 'THIRUVANANTHAPURAM', ['TVMMNK', 'TVMTPK'])
