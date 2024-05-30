import os
import pytest
from Vasak.application.vsk_javascript import VSKJavaScript

def setup_function():
    global vsk
    vsk = VSKJavaScript('test_page')

def test_is_file_or_string_with_string():
    script = "console.log('Hello, World!');"
    result = vsk._is_file_or_string(script)
    assert result == script

def test_is_file_or_string_with_existing_file():
    script = "./test_script.js"
    with open(script, 'w') as file:
        file.write("console.log('Hello, World!');")
    expected = "console.log('Hello, World!');"
    result = vsk._is_file_or_string(script)
    assert result == expected
    os.remove(script)
