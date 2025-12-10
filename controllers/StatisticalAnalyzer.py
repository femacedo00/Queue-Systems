import math
import matplotlib.pyplot as plt
from typing import Optional

# Classe para cálculo de métricas
class StatisticalAnalyzer:
    def __init__(self, name):
        self.name = name # Nome da métrica que iremos calcular
        self.count = 0 # Soma do tempo de uma seed
        self.avaranges = [] # Array com as médias de tempo de todas as seeds
        self.result = {} # Resultado dos cálculos
    
    # Média das médias
    @staticmethod
    def calculate_avarange_avaranges(avaranges, n):
        sum_result = sum(avaranges)
        if not sum_result: return 0
        return sum_result / n

    # Desvio padrão
    @staticmethod
    def calculate_standard_deviation(avaranges, avarange, n):
        if n <= 1:
            return 0.0
        s = 0.0
        for num in avaranges:
            s += (num - avarange) ** 2
        return (s / (n - 1)) ** 0.5

    # Realiza o cálculo do intervalo de confiança
    @staticmethod
    def calculate_confidence_interval(avaranges):
        n = len(avaranges) # Quantidade de posições da array
        n = len(avaranges) # Quantidade de posições da array
        if n == 0:
            return {
                "avarange": 0.0,
                "standard_deviation": 0.0,
                "margin_error": 0.0,
                "lower_bound": 0.0,
                "upper_bound": 0.0
            }
        avarange = StatisticalAnalyzer.calculate_avarange_avaranges(avaranges, n) # Calculando a média das médias
        standard_deviation = StatisticalAnalyzer.calculate_standard_deviation(avaranges, avarange, n) # Calculando o desvio padrão
        z = 1.96
        
        margin_error = z * (standard_deviation / (n ** (1/2)))
        
        # Retornando o limite inferior e superior
        return {
            "avarange": avarange,
            "standard_deviation": standard_deviation,
            "margin_error": margin_error,
            "lower_bound": avarange - margin_error,
            "upper_bound": avarange + margin_error
        }
        
    # Métodos de plotagem de gráfico
    def plot_confidence_interval(self, show: bool = True, savepath: Optional[str] = None, figsize=(18, 5)):
        # Plota a média das médias com intervalo de confiança (média ± margem de erro).
        if not self.avaranges:
            print(f"[plot_confidence_interval] Nenhum dado em avaranges para '{self.name}'.")
            return

        # (re)calcula resultado se necessário
        self.result = StatisticalAnalyzer.calculate_confidence_interval(self.avaranges)
        mean = self.result['avarange']
        me = self.result['margin_error']
        lower = self.result['lower_bound']
        upper = self.result['upper_bound']

        plt.figure(figsize=figsize)
        # Plota as avaranges individuais como pontos
        plt.scatter(range(1, len(self.avaranges) + 1), self.avaranges, label='Médias por semente')
        # Linha da média
        plt.hlines(mean, xmin=1, xmax=max(1, len(self.avaranges)), linestyles='--', label=f'Média = {mean:.4f}')
        # Banda do intervalo de confiança
        plt.fill_between([1, max(1, len(self.avaranges))], [lower, lower], [upper, upper], alpha=0.2,
                         label=f'IC 95%: [{lower:.4f}, {upper:.4f}]')
        plt.title(f"{self.name} — Média e Intervalo de Confiança (95%)")
        plt.xlabel("Semente (índice)")
        plt.ylabel("Valor")
        plt.legend()
        plt.grid(True)

        if savepath:
            plt.savefig(savepath, bbox_inches='tight')
            print(f"[plot_confidence_interval] Salvo: {savepath}")
        if show:
            plt.show()
        else:
            plt.close()
        
    # Inicia o cálculo para encontrar o intervalo de confiança e imprime o resultado em seguida
    def show_analysis(self, prefix_filename: Optional[str] = None, show: bool = True):
        self.result = StatisticalAnalyzer.calculate_confidence_interval(self.avaranges)
        
        print(f"\n{self.name}:")
        print(f"  Média das Médias (Average): {self.result['avarange']:.4f}")
        print(f"  Intervalo de confiança:       {self.result['standard_deviation']:.4f}")
        print(f"  Margem de Erro:       {self.result['margin_error']:.4f}")
        print(f"  Intervalo de confiança: [{self.result['lower_bound']:.4f}, {self.result['upper_bound']:.4f}]\n")
        
        # Plota e salva (opcional) os dois gráficos: série e média+IC.
        # prefix_filename: se informado salva em '{prefix_filename}_series.png' e '{prefix_filename}_ci.png'
        if prefix_filename:
            self.plot_confidence_interval(show=show, savepath=f"results/{prefix_filename}_ci.png")
        else:
            self.plot_confidence_interval(show=show)
    