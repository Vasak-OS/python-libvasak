import os
import platform

class VSKInfoHard:
    def __init__(self):
        self._info = {
              "os": self.getOSName(),
              "system": platform.system(),
              "kernel": platform.release(),
              "machine": platform.machine(),
              "architecture": platform.architecture()[0],
              "uname": platform.uname()[1],
              "ram": round((os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")) / (1012.**3)),
              "cpu": self.getCPUInfo(),
              "gpu": self.getGPUInfo(),
              "hostname": platform.node(),
              "username": os.getlogin(),
            }
    
    def getInfo(self):
        return self._info
    
    def getCPUInfo(self):
        hard = os.popen("cat /proc/cpuinfo | grep 'model name'").read()
        return hard.split("\n")[0].split(":")[1].strip()
    
    def getGPUInfo(self):
        hard = os.popen("lspci | grep VGA").read()
        return hard.split("\n")[0].split(":")[2].strip()
    
    def getOSName(self):
        name = os.popen("grep -E '^(NAME)=' /etc/os-release").read()
        return name.split("=")[1].strip().replace('"', '')