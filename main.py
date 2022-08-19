import datetime
import time

# Enter the date and time that you wanted to block in the (YYYY, MM, DD) format
end_time = datetime.datetime(2022, 8, 20)

# Enter the websites that you wants to block
site_block = ["www.facebook.com", "www.instagram.com"]

# Enter the path of the host file in Windows
host_path = "C:/Windows/System32/drivers/etc/hosts"

# Enter the redirect local host
redirect = "127.0.0.1"


while True:
    if datetime.datetime.now() < end_time:
        print("Start Blocking")
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect + " " + website + "\n")
                else:
                    pass
    else:
        with open(host_path, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate()
        time.sleep(5)
