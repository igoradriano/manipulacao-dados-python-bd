from cefpython3 import cefpython as cef
import platform
import sys
def main():
    check_versions()
    sys.excepthook = cef.ExceptHook # Isso é necessário para que todos os processos CEF sejam encerrados em caso de erro
    cef.Initialize() #Inicializa o CefSharp com configurações fornecidas pelo usuário. É importante observar que Initialize / Shutdown DEVE ser chamado no thread do aplicativo principal (normalmente o cabeçalho da IU)
    cef.CreateBrowserSync(url="https://www.google.com/",
        window_title="Olá, mundo! Este é o primeiro exemplo do CEF Python")
    cef.MessageLoop() # garante que o navegador continue aberto, se nao abre e fecha imediatamente
    cef.Shutdown()# Encerra o CefSharp e a infraestrutura CEF subjacente. É seguro chamar esse método várias vezes; ele encerrará apenas o CEF na primeira chamada (todas as chamadas subsequentes serão ignoradas). Esta função deve ser chamada no encadeamento principal do aplicativo para encerrar o processo do navegador CEF antes que o aplicativo seja encerrado.

def check_versions():
    ver = cef.GetVersion()
    print(f"[hello_world.py] CEF Python {ver['version']}")
    print(f"[hello_world.py] Chromium {ver['chrome_version']}")
    print(f"[hello_world.py] CEF {ver['cef_version']}")
    print(f"[hello_world.py] Python {platform.python_version()} {platform.architecture()[0]}")
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"


if __name__ == '__main__':
    main()