from datetime import datetime 
import pytz


def convert_to_br(iso_utc_str):
    if not iso_utc_str:
        return '[sem horário]'

    # Remove o "Z" e adiciona o offset UTC se necessário
    if iso_utc_str.endswith('Z'):
        iso_utc_str = iso_utc_str.replace('Z', '+00:00')

    utc_time = datetime.fromisoformat(iso_utc_str)

    # Define os fusos horários
    br_tz = pytz.timezone("America/Sao_Paulo")
    utc_time = utc_time.astimezone(pytz.utc)
    br_time = utc_time.astimezone(br_tz)

    return br_time.strftime('%d/%m/%Y %H:%M:%S')