from classUser import User

admin = User("admin", "P@$$w0rd", "administrador")
admin.login("admin", "P@$$w0rd")
admin.alterarSenha("admin", "12345")
admin.login("admin", "12345")
