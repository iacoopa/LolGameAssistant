from distutils.core import setup
import py2exe

setup(
      options = {
        "py2exe": {
            "dll_excludes": ["MSVCP90.dll"]
        }
    },
      windows=['D:\workspace\LolGameAssistant\emptybox\ItemChanger.py']
      )