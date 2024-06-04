import pytest
from unittest.mock import patch, MagicMock
from Vasak.system.vsk_network_manager import VSKNetworkManager

@patch('os.popen')
def test_update_network_status(mock_popen):
    vsk_network_manager = VSKNetworkManager()
    vsk_network_manager.defaultNetworkInterface = 'eth0'
    mock_popen.return_value.read.return_value = 'up\n'
    vsk_network_manager.updateNetworkStatus()
    assert vsk_network_manager.defaultNetworkStatus == True
    mock_popen.assert_called_once_with("cat /sys/class/net/eth0/operstate")

@patch('os.popen')
def test_get_all_wifi_networks(mock_popen):
    mock_popen.return_value.read.return_value = 'SSID1\nSSID2\n'
    vsk_network_manager = VSKNetworkManager()
    wifi_networks = vsk_network_manager.getAllWifiNetworks()
    assert wifi_networks == ['SSID1', 'SSID2', '']
    mock_popen.assert_called_once_with("nmcli device wifi list")