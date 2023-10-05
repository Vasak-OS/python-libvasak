import os
import re

from Vasak.VSKIconManager import VSKIconManager

class VSKNetworkManager:
    def __init__(self):
        self.iconManager = VSKIconManager()
        self.defaultNetworkInterface = ''
        self.defaultNetworkType = ''
        self.defaultNetworkName = ''
        self.defaultNetworkStatus = False
        self.defaultNetworkIcon = ''
    
    def getDefaultNetworkInterface(self):
        return self.defaultNetworkInterface
    
    def updateStatus(self):
        data = os.popen("ip route 2> /dev/null | grep default").read().split(" ")
        if (data[0] == 'none' and data[5]):
            self.defaultNetworkInterface = data[5]
        else: 
            self.defaultNetworkInterface = data[4]
        
        data = re.sub(
            r"\s+",
            " ",
            os.popen("nmcli device status 2> /dev/null | grep " + self.defaultNetworkInterface).read(),
            0).split(" ")
        data.pop()

        self.defaultNetworkType = data[1]
        self.defaultNetworkName = " ".join(map(str,data[slice(3, data.__len__())]))

        if (os.popen("cat /sys/class/net/" + self.defaultNetworkInterface + "/operstate").read() == "up\n"):
            self.defaultNetworkStatus = True
        
        if(self.defaultNetworkType == 'ethernet'):
            if(self.defaultNetworkStatus):
                self.defaultNetworkIcon = self.iconManager.get_icon('network-wired-symbolic')
            else:
                self.defaultNetworkIcon = self.iconManager.get_icon('network-wired-disconnected-symbolic')
        elif(self.defaultNetworkType == 'wifi'):
            if(self.defaultNetworkStatus):
                #TODO: Add Wifi Signal icons
                self.defaultNetworkIcon = self.iconManager.get_icon('network-wireless-connected-symbolic')
            else:
                self.defaultNetworkIcon = self.iconManager.get_icon('network-wireless-disconnected-symbolic')

    def getDefaultConnectionData(self):
        return {
            "interface": self.defaultNetworkInterface,
            "type": self.defaultNetworkType,
            "name": self.defaultNetworkName,
            "connected": self.defaultNetworkStatus,
            "icon": self.defaultNetworkIcon
        }
        
