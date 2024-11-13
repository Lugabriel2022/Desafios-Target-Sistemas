SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total = SP + RJ + MG + ES + Outros

per_sp = (SP / total) * 100
per_rj = (RJ / total) * 100
per_mg = (MG / total) * 100
per_es = (ES / total) * 100
per_out = (Outros / total) * 100

print(f'O faturalmento total foi de R${total:.2f}')
print(f'O percentual de Sp foi {per_sp:.2f}%')
print(f'O percentual do Rj foi {per_rj:.2f}%')
print(f'O percentual de Mg foi {per_mg:.2f}%')
print(f'O percentual do Es foi {per_es:.2f}%')
print(f'O percentual dos Outros foi {per_out:.2f}%')
