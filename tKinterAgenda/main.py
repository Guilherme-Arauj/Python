import tkinter as tk
from tkinter import simpledialog, messagebox
from db_manager import DatabaseManager

class App:
    def __init__(self, root):
        # Instanciar gerenciador de banco de dados
        self.db = DatabaseManager(
            host="localhost",
            user="eclipse",
            password="1234",
            database="pythonsql"
        )
        
        # Configurar janela principal
        self.root = root
        self.root.title("Gerenciador de Usuários")
        
        # Configurar interface
        self.setup_ui()

    def setup_ui(self):
        """Configura os elementos da interface gráfica."""
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="E-mail:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(frame)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Idade:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_age = tk.Entry(frame)
        self.entry_age.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="CPF:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_cpf = tk.Entry(frame)
        self.entry_cpf.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="CEP:").grid(row=4, column=0, padx=5, pady=5)
        self.entry_cep = tk.Entry(frame)
        self.entry_cep.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Gênero:").grid(row=5, column=0, padx=5, pady=5)
        self.entry_gender = tk.Entry(frame)
        self.entry_gender.grid(row=5, column=1, padx=5, pady=5)

        btn_add = tk.Button(frame, text="Adicionar Usuário", command=self.add_user)
        btn_add.grid(row=6, column=0, columnspan=2, pady=10)

        btn_update = tk.Button(frame, text="Atualizar Usuário", command=self.update_user)
        btn_update.grid(row=7, column=0, columnspan=2, pady=10)

        btn_delete = tk.Button(frame, text="Deletar Usuário", command=self.delete_user)
        btn_delete.grid(row=8, column=0, columnspan=2, pady=10)

        self.listbox_users = tk.Listbox(self.root, width=80)
        self.listbox_users.pack(pady=10)
        self.listbox_users.bind('<<ListboxSelect>>', self.load_user_data)

        # Inicializar exibição de usuários
        self.display_users()

    def add_user(self):
        """Adiciona um usuário ao banco de dados."""
        name = self.entry_name.get()
        email = self.entry_email.get()
        age = self.entry_age.get()
        cpf = self.entry_cpf.get()
        cep = self.entry_cep.get()
        gender = self.entry_gender.get()

        if not all([name, email, age, cpf, cep, gender]):
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos!")
            return

        try:
            self.db.insert_user(name, email, age, cpf, cep, gender)
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
            self.clear_entries()
            self.display_users()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível adicionar o usuário: {e}")

    def update_user(self):
        """Atualiza os dados do usuário selecionado."""
        user_id = simpledialog.askinteger("Atualizar Usuário", "Digite o ID do usuário que deseja atualizar:")

        if user_id is None:
            return

        field = simpledialog.askstring("Campo para Atualizar", "Digite o campo que deseja atualizar (name, email, age, cpf, cep, gender):")
        
        if field not in ["name", "email", "age", "cpf", "cep", "gender"]:
            messagebox.showwarning("Erro", "Campo inválido!")
            return

        value = simpledialog.askstring("Novo Valor", f"Digite o novo valor para {field}:")

        if value is None:
            return

        try:
            self.db.update_user_field(user_id, field, value)
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
            self.display_users()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível atualizar o usuário: {e}")

    def delete_user(self):
        """Deleta um usuário do banco de dados."""
        user_id = simpledialog.askinteger("Deletar Usuário", "Digite o ID do usuário que deseja deletar:")

        if user_id is None:
            return

        try:
            self.db.delete_user(user_id)
            messagebox.showinfo("Sucesso", "Usuário deletado com sucesso!")
            self.display_users()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível deletar o usuário: {e}")

    def load_user_data(self, event):
        """Carrega os dados do usuário selecionado nos campos de entrada."""
        try:
            selected_user_index = self.listbox_users.curselection()[0]
            selected_user = self.users[selected_user_index]

            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, selected_user[1])

            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, selected_user[2])

            self.entry_age.delete(0, tk.END)
            self.entry_age.insert(0, selected_user[3])

            self.entry_cpf.delete(0, tk.END)
            self.entry_cpf.insert(0, selected_user[4])

            self.entry_cep.delete(0, tk.END)
            self.entry_cep.insert(0, selected_user[5])

            self.entry_gender.delete(0, tk.END)
            self.entry_gender.insert(0, selected_user[6])
        except IndexError:
            pass

    def display_users(self):
        """Exibe os usuários cadastrados na lista."""
        self.users = self.db.fetch_users()
        self.listbox_users.delete(0, tk.END)
        for user in self.users:
            self.listbox_users.insert(tk.END, f"ID: {user[0]} - {user[1]} ({user[2]}), Idade: {user[3]}, CPF: {user[4]}, CEP: {user[5]}, Gênero: {user[6]}")

    def clear_entries(self):
        """Limpa todos os campos de entrada."""
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_cep.delete(0, tk.END)
        self.entry_gender.delete(0, tk.END)


# Inicializar aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
