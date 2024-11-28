import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.connection = self.create_connection()
        self.create_table()

    def create_connection(self):
        """Estabelece a conexão com o banco de dados."""
        return mysql.connector.connect(**self.config)

    def create_table(self):
        """Cria a tabela de usuários, caso não exista."""
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                age INT NOT NULL,
                cpf VARCHAR(14) NOT NULL UNIQUE,
                cep VARCHAR(9) NOT NULL,
                gender VARCHAR(20) NOT NULL
            )
        """)
        self.connection.commit()

    def insert_user(self, name, email, age, cpf, cep, gender):
        """Insere um novo usuário no banco de dados."""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, age, cpf, cep, gender) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, email, age, cpf, cep, gender)
        )
        self.connection.commit()

    def fetch_users(self):
        """Busca todos os usuários cadastrados."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

    def update_user_field(self, user_id, field, value):
        """Atualiza um campo específico de um usuário no banco de dados."""
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            UPDATE users
            SET {field} = %s
            WHERE id = %s
            """,
            (value, user_id)
        )
        self.connection.commit()

    def delete_user(self, user_id):
        """Remove um usuário do banco de dados."""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.connection.commit()

    def __del__(self):
        """Fecha a conexão com o banco de dados ao destruir a instância."""
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()
