from datetime import datetime, timezone
import pytz

def convert_to_br(iso_utc_str):
    if not iso_utc_str:
        return '[sem horário]'

    # Trata o formato com 'Z'
    if iso_utc_str.endswith('Z'):
        iso_utc_str = iso_utc_str.replace('Z', '')

    utc_time = datetime.fromisoformat(iso_utc_str)

    # Se não tem tzinfo, adiciona UTC
    if utc_time.tzinfo is None:
        utc_time = pytz.utc.localize(utc_time)

    # Converte para horário de Brasília
    br_tz = pytz.timezone("America/Sao_Paulo")
    br_time = utc_time.astimezone(br_tz)

    return br_time.strftime('%d/%m/%Y %H:%M:%S')


def horario_agora_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
