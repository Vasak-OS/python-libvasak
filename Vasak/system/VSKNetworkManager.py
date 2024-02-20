import os
import re

from Vasak.system.VSKIconManager import VSKIconManager

class VSKNetworkManager:
    def __init__(self):
        self.iconManager = VSKIconManager()
        self.defaultNetworkInterface = ''
        self.defaultNetworkType = ''
        self.defaultNetworkName = ''
        self.defaultNetworkStatus = False
        self.defaultNetworkIcon = ''
        self.ip = ''
    
    def getDefaultNetworkInterface(self):
        return self.defaultNetworkInterface
    
    def updateStatus(self):
        self.setDefaultNetworkInterface()
        
        data = re.sub(
            r"\s+",
            " ",
            os.popen("nmcli device status 2> /dev/null | grep " + self.defaultNetworkInterface).read(),
            0).split(" ")
        data.pop()

        self.defaultNetworkType = data[1]
        self.defaultNetworkName = " ".join(map(str,data[slice(3, data.__len__())]))
        self.updateNetworkStatus()
        self.updateNetworkIcon()

    def setDefaultNetworkInterface(self):
        data = os.popen("ip route 2> /dev/null | grep default").read().split(" ")
        if (data[0] == 'none' and data[5]):
            self.defaultNetworkInterface = data[5]
        else: 
            self.defaultNetworkInterface = data[4]

        self.ip = data[8]
        
    def updateNetworkStatus(self):
        if (os.popen("cat /sys/class/net/" + self.defaultNetworkInterface + "/operstate").read() == "up\n"):
            self.defaultNetworkStatus = True
        else:
            self.defaultNetworkStatus = False

    def updateNetworkIcon(self):
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
            "icon": self.defaultNetworkIcon,
            "ip": self.ip
        }
    
    def getAllWifiNetworks(self):
        return os.popen("nmcli device wifi list").read().split("\n")
    
    def connectToWifi(self, ssid, password):
        status = os.popen("nmcli device wifi connect " + ssid + " password " + password).read()
        self.updateStatus()
        return status