
def padronizar_titulo(titulo): # Remove o ".exe" do processo ativo coletado e padroniza para o Clockify.
    """
    Remove o sufixo '.exe' (independente de maiúsculas) do nome do processo
    e retorna o nome com a primeira letra maiúscula.
    """
    if not titulo:
        return None

    nome_limpo = titulo.lower().removesuffix(".exe")
    return nome_limpo.capitalize() # Deixa a primeira letra do processo em maiúsculo

