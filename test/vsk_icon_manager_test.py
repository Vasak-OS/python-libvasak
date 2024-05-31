import pytest
from unittest.mock import patch, MagicMock
from Vasak.system.vsk_icon_manager import VSKIconManager

@patch('os.path.isfile')
@patch('gi.repository.Gtk.IconTheme.get_default')
def test_get_icon(mock_get_default, mock_isfile):
    mock_icon_theme = MagicMock()
    mock_icon_theme.has_icon.return_value = False
    mock_get_default.return_value = mock_icon_theme
    mock_isfile.return_value = False
    vsk_icon_manager = VSKIconManager()
    vsk_icon_manager.get_icon('test_icon')
    mock_get_default.assert_called_once()
    mock_isfile.assert_called()

@patch('os.path.isfile')
@patch('gi.repository.Gtk.IconTheme.get_default')
def test_get_icon_with_full_path(mock_get_default, mock_isfile):
    mock_icon_theme = MagicMock()
    mock_icon_theme.has_icon.return_value = False
    mock_get_default.return_value = mock_icon_theme
    mock_isfile.return_value = False
    vsk_icon_manager = VSKIconManager()
    icon = vsk_icon_manager.get_icon('/path/to/test_icon.png')
    assert icon == '/path/to/test_icon.png'
    mock_get_default.assert_not_called()
    mock_isfile.assert_not_called()