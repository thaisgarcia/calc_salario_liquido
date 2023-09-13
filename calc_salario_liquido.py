salario_hora = float(input("Informe quanto você ganha por hora: "))
horas_trab = int(input("Informe o número de horas trabalhadas no mês: "))

salario_bruto = float(salario_hora * horas_trab)
ir=(salario_bruto*0.11)
inss=(salario_bruto*0.08)
sindicato=(salario_bruto*0.05)

print(f"""
    + Salário Bruto : R$ {salario_bruto:.2f}
    - Imposto de Renda (11%) : R$ {ir:.2f}
    - INSS (8%) : R$ {inss:.2f}
    - Sindicato (5%) : R$ {sindicato:.2f}
    = SALÁRIO LÍQUIDO : R$ {salario_bruto - ir - inss - sindicato:.2f}
""")
