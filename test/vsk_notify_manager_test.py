import pytest
from unittest.mock import patch, Mock
from Vasak.application.vsk_notify_manager import VSKNotifyManager

@patch('gi.repository.Notify.Notification.new')
@patch('gi.repository.Notify.init')
def test_init(mock_notify_init, mock_notify_new):
    vsk_notify_manager = VSKNotifyManager()
    mock_notify_init.assert_called_once_with("VasakOS")
    assert vsk_notify_manager.notify == mock_notify_new
