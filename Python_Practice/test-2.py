import subprocess
"""string = subprocess.check_output("ipconfig").decode("utf-8")
list1 = string.split("\n")
for i in list1:
    if "IPv4 Address" in i:
        print(i.split(' ')[-1])"""
def task(string_list):
    dict1 ={}
    for i in string_list[3:]:
        if len(i)==0:
            continue
        string_doublespace = i.split("  ")
        I = []
        for j in string_doublespace:
            if len(j)!=0:
                I.append(j)
        ser = I[0]
        pid = I[1].split(" ")[0]
        mem = I[3][:-1]
        dict1[ser]=[pid,mem]
    return dict1
def pid(string_list):
    dict2 = {}
    x = task(string_list)
    for k,v in x.items():
        dict2[k]=v[0]
    return dict2

def mem(string_list):
    dict2 = {}
    x = task(string_list)
    for k,v in x.items():
        dict2[k]=v[1]
    return dict2
        
        
string = subprocess.check_output("tasklist").decode("utf-8")
string_list = string.split("\n")
#print(pid(string_list))
#print(mem(string_list))
#Task4: services starts with s: and its process id
def service(string):
    dict3 = {}
    x = pid(string_list)
    for k,v in x.items():
        if k.startswith(string):
            dict3[k]=v
    return dict3
    
string = "p"
#print(service(string))
#Task 5: list all the services running
def running(string_list):
    list1 = []
    x = mem(string_list)
    for k,v in x.items():
        list1.append(k)
    return list1
running(string_list)
#print(running(string_list))
#Task 6:Size of the particular service:
def size_ser(string_list,ser):
    x = mem(string_list)
    for k,v in x.items():
        if ser in k:
            return v
        else:
            continue
ser = "IntelCpHDCPSvc.exe"
#print(size_ser(string_list,ser))
#Task 7: process id for particular service
def pid_ser(string_list,ser):
    x = pid(string_list)
    for k,v in x.items():
        if ser in k:
            return v
        else:
            continue
ser = "IntelCpHDCPSvc.exe"
#print(pid_ser(string_list,ser))
#Task 8: get the service name for the given process id
def ser_name_pid(string_list,process_id):
    x = pid(string_list)
    for k,v in x.items():
        if process_id in v:
            return k
        else:
            continue
string = subprocess.check_output("tasklist").decode("utf-8")
string_list = string.split("\n")
process_id ="5312"
#print(ser_name_pid(string_list,process_id))
    


