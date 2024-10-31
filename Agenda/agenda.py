import csv
from datetime import datetime

class Contato:
    def __init__(self, nome, telefone, endereco, aniversario, outras_infos=""):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.aniversario = aniversario  # Data no formato "dd-mm-yyyy"
        self.outras_infos = outras_infos

class Agenda:
    def __init__(self, arquivo='contatos.csv'):
        self.contatos = []
        self.arquivo = arquivo
        self.carregar_contatos()
        
    def carregar_contatos(self):
        try:
            with open(self.arquivo, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for linha in reader:
                    if linha:
                        nome, telefone, endereco, aniversario, outras_infos = linha
                        self.contatos.append(Contato(nome, telefone, endereco, aniversario, outras_infos))
        except FileNotFoundError:
            print("Arquivo de contatos não encontrado. Criando novo arquivo.")
    
    def grava(self):
        with open(self.arquivo, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for contato in self.contatos:
                writer.writerow([contato.nome, contato.telefone, contato.endereco, contato.aniversario, contato.outras_infos])

    def apaga(self, nome):
        self.contatos = [c for c in self.contatos if c.nome != nome]
        self.grava()

    def altera(self, nome, novo_contato):
        for idx, contato in enumerate(self.contatos):
            if contato.nome == nome:
                self.contatos[idx] = novo_contato
                self.grava()
                return
        print("Contato não encontrado.")

    def lista(self):
        contatos_ordenados = sorted(self.contatos, key=lambda c: c.nome)
        for idx, contato in enumerate(contatos_ordenados):
            print(f"{idx + 1}. {contato.nome} - {contato.telefone} - {contato.endereco} - Aniversário: {contato.aniversario}")

    def le(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                print(f"Nome: {contato.nome}\nTelefone: {contato.telefone}\nEndereço: {contato.endereco}\nAniversário: {contato.aniversario}")
                return
        print("Contato não encontrado.")

    def verificarbirthday(self):
        hoje = datetime.now().strftime("%d-%m")
        aniversariantes = [c.nome for c in self.contatos if c.aniversario.startswith(hoje)]
        if aniversariantes:
            print("Hoje é aniversário de:", ", ".join(aniversariantes))
        else:
            print("Nenhum aniversário hoje.")

    def menu(self):
        while True:
            print("\nAgenda de Contatos")
            print(f"Total de contatos: {len(self.contatos)}")  # Exibe o tamanho da agenda
            print("1. Exibir contatos")
            print("2. Adicionar contato")
            print("3. Apagar contato")
            print("4. Alterar contato")
            print("5. Procurar contato")
            print("6. Ordenar lista por nome")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.lista()
            elif opcao == "2":
                self.adicionar()
            elif opcao == "3":
                nome = input("Nome do contato a ser apagado: ")
                self.apaga(nome)
            elif opcao == "4":
                nome = input("Nome do contato a ser alterado: ")
                novo_contato = self.novo_contato(nome)
                self.altera(nome, novo_contato)
            elif opcao == "5":
                nome = input("Nome do contato a ser buscado: ")
                self.le(nome)
            elif opcao == "6":
                self.contatos.sort(key=lambda c: c.nome)
                print("Contatos ordenados por nome.")
            elif opcao == "7":
                break
            else:
                print("Opção inválida.")

    def adicionar(self):
        nome = input("Nome: ")
        if any(c.nome == nome for c in self.contatos):
            print("Erro: Já existe um contato com esse nome.")
            return
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        aniversario = input("Data de aniversário (dd-mm-yyyy): ")
        outras_infos = input("Outras informações: ")
        novo_contato = Contato(nome, telefone, endereco, aniversario, outras_infos)
        self.contatos.append(novo_contato)
        self.grava()

    def novo_contato(self, nome):
        telefone = input("Novo Telefone: ")
        endereco = input("Novo Endereço: ")
        aniversario = input("Nova Data de Aniversário (dd-mm-yyyy): ")
        outras_infos = input("Novas Outras Informações: ")
        return Contato(nome, telefone, endereco, aniversario, outras_infos)

# Executando a aplicação
agenda = Agenda()
agenda.verificarbirthday()  # Notifica aniversariantes ao abrir a agenda
agenda.menu()
