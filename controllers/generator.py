class Pseudorandom:
   # Gerador de números pseudoaleatórios utilizando o método no intervalo [0,1].
    
    def __init__(self, amount, seed):
        self.seed = seed
        self.a = 48271
        self.c = 0
        self.m = 2**31 - 1
        self.generated_numbers = self.generate(amount)
        
    def generate(self, amount):
        amount += 2
        x_n = self.seed
        generated_numbers = []
        
        i = 0  # Inicializa o contador
        while i < amount:
            x_n = (self.a * x_n + self.c) % self.m
            result = x_n / self.m
            
            # Condição para verificar se o 'result' é diferente de 0
            if result > 0:
                if i >= 2: # Aplica a lógica de ignorar os dois primeiros números gerados
                    generated_numbers.append(result)
                i += 1 # i só incrementa se result for diferente de 0
            
            # Se result for igual a 0, o loop continua e 'i' não é incrementado, 
            # forçando o recálculo com o mesmo 'i' e o novo 'x_n'.
            
        return generated_numbers