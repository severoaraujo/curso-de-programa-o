populacao_a = 80000  # População do país A
taxa_crescimento_a = 0.03  # Taxa de crescimento anual do país A (3%)

populacao_b = 200000  # População do país B
taxa_crescimento_b = 0.015  # Taxa de crescimento anual do país B (1.5%)

anos = 0  # Contador de anos

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_crescimento_a
    populacao_b += populacao_b * taxa_crescimento_b
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.")
