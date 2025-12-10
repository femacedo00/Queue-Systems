import math

# Classe com as informações do cliente
class Client:
    def __init__(self, client, num_tec, num_ts):
        self.id = client # Cliente atendido
        self.is_client_in_time = False # Bool para sabermos se o cliente foi atendido dentro do tempo de funcionamento
        self.employee = -1 # Funcionário que atendeu
        self.arrival_clock = 0 # Horário de chegada
        self.service_start = 0 # Horário em que o atendimento começa
        self.service_end = 0 # Horário em que o atendimento termina
        self.queue = 0 # Tempo na fila
        self.system_time = 0 # Tempo total no sistema (na fila + atendimento)
        self.tec = self.calculate_tec(num_tec) # Calculando TEC
        self.ts = self.calculate_ts(num_ts) # Calculando TS
        self.employee_idle = 0 # Tempo que o funcionário passou ocioso antes de atender o cliente
    
    @staticmethod
    def calculate_tec(num_tec):
        return round(-math.log(num_tec) / 0.6, 4) # Tempos entre as chegadas
    
    @staticmethod
    def calculate_ts(num_ts):
        return round(-math.log(num_ts) / 0.4 + 0.3, 4) # Tempos de serviço
    
    def __str__(self): # Método para printar a classe
        return (
            f"--- Atendimento (Cliente: {self.id}) ---\n"
            f"  Funcionário que atendeu: {self.employee}\n"
            f"  TEC: {self.tec}\n"
            f"  TS:  {self.ts}\n"
            f"  Chegada no relógio: {self.arrival_clock}\n"
            f"  Início do Serviço: {self.service_start}\n"
            f"  Fim do Serviço: {self.service_end}\n"
            f"  Tempo na fila: {self.queue}\n"
            f"  Tempo no sistema: {self.system_time}\n"
            f"  Tempo ocioso do funcionário: {self.employee_idle}\n"
        )