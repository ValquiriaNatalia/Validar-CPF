import json
import re

def carregar_usuarios():
    with open("usuarios.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    return True

def autenticar(cpf, senha):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
            return True
    return False

def executar():
    print("=" * 35)
    print("       SISTEMA DE LOGIN")
    print("=" * 35)

    cpf = input("Digite seu CPF: ")
    cpf = re.sub(r"\D", "", cpf)

    if not validar_cpf(cpf):
        print("\nCPF inválido!")
        return

    senha = input("Digite sua senha: ")

    if not senha:
        print("\nA senha não pode estar vazia!")
        return

    if autenticar(cpf, senha):
        print("\nLogin realizado com sucesso!")
        print("Bem-vindo ao sistema!")
    else:
        print("\nCPF ou senha incorretos!")


if __name__ == "__main__":
    executar()