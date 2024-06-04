import pytest
from unittest.mock import patch, MagicMock
from Vasak.system.vsk_power_manager import VSKPowerManager

@patch('Vasak.application.vsk_package_manager.VSKPackageManager.locked')
@patch('Vasak.application.vsk_shell_connector.VSKShellConnector.run')
def test_logout(mock_run, mock_locked):
    mock_locked.return_value = False
    VSKPowerManager.logout()
    mock_run.assert_called_once_with('loginctl terminate-session $XDG_SESSION_ID', shell=True)

@patch('Vasak.application.vsk_package_manager.VSKPackageManager.locked')
@patch('Vasak.application.vsk_shell_connector.VSKShellConnector.run')
def test_poweroff(mock_run, mock_locked):
    mock_locked.return_value = False
    VSKPowerManager.poweroff()
    mock_run.assert_called_once_with(['systemctl', 'poweroff'])

@patch('Vasak.application.vsk_package_manager.VSKPackageManager.locked')
@patch('Vasak.application.vsk_shell_connector.VSKShellConnector.run')
def test_reboot(mock_run, mock_locked):
    mock_locked.return_value = False
    VSKPowerManager.reboot()
    mock_run.assert_called_once_with(['systemctl', 'reboot'])

@patch('Vasak.application.vsk_package_manager.VSKPackageManager.locked')
@patch('Vasak.application.vsk_shell_connector.VSKShellConnector.run')
def test_suspend(mock_run, mock_locked):
    mock_locked.return_value = False
    VSKPowerManager.suspend()
    mock_run.assert_called_once_with(['systemctl', 'suspend'])

@patch('Vasak.application.vsk_shell_connector.VSKShellConnector.run')
def test_lock(mock_run):
    VSKPowerManager.lock()
    mock_run.assert_called_once_with(['loginctl', 'lock-session'])