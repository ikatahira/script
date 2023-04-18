#!/usr/bin/env python3

import subprocess

# Define o nome de usuário e senha para o novo usuário
new_user_name = "john.doe"
new_user_password = "password123"

# Cria o novo usuário do sistema
subprocess.run(["sudo", "useradd", new_user_name])
subprocess.run(["sudo", "passwd", new_user_name], input=f"{new_user_password}\n{new_user_password}\n".encode())