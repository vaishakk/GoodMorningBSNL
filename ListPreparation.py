import pandas as pd
import os
from datetime import datetime


def prepare_list(exgs=[], cols=[], filename=''):
    fltData = pd.read_csv(filename)
    fltData = fltData[fltData.Exchange.isin(exgs)][cols]
    fltData.set_index("Phone No", inplace=True)
    return fltData


def write_list(exgs=[], cols=[]):
    download_dir = os.path.join(os.path.expanduser('~')+'\.GM')
    ll_cols = ["Exchange", "Phone No", "Fault Booked Date", "Complaint Sub Type", "Workgroup", "Vertical", "Pillar",
               "Customer Name", "House No", "Village", "Additional Details", "Mobile No"]
    ftth_cols = ["Exchange", "Phone No", "Booked Date", "Customer Name", "House No", "Village Name",
                 "Additional Details", "Mobile No"]
    ftth_file = os.path.join(download_dir+'\pending_bharat_fiber_complaints.csv')
    ll_file = os.path.join(download_dir+'\Pending faults Details.csv')
    ftth_list = prepare_list(exgs=exgs, cols=ftth_cols, filename=ftth_file)
    ll_list = prepare_list(exgs=exgs, cols=ll_cols, filename=ll_file)
    current_time = datetime.now().strftime("%d_%m_%Y_%H%M%S")
    dl_path = os.path.join(os.environ['userprofile'], 'Desktop\\Faults_{}.xlsx'.format(current_time))
    with pd.ExcelWriter(dl_path) as writer:
        ftth_list.to_excel(writer, 'FTTH')
        ll_list.to_excel(writer, 'LL+BB')
    os.remove(ftth_file)
    os.remove(ll_file)
