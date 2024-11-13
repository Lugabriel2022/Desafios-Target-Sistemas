dias = list(range(1 , 31))
ganhos = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722,
          0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667,
          18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

soma = sum(ganhos)
quant = len(ganhos)
media = soma / quant
maior = max(ganhos)
menor = min(ganhos)

dias_acima_da_media = [dia for dia, ganho in zip(dias,ganhos) if ganho > media]

num_dias_ac_media = len(dias_acima_da_media)

print(f'O maior faturamento foi de R${maior}')
print(f'O menor faturamento foi de R${menor}')
print(f'E {num_dias_ac_media} dias tiveram um faturamento acima da média')