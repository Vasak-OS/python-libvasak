import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

class VSKNotifyManager():
  def __init__(self):
    Notify.init("VasakOS")
    self.notify = Notify.Notification.new

  def show(self, title, message, type = "dialog-information"):
    self.notify(title, message, type).show()