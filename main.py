from datetime import datetime

def get_date():
    date = input("Input the date for which you are entering values.\nIf you just want to use today's date, press enter.\nIf you want to use a different date, enter it in the form mm/dd/yyyy:\n")
    if date == "":
        date = datetime.today()
    else:
        specs = date.split("/")
        date = datetime(month=int(specs[0]), day=int(specs[1]), year=int(specs[2]))
    return date

def get_hours_v_needed():
    return int(input("\nInput the % value for the amount of sleep you got, versus how much you needed:\n"))

def get_sleep_consistency():
    return int(input("\nInput the % value for your sleep consistency:\n"))

def get_recovery():
    return int(input("\nInput the % value for your recovery:\n"))

def get_strain():
    return int(input("\nInput the value for your strain:\n"))

def get_hrv():
    return int(input("\nInput the ms value for your heart rate variability:\n"))

def main():
    date = get_date()
    hours_v_needed = get_hours_v_needed()
    sleep_consistency = get_sleep_consistency()
    recovery = get_recovery()
    strain = get_strain()
    hrv = get_hrv()

main()