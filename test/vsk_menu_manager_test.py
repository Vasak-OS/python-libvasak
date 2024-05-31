import pytest
from unittest.mock import patch, MagicMock
from Vasak.system.vsk_menu_manager import VSKMenuManager

def test_fix_description():
    vsk_menu_manager = VSKMenuManager()
    description = "This is a 'description'"
    fixed_description = vsk_menu_manager.fix_description(description)
    assert fixed_description == "This is a  description "