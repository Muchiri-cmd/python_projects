import subprocess
import time
out = subprocess.getoutput('netsh wlan show profiles').split("\n")  
profiles = []  
for profile in out:
    if "All User Profile" in profile:
        profile = profile.split(":")
        profile = profile[1]
        profile = profile.strip()
        profiles.append(profile)
        shortlist= []
        
for ssid in profiles:
    cmd = 'netsh wlan show profiles "'+ssid+'" key=clear"'
    data = subprocess.getoutput(cmd).split("\n")
    for word in data:
        if "Key Content" in word:
            password = word.split(":")
            password = password[1]
            password = password.strip()
            shortlist.append([ssid,password])

for info in shortlist:
    print("\nSSID: ",info[0],"\nPassword: ",info[1])
    print("\n-----------------------")

time.sleep(10)
