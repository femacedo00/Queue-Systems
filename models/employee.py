# Classe com as informações do funcionário
class Employees:
    def __init__(self, employee):
        self.id = employee
        self.end_service = 0 # Horário do último atendimento do funcionário
        self.services = 0 # Quantidades de atendimento que o funcionário
    
    def __str__(self): # Método para printar a classe
        return (
            f"--- Funcionário: {self.id} ---\n"
            f" Quantidade de atendimentos: {self.services}\n"
        )