import os
print("keys:\n enter 0 for shekan dns \n enter 1 for 1.1.1.1 and 8.8.8.8 dns \n enter 3 for 8.8.8.8 and 8.8.4.4 dns \n enter 4 for 1.1.1.1 and 1.0.0.1 dns \n")
a = int(input('which DNS do you want?  :'))
if a == 1 :
    os.system('netsh interface ip set dns name="Wi-Fi" source="static" address="1.1.1.1"')
    os.system('netsh interface ip add dns name="Wi-Fi" addr="8.8.8.8" index=2')
elif a == 0 :
    os.system('netsh interface ip set dns name="Wi-Fi" source="static" address="178.22.122.100"')
    os.system('netsh interface ip add dns name="Wi-Fi" addr="94.232.174.194" index=2')
elif a == 0 :
    os.system('netsh interface ip set dns name="Wi-Fi" source="static" address="8.8.8.8"')
    os.system('netsh interface ip add dns name="Wi-Fi" addr="8.8.4.4" index=2')
elif a == 0 :
    os.system('netsh interface ip set dns name="Wi-Fi" source="static" address="1.1.1.1"')
    os.system('netsh interface ip add dns name="Wi-Fi" addr="1.0.0.1" index=2')




print("dns changed succfully")    
    


        
       






