def validar_email(email):
    return '@' in email

def cadastrar_usuario(nome, email):
    if not validar_email(email):
        raise ValueError('email invalido')
    return {'nome': nome, 'email': email}

