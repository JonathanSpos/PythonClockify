import win32gui
import win32process
import psutil

def obter_janela_foco() -> int:
    janela_ativa = win32gui.GetForegroundWindow() # Obtém a janela em foco.
    
    if not janela_ativa: # Ignora caso não tenha janela ativa para evitar erros.
        return None
    return janela_ativa


def obter_pid_janela(handle):
    if not handle:
        return None, None # Retorna vazio o handle e o pid. Handle é necessario para encontrar o pid.

    handle = obter_janela_foco()
    _, pid = win32process.GetWindowThreadProcessId(handle) # Coleta o pid da janela.
    return _, pid


def obter_nome_processo_pid(pid):
    # Retorna o nome do processa dado o PID.

    try:
        processo = psutil.Process(pid)
        return processo.name()
    
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return None


def retornar_nome_processo_janela_ativa() -> str:
    # Retorna o nome do processo da janela em foco.
    janela = obter_janela_foco()
    _, pid = obter_pid_janela(janela)
    if pid is None:
        return None
    return obter_nome_processo_pid(pid)



