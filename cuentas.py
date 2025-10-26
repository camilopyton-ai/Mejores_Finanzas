# ============================================================
# Simulación financiera con Monte Carlo
# Autor: [Tu nombre]
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# PARTE 1: PARÁMETROS BASE
# ------------------------------

np.random.seed(123)  # Para reproducibilidad

# Supuestos
meses = 12                   # horizonte en meses
simulaciones = 1000          # número de escenarios

media_ingresos = 3000000     # ingreso mensual promedio
sd_ingresos = 200000         # desviación estándar ingresos

media_gastos = 2000000       # gasto mensual promedio
sd_gastos = 300000           # desviación estándar gastos

# ------------------------------
# PARTE 2: SIMULACIÓN
# ------------------------------

# Creamos matrices aleatorias
ingresos = np.random.normal(media_ingresos, sd_ingresos, (simulaciones, meses))
gastos = np.random.normal(media_gastos, sd_gastos, (simulaciones, meses))

# Ahorro mensual y acumulado
ahorro_mensual = ingresos - gastos
ahorro_acumulado = np.cumsum(ahorro_mensual, axis=1)

# ------------------------------
# PARTE 3: ESTADÍSTICAS CLAVE
# ------------------------------

saldo_final = ahorro_acumulado[:, -1]  # saldo al final del año

media_saldo = np.mean(saldo_final)
p10 = np.percentile(saldo_final, 10)
p90 = np.percentile(saldo_final, 90)
prob_saldo_positivo = np.mean(saldo_final > 0)

print("Resultados de la simulación Monte Carlo:\n")
print(f"Saldo final promedio: ${media_saldo:,.0f}")
print(f"Percentil 10% (escenario pesimista): ${p10:,.0f}")
print(f"Percentil 90% (escenario optimista): ${p90:,.0f}")
print(f"Probabilidad de terminar con saldo positivo: {prob_saldo_positivo*100:.1f}%")

# ------------------------------
# PARTE 4: VISUALIZACIÓN
# ------------------------------

plt.figure(figsize=(8,5))
plt.hist(saldo_final, bins=30, edgecolor='black', alpha=0.7)
plt.axvline(media_saldo, color='red', linestyle='--', label=f'Media = ${media_saldo:,.0f}')
plt.axvline(p10, color='orange', linestyle='--', label=f'P10 = ${p10:,.0f}')
plt.axvline(p90, color='green', linestyle='--', label=f'P90 = ${p90:,.0f}')
plt.title('Distribución del saldo final (12 meses)')
plt.xlabel('Saldo final ($)')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# ------------------------------
# PARTE 5: EXPORTAR RESULTADOS
# ------------------------------

# Guardar simulaciones en un DataFrame
df_sim = pd.DataFrame(ahorro_acumulado,
                      columns=[f"Mes_{i+1}" for i in range(meses)])
df_sim["Saldo_final"] = saldo_final

# Exportar a Excel si lo deseas
df_sim.to_excel("Simulacion_MonteCarlo_Finanzas.xlsx", index=False)
print("\nArchivo 'Simulacion_MonteCarlo_Finanzas.xlsx' generado correctamente.")
