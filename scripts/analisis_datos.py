import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos/dataset.csv')
df['fecha'] = pd.to_datetime(df['fecha'])
df['total_linea'] = df['cantidad'] * df['precio']

ventas_totales = df['total_linea'].sum()
producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()

df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['total_linea'].sum()

print("--- INDICADORES PROCESADOS ---")
print(f"Ventas Totales: ${ventas_totales:,.2f}")
print(f"Producto más vendido: {producto_mas_vendido}")
print("\nVentas por mes:\n", ventas_por_mes.to_string())

plt.figure(figsize=(8, 4))
ventas_por_mes.plot(kind='line', marker='o', color='green', linewidth=2)
plt.title('Evolución de Ventas por Mes')
plt.xlabel('Período Mensual')
plt.ylabel('Ventas ($)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('resultados/grafico_resultados.png', dpi=300)
