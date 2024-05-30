import os
import time
from Vasak.application.vsk_notify_manager import VSKNotifyManager
from Vasak.application.vsk_package_manager import VSKPackageManager
from Vasak.application.vsk_shell_connector import VSKShellConnector

class VSKPowerManager():
  def __init__(self):
    self.desktop_session = os.environ.get('DESKTOP_SESSION')

  @staticmethod
  def logout():
    if not VSKPackageManager.locked():
      VSKShellConnector.run('loginctl terminate-session $XDG_SESSION_ID', shell=True)
    else:
      VSKNotifyManager.show("Warnning", "Cannot log out, instalation or update in progress.")

  @staticmethod
  def poweroff():
    if not VSKPackageManager.locked():
      VSKShellConnector.run(['systemctl', 'poweroff'])
    else:
      VSKNotifyManager.show("Information", "Instalation or update in progress, your session is scheduled to shutdown, locking in 30s Goodbye.")
      time.sleep(30)
      VSKPowerManager.lock()
      while VSKPackageManager.locked():
        time.sleep(1)
      VSKPowerManager.powerOff()
  
  @staticmethod
  def reboot():
    if not VSKPackageManager.locked():
      VSKShellConnector.run(['systemctl', 'reboot'])
    else:
      VSKNotifyManager.show("Information", "Instalation or update in progress, your session is scheduled to reboot, locking in 10s Goodbye.")
      time.sleep(10)
      VSKPowerManager.lock()
      while VSKPackageManager.locked():
        time.sleep(1)
      VSKPowerManager.reboot()

  @staticmethod
  def suspend():
    if not VSKPackageManager.locked():
      VSKShellConnector.run(['systemctl', 'suspend'])
    else:
      VSKNotifyManager.show("Information", "Instalation or update in progress, your session is scheduled to suspend, locking in 10s Goodbye.")
      time.sleep(10)
      VSKPowerManager.lock()
      while VSKPackageManager.locked():
        time.sleep(1)
      VSKPowerManager.suspend()
  
  @staticmethod
  def lock():
    VSKShellConnector.run(['loginctl', 'lock-session'])