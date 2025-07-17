import traceback
import keyboard
from Service.requisicoes import ClockifyClient
from Utils.nomes_personalizados import padronizar_titulo
from time import sleep
from Model.obter_janela import  retornar_nome_processo_janela_ativa
  
def auto_time_tracker(clockify_client: ClockifyClient):
    janela_anterior = None
    print("Começando rastreamento automático...")

    while True:
        try:
            # Caso aperte ou segura shift+F8, encerra o Tracker
            if keyboard.is_pressed("shift+F8"):
                print("Encerrando o rastreamento...")
                clockify_client.stop_active_time_entry()
                break

            sleep(0.25)

            janela = retornar_nome_processo_janela_ativa()
            titulo_padronizado = padronizar_titulo(janela)

            # Verificação para evitar erros e continuar o loop
            if not titulo_padronizado:
                continue
            
            # Se o nome do processo for diferente do anterior, cria um novo entry com o novo processo
            if titulo_padronizado != janela_anterior:
                clockify_client.stop_active_time_entry()
                clockify_client.create_time_entry(titulo_padronizado)
                janela_anterior = titulo_padronizado

        # Sinalizar que foi encerrado manualmente
        except KeyboardInterrupt:
            print("Rastreamento interrompido manualmente.")
            clockify_client.stop_active_time_entry()
            break

        except Exception:
            print("Ocorreu um erro durante o rastreamento automático:")
            traceback.print_exc()
            clockify_client.stop_active_time_entry()
            break





