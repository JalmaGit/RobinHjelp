import shutil as sh

def simpleSolution():
    totaldiskSpace = float(input("Write in the size of your drive: "))
    utilizedDiskSpace = float(input("Write in the current drive usage: "))

    freeDiskSpace = totaldiskSpace - utilizedDiskSpace

    print(f"You have currently {freeDiskSpace} GB of free diskspace ")

def harderSolution():
    path = str(input("Write in the root to your system, for windows it will be C:\ "))
    stat = sh.disk_usage(path)
    print(f"Disk Usage statistics:\n{stat}")

harderSolution()