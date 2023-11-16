import tkinter as tk
from tkinter import ttk
import locale

# Configurar a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatar_moeda(valor):
    return locale.currency(valor, grouping=True)

def mostrar_mensagem_destacada(meta, economia_mensal, meses_inteiros, dias_adicionais):
    popup = tk.Toplevel(root)
    popup.title("Mensagem Destacada")

    # Criar rótulos para cada parte da mensagem
    label_part1 = ttk.Label(popup, text=f"Para atingir a meta de {formatar_moeda(meta)}", font=("Arial", 12), background="yellow")
    label_part2 = ttk.Label(popup, text=f"economizando {formatar_moeda(economia_mensal)} por mês,", font=("Arial", 12), background="yellow")
    label_part3 = ttk.Label(popup, text=f"levará aproximadamente {meses_inteiros} meses e {dias_adicionais} dias.", font=("Arial", 12), background="yellow")

    # Destacar o resultado das variáveis
    label_part1.config(font=("Arial", 12, "bold"))
    label_part2.config(font=("Arial", 12, "bold"))
    label_part3.config(font=("Arial", 12, "bold"))

    # Posicionar rótulos na janela
    label_part1.pack(padx=10, pady=5)
    label_part2.pack(padx=10, pady=5)
    label_part3.pack(padx=10, pady=5)

def calcular_tempo_necessario():
    try:
        # Obter valores da entrada e converter para float
        meta_str = entry_meta.get().replace('R$', '').replace('.', '').strip()
        meta = float(meta_str.replace(',', '.'))

        economia_mensal_str = entry_economia.get().replace('R$', '').replace('.', '').strip()
        economia_mensal = float(economia_mensal_str.replace(',', '.'))

        # Verificar se os valores são positivos
        if meta <= 0 or economia_mensal <= 0:
            resultado_var.set("Valores devem ser positivos.")
        elif meta < economia_mensal:
            resultado_var.set("O valor da meta é menor que a economia mensal.")
        else:
            # Calcular tempo necessário
            tempo_necessario_meses = meta / economia_mensal
            meses_inteiros = int(tempo_necessario_meses)
            dias_adicionais = int((tempo_necessario_meses - meses_inteiros) * 30)  # Assumindo 30 dias por mês

            # Chamar a função para mostrar a mensagem destacada em uma nova janela
            mostrar_mensagem_destacada(meta, economia_mensal, meses_inteiros, dias_adicionais)
    except ValueError as e:
        # Tratar erros de conversão para float
        resultado_var.set(f"Erro: {str(e)}")

# janela principal
root = tk.Tk()
root.title("Calculadora de Meta Financeira")

# widgets
label_meta = ttk.Label(root, text="Digite o valor da sua meta financeira: R$")
entry_meta = ttk.Entry(root)
label_economia = ttk.Label(root, text="Digite o valor que você pode economizar mensalmente: R$")
entry_economia = ttk.Entry(root)
button_calcular = ttk.Button(root, text="Calcular", command=calcular_tempo_necessario)
resultado_var = tk.StringVar()
label_resultado = ttk.Label(root, textvariable=resultado_var)

label_meta.grid(row=0, column=0, sticky=tk.W)
entry_meta.grid(row=0, column=1)
label_economia.grid(row=1, column=0, sticky=tk.W)
entry_economia.grid(row=1, column=1)
button_calcular.grid(row=2, column=0, columnspan=2)
label_resultado.grid(row=3, column=0, columnspan=2)

root.mainloop()
