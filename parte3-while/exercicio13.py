## 13. Peça uma senha ao usuário e continue pedindo até que ele digite senai123. Ao acertar, exiba "Acesso liberado".

senha_correta = "senai123"
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado.")
        break
    else:
        print("Senha incorreta. Tente novamente.")