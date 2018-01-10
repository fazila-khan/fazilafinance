from datetime import datetime
from datetime import timedelta
from pathlib import Path
import json
import os.path

fd_list=[]

def get_fd_data():
    fd={}
    fd['bank']= input("Enter the Bank name: ")
    fd['start_date'] = input("Enter the FD start date (in format dd-mm-yy) : ")
    fd['principal']= input("Enter the principal amount: ")
    fd['interest']= input("Enter the interest rate: ")
    fd['duration']=input("Enter the duration of investment (in days): ")
    fd['goal']= input("Enter the goal (car,emergency,insurance,exam,bday) : ")
    fd['maturity_date']=calc_maturity_date(fd)
    fd['maturity_amount']=calc_maturity_amount(fd)
    fd_list.append(fd)


def calc_maturity_date(fd):
    t_maturity_date= datetime.strptime(fd['start_date'],'%d-%m-%y') + timedelta(days=int(fd['duration']))
    return t_maturity_date.isoformat()


def calc_maturity_amount(fd):
    t_interest= int(fd['interest'])/100
    #print("Interest in formula : %.2f " %(t_interest))
    t_duration= int(fd['duration'])/365
    #print("Time in formulat is %.2f" %(t_duration))
    t_maturity_amount= int(fd['principal']) * (1 + (t_interest * t_duration))
    #print("The maturity amount in the function is %.2f" %(t_maturity_amount))
    return t_maturity_amount


def print_fd_list():
    for fd in fd_list:
        print("Bank : " + fd['bank'])
        print("FD Start date : " + fd['start_date'])
        print("Principal : " + fd['principal'])
        print("Interest rate : " + fd['interest'])
        print("Duration : " + fd['duration'])
        print("Maturity date : " + fd['maturity_date'].strftime('%d-%m-%y'))
        print("Maturity amount : %.2f"  %(fd['maturity_amount']))
        print("Goal : " + fd['goal'])
        print("************************************************************")


def save_file():
    try:
        file_path=Path("FD_data.json")
        if file_path.exists():
            print(file_path.exists())
            f = open("FD_data.json", "ab")
            f.seek(-1,os.SEEK_END)
            f.truncate()
            for fd in fd_list:
                f.write(b',')
                f.write(json.dumps(fd).encode('utf-8'))
            f.write(b']')
        else:
            f = open("FD_data.json","ab")
            f.write(b'[')
            for fd in fd_list:
                f.write(json.dumps(fd).encode('utf-8'))
            f.write(b']')
            f.close()
    except Exception:
        print("Error saving data to file")


choice = input("Enter 1 for new FD addition: ")
if choice == "1":
    get_fd_data()
    #print_fd_list()
    save_file()
    print ("Thank you!")

