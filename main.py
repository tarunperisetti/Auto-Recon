from validator.valid import classify_target

#-----------------main-----------------
target = input("[+] Enter IP address or Domain name : ")
target_type = classify_target(target)