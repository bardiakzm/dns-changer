import ctypes, sys, os , types, traceback

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    adp = "Wi-Fi"


    print("        DONT FORGET TO RUN AS ADMINISTRATOR!!!")
    b = (input("keys:\n"
              "enter 0 if you dont know what is your dns \n"
              "enter 1 for shekan DNS \n"
              "enter 2 for 1.1.1.1 and 8.8.8.8 DNS \n"
              "enter 3 for 8.8.8.8 and 8.8.4.4 DNS \n"
              "enter 4 for 1.1.1.1 and 1.0.0.1 DNS \n"
              "enter 5 for OpenDNS  \n"
              "enter 6 for level3 DNS  \n"
              "enter 7 for comodo DNS \n"
              "enter 8 for NortonSafe DNS \n"
              "enter 9 for yandex DNS \n"
              "enter 10 for just 8.8.4.4 as primary DNS \n"
			  "enter 11 for addguard DNS \n"
			  "enter 12 for Iran DNS \n"
              ":-->>"))
    a = int(b)

    if a == 2 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="1.1.1.1"')
        os.system('netsh interface ip add dns name=' + adp + '  addr="8.8.8.8" index=2')

    elif a == 1 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="178.22.122.100"')
        os.system('netsh interface ip add dns name=' + adp + '  addr="185.51.200.2" index=2')

    elif a == 3 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="8.8.8.8"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="8.8.4.4" index=2')

    elif a == 4 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="1.1.1.1"')
        os.system('netsh interface ip add dns name=' + adp + '  addr="1.0.0.1" index=2')
    elif a == 5 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="208.67.222.222"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="208.67.220.220" index=2')

    elif a == 6 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="209.244.0.3"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="209.244.0.4" index=2')

    elif a == 7 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="8.26.56.26"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="8.20.247.20" index=2')

    elif a == 8 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="199.85.126.10"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="199.85.127.10" index=2')

    elif a == 9 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="77.88.8.8"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="77.88.8.1" index=2')

    elif a == 11 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="176.103.130.132"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="176.103.130.134" index=2')

    elif a == 12 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="217.218.127.127"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="217.218.155.155" index=2')

    elif a == 0 :
        os.system('echo exit | nslookup')

    if a == 10 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="8.8.4.4"')


    print("dns changed succfully")
    os.system('echo exit | nslookup')
    input('Press ENTER to exit')

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#2606:4700:4700::1001 , 2606:4700:4700::1111s
