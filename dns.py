import ctypes, sys, os , types, traceback
import re
import socket
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_default_interface_name():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  s.connect(("8.8.8.8", 80))
  ip = s.getsockname()[0]

  proc = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
  stdout = proc.communicate()[0].decode()

  interfaces = []
  iface = None 
  for line in stdout.splitlines():
    if re.search(r"adapter \w+", line):
      iface = line.split(":")[0]
      interfaces.append(iface)
    elif ip in line:
      return iface

  if not interfaces:
    return None
    
  return interfaces[0]
  
  
if is_admin():
    interface = get_default_interface_name()
    words = interface.split("adapter ")
    adp = words[1]


    print("        DONT FORGET TO RUN AS ADMINISTRATOR!!!")
    b = (input("keys:\n"
              "enter 0 if you dont know what your dns is \n"
              "enter 1 for Cloudflare - 1.1.1.1, 1.0.0.1 \n"
              "enter 2 for Google - 8.8.8.8, 8.8.4.4 \n"
              "enter 3 for OpenDNS - 208.67.222.222, 208.67.220.220 \n"
              "enter 4 for Quad9 - 9.9.9.9, 149.112.112.112 \n"
              "enter 5 for CleanBrowsing - 185.228.168.9, 185.228.169.9  \n"
              "enter 6 for AdGuard - 176.103.130.130, 176.103.130.131  \n"
              "enter 7 for Comodo - 8.26.56.26, 8.20.247.20 \n"
              "enter 8 for DNS.WATCH - 84.200.69.80, 84.200.70.40 \n"
              "enter 9 for Yandex - 77.88.8.8, 77.88.8.1 \n"
              "enter 10 for UncensoredDNS - 91.239.100.100, 89.233.43.71 \n"
	      "enter 11 for Ad-filtering - 76.76.19.19, 76.223.122.150 \n"
	      "enter 12 for Shekan DNS (not recommended) \n"
              "enter 13 for Electro DNS (not recommended) \n"
              "enter 14 for Radar-game DNS (not recommended) \n"
              "\n"
              "**enter 99 for clearing DNS cache \n"
              "\n"
              ":-->>"))
    a = int(b)

    if a == 1 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="1.1.1.1"')
        os.system('netsh interface ip add dns name=' + adp + '  addr="1.0.0.1" index=2')

    elif a == 2 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="8.8.8.8"')
        os.system('netsh interface ip add dns name=' + adp + '  addr="8.8.4.4" index=2')

    elif a == 3 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="208.67.222.222')
        os.system('netsh interface ip add dns name=' + adp + ' addr="208.67.220.220" index=2')

    elif a == 4 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="9.9.9.9"')
        os.system('netsh interface ip add dns name=' + adp + '  addr="149.112.112.112" index=2')
        
    elif a == 5 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="185.228.168.9"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="185.228.169.9" index=2')

    elif a == 6 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="176.103.130.130"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="176.103.130.131" index=2')

    elif a == 7 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="8.26.56.26"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="8.20.247.20" index=2')

    elif a == 8 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="84.200.69.80"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="84.200.70.40" index=2')

    elif a == 9 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="77.88.8.8"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="77.88.8.1" index=2')
        
    elif a == 10 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="91.239.100.100"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="89.233.43.71" index=2')

    elif a == 11 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="76.76.19.19"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="76.223.122.150" index=2')

    elif a == 12 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="178.22.122.100"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="185.51.200.2" index=2')
        
    elif a == 13 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="78.157.42.100"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="78.157.42.101" index=2')
        
    elif a == 14 :
        os.system('netsh interface ip set dns name=' + adp + ' source="static" address="10.202.10.10"')
        os.system('netsh interface ip add dns name=' + adp + ' addr="10.202.10.11" index=2')

    elif a == 0 :
        os.system('echo exit | nslookup')

    elif a == 99 :
        os.system('ipconfig /flushdns')
        print("Your DNS cache is now clear")



    print("Task completed successfully")
    os.system('echo exit | nslookup')
    input('Press ENTER to exit')

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


