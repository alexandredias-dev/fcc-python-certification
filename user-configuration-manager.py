# Passo 1: Criando o dicionário de teste com valores iniciais
test_settings = {
    'theme': 'dark',
    'language': 'portuguese',
    'notifications': 'enabled'
}

# Passo 2: Função para ADICIONAR uma configuração
def add_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# Passo 3: Função para ATUALIZAR uma configuração existente
def update_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()
    
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

# Passo 4: Função para DELETAR uma configuração
def delete_setting(settings, key):
    key = key.lower()
    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

# Passo 5: Função para VISUALIZAR todas as configurações formatadas
def view_settings(settings):
    if not settings:
        return "No settings available."
    
    output = "Current User Settings:\n"
    for key, value in settings.items():
        # .capitalize() deixa a primeira letra maiúscula para o relatório
        output += f"{key.capitalize()}: {value}\n"
    
    return output