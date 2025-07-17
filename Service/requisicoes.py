import requests
from datetime import datetime, timezone
from Model.meu_usuario import json_para_meu_user
from Utils.obter_chave import minha_chave
from Utils.converter_horario import convert_to_br 
from typing import Optional


class ClockifyClient:
    def __init__(self, chave_api: Optional[str] = None):
        self.chave_api = chave_api or minha_chave()
        self.url = "https://api.clockify.me/api/v1"
        self.headers = {
            "Content-Type": "application/json",
            "X-Api-Key": self.chave_api
        }
    
    
    # Realiza as chamdas da API
    def _call_request(self, endpoint: str) -> tuple[str, dict[str, str]]:
        url = f"{self.url}/{endpoint}"
        
        return url, self.headers
    
    # Automatiza o GET
    def _get(self, endpoint: str) -> dict:
        url, headers = self._call_request(endpoint)

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()
    

    # Automatiza o POST
    def _post(self, endpoint: str, data: dict) -> dict:
        url, headers = self._call_request(endpoint)

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        return response.json()
    

    # Automatiza o PATCH
    def _patch(self, endpoint: str, data: dict) -> requests.Response:
        url, headers = self._call_request(endpoint)
        
        response = requests.patch(url, headers=headers, json=data)
        response.raise_for_status()

        return response
    

    # Retorna informações do usuário (GET)
    def get_user_info(self) -> dict:
        return self._get("user")
    

    # Retorna valor booleano caso tenha um time entry ativo
    def tem_entry_ativa(self) -> bool:
        usuario = json_para_meu_user(self.get_user_info())
        workspace_id = usuario.activeWorkspace
        endpoint = f"workspaces/{workspace_id}/time-entries/status/in-progress"
        entries = self._get(endpoint)
        return bool(entries)
    

    # Retorna o time entry ativo e o horário do início(UTC São Paulo) (GET)
    def get_active_time_entry(self) -> str:
        usuario = json_para_meu_user(self.get_user_info())
        workspace_id = usuario.activeWorkspace
        endpoint = f"workspaces/{workspace_id}/time-entries/status/in-progress"
        entries = self._get(endpoint)

        if not self.tem_entry_ativa():
            return "Nenhum time entry ativo"
        
        entry = entries[0]
        description = entry.get("Descrição") or "Sem descrição"
        start_iso = entry.get("TimeInterval", {}.get("start"))

        try:
            start_formatado = convert_to_br(start_iso)
        except Exception as erro:
            start_formatado = f"(erro: {erro})"
        
        return f"Nome do time entry: {description} | Início: {start_formatado}"
    

    # Cria um time entry (POST)
    def create_time_entry(self, nome_janela: str) -> str:
        usuario = json_para_meu_user(self.get_user_info())
        workspace_id = usuario.activeWorkspace
        endpoint = f"workspaces/{workspace_id}/time-entries"
        start_time_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

        data = {
            "start": start_time_utc,
            "description": nome_janela,
            "billable": False
        }

        entry = self._post(endpoint, data)
        start_formatado = convert_to_br(entry["timeInterval"]["start"])
        return f"Novo time entry criado para: '{nome_janela}' às {start_formatado}"
    
    
    # Para o time entry que está ativo (PATCH)
    def stop_active_time_entry(self) -> str:
        if not self.tem_entry_ativa():
            return "nenhuma entrada ativa no momento."
        
        usuario = json_para_meu_user(self.get_user_info())
        workspace_id = usuario.activeWorkspace
        user_id = usuario.id

        endpoint = f"workspaces/{workspace_id}/user/{user_id}/time-entries"
        end_time = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        data = {"end": end_time}

        try:
            res = self._patch(endpoint, data)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400:
                return "Nenhuma entrada de tempo ativa para encerrar."
            raise res

        return f"Entrada de tempo encerrada às {convert_to_br(end_time)}."


