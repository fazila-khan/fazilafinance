from datetime import datetime
from datetime import timedelta

fd_list=[]


def get_fd_data():
    fd={}
    fd['bank']= input("Enter the Bank name: ")
    fd['start_date'] = input("Enter the FD start date: ")
    fd['principal']= input("Enter the principal amount: ")
    fd['interest']= input("Enter the interest rate: ")
    fd['duration']=input("Enter the duration of investment (in days): ")
    fd['goal']= input("Enter the goal (car,emergency,insurance,exam,bday) : ")
    fd['maturity_date']=calc_maturity_date(fd)
    fd['maturity_amount']=calc_maturity_amount(fd)
    fd_list.append(fd)


def calc_maturity_date(fd):
    t_maturity_date= datetime.strptime(fd['start_date'],'%d-%m-%y') + timedelta(days=int(fd['duration']))
    return t_maturity_date


def calc_maturity_amount(fd):
    t_interest= int(fd['interest'])/100
    print("Interest in formula : %.2f " %(t_interest))
    t_duration= int(fd['duration'])/365
    print("Time in formulat is %.2f" %(t_duration))
    t_maturity_amount= int(fd['principal']) * (1 + (t_interest * t_duration))
    print("The maturity amount in the function is %.2f" %(t_maturity_amount))
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

choice = input("Enter 1 for new FD addition: ")
if choice == "1":
    get_fd_data()
    print_fd_list()

