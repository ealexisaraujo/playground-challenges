from importlib import reload, import_module
import shutil

def reload_module(name):
  module = import_module(name)
  shutil.rmtree("__pycache__", ignore_errors=True)
  reload(module)
  return module

def test_many_countries(capfd):
    reload_module('exercise')
    expected_str = "{'ARG', 'USA', 'CANADA', 'GT', 'COL', 'MX', 'BZ'}\n"
    out, error = capfd.readouterr()
    assert out  == expected_str