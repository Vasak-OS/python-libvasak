import pytest
from unittest.mock import patch
from Vasak.application.vsk_package_manager import VSKPackageManager

@patch('os.path.exists')
def test_locked_when_file_exists(mock_exists):
    mock_exists.return_value = True
    assert VSKPackageManager.locked() == True
    mock_exists.assert_called_once_with('/var/lib/pacman/db.lck')

@patch('os.path.exists')
def test_locked_when_file_does_not_exist(mock_exists):
    mock_exists.return_value = False
    assert VSKPackageManager.locked() == False
    mock_exists.assert_called_once_with('/var/lib/pacman/db.lck')