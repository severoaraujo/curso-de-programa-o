salario=float(input("Digite o salário: R$"))
ir=round(float(salario*11/100),2)
print(f"IR (11%): R$", round(float(ir),2))
inss=round(float(salario*8/100),2)
print(f"((INSS (8%): R$", round(float(inss),2))
sindicato=round((float(salario*5/100)),2)
print(f"Sindicato (5%): R$", round(float(sindicato),2))
salario_liquido=round(float(salario-ir-inss-sindicato),2)
print(f"Salário Liquido: R$", round(float(salario_liquido),2))