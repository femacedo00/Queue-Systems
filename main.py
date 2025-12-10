from config.constants import Constants
from controllers.StatisticalAnalyzer import StatisticalAnalyzer
from controllers.generator import Pseudorandom
from models.client import Client
from models.employee import Employees

def main():
    # Trazendo valores constantes do sistema
    constants = Constants()
    seed = constants.first_seed # Semente atual
    
    # Instanciando variáveis para análise de métricas
    tec = StatisticalAnalyzer("Tempo entre chegadas")
    ts = StatisticalAnalyzer("Início de atendimento")
    service_start = StatisticalAnalyzer("Início do serviço")
    service_end = StatisticalAnalyzer("Fim do serviço")
    queue = StatisticalAnalyzer("Tempo na fila")
    system_time = StatisticalAnalyzer("Tempo no sistema")
    employee_idle = StatisticalAnalyzer("Tempo ocioso do funcionário")
    employee_services = [StatisticalAnalyzer(f"Clientes atendidos pelo funcionário {employee + 1}") for employee in range(constants.num_employees)]
    clients_served = StatisticalAnalyzer("Total de clientes atendidos")
    
    # Laço para gerar valores de todas as sementes
    while(seed < constants.first_seed + constants.num_seeds):
        print("-" * 50)
        print(" SEMENTE: ", seed)
        print("-" * 50)
        random_nums = Pseudorandom(constants.num_clients * 2, seed) # Gerando números aleatorios para o cálculo do tec e ts
        seed += 1
        
        random_num_tec = random_nums.generated_numbers[:constants.num_clients] # Coletando os números aleatórios para tec
        random_num_ts = random_nums.generated_numbers[-constants.num_clients:] # Coletando os números aleatórios para ts
        
        clients = [Client(client + 1, random_num_tec[client], random_num_ts[client]) for client in (range(constants.num_clients))] # Instanciando todos os clientes que poderão ser atendidos dentro do tempo estimado
        employees = [Employees(employee + 1) for employee in range(constants.num_employees)] # Instanciando todos os funcionários que irão atender
        
        previous_arrival_clock = 0 # Tempo de chegada do cliente anterior
        clients_served.count = 0 # Quantidade de cliente que foram atendidos
        
        # Inicializando a soma de tempo de uma seed
        tec.count = 0
        ts.count = 0
        service_start.count = 0
        service_end.count = 0
        queue.count = 0
        system_time.count = 0
        employee_idle.count = 0
        
        # Iniciando o atendimento, na qual será atendido apenas o cliente que chegar a hora limite do estabelecimento
        for client in clients:
            client.arrival_clock = client.tec + previous_arrival_clock # Tempo de chegada no relógio
            previous_arrival_clock = client.arrival_clock
            
            if client.arrival_clock <= constants.operating_time: # Se o cliente está no horário de funcionamento, ele será atendido
                client.is_client_in_time = True # Cliente será atendido
                clients_served.count += 1
                
                employee = min(employees, key=lambda employee: employee.end_service) # O funcionário que terminar primeiro irá atender o próximo cliente 
                employee.services += 1 # O funcionário atendeu + 1
                client.employee = employee.id # Identificando qual funcionário atendeu o cliente
                
                # Tempo do inicio do serviço
                if employee.end_service > client.arrival_clock: # Se o último atendimento do funcionário terminou depois da chegada do cliente, então o cliente estava na fila
                    client.service_start = employee.end_service
                else:
                    client.service_start = client.arrival_clock
                    
                client.service_end = client.service_start + client.ts # Tempo do fim do serviço
                client.queue = client.service_start - client.arrival_clock # Tempo de fila
                client.system_time = client.queue + client.ts # Tempo no sistema
                client.employee_idle = client.service_start - employee.end_service # Tempo ocioso do funcionário
                
                employee.end_service = client.service_end # Tempo do último atendimento para a validação de quem será o próximo a atender
                
                # Somando cada tempo para o cálculo da média
                tec.count += client.tec
                ts.count += client.ts
                service_start.count += client.service_start
                service_end.count += client.service_end
                queue.count += client.queue
                system_time.count += client.system_time
                employee_idle.count += client.employee_idle
                
                print(client)
                    
            else: # Se não, não haverão mais atendimentos
                break
    
        # Média de quantos clientes cada funcionario atendeu
        for employee in employees:
            id = employee.id - 1
            employee_services[id].count = employee.services
            
            if clients_served.count:
                employee_services[id].avaranges.append(employee_services[id].count / clients_served.count)
            else:
                employee_services[id].avaranges.append(clients_served.count)
            
        # Inserindo a média
        if clients_served.count:
            tec.avaranges.append(tec.count / clients_served.count)
            ts.avaranges.append(ts.count / clients_served.count)
            service_start.avaranges.append(service_start.count / clients_served.count)
            service_end.avaranges.append(service_end.count / clients_served.count)
            queue.avaranges.append(queue.count / clients_served.count)
            system_time.avaranges.append(system_time.count / clients_served.count)
            employee_idle.avaranges.append(employee_idle.count / clients_served.count)
            clients_served.avaranges.append(clients_served.count / constants.num_clients)
        else:
            tec.avaranges.append(clients_served.count)
            ts.avaranges.append(clients_served.count)
            service_start.avaranges.append(clients_served.count)
            service_end.avaranges.append(clients_served.count)
            queue.avaranges.append(clients_served.count)
            system_time.avaranges.append(clients_served.count)
            employee_idle.avaranges.append(clients_served.count)
            clients_served.avaranges.append(clients_served.count)
        
    # Resultados finais
    print("-" * 50)
    print(" MÉTRICAS GERAIS ")
    print("-" * 50)
    
    tec.show_analysis(prefix_filename="tec")
    ts.show_analysis(prefix_filename="ts")
    service_start.show_analysis(prefix_filename="service_start")
    service_end.show_analysis(prefix_filename="service_end")
    queue.show_analysis(prefix_filename="queue")
    system_time.show_analysis(prefix_filename="system_time")
    employee_idle.show_analysis(prefix_filename="employee_idle")
    clients_served.show_analysis(prefix_filename="clients_served")
    
    pos = 1
    for employee_service in employee_services:
        employee_service.show_analysis(prefix_filename=f"employee_service{pos}")
        pos += 1
    
if __name__ == "__main__":
    main()