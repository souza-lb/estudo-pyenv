# Este trecho de código foi obtido em:
# https://github.com/cztomczak/cefpython/blob/master/examples/hello_world.py
# Desenvolvedor original: Czarek Tomczak
# Tradução e adaptação: Leonardo Bruno.

from cefpython3 import cefpython as cef
import platform
import sys


def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # para derrubar todos o processos cef em caso de erro.
    cef.Initialize()
    cef.CreateBrowserSync(url="https://duckduckgo.com/",
                          window_title="Ola Mundo!")
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[teste-cefpython3.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[teste-cefpython3.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[teste-cefpython3.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[teste-cefpython3.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "66.0", "Requer a versão 66.0 para rodar!"


if __name__ == '__main__':
    main()
