import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ventas.csv', parse_dates=["fecha"])

#print(df.dtypes)

# Ventas por mes

df['mes'] = df['fecha'].dt.to_period('M')

ventas_por_mes = df.groupby('mes').apply(lambda d: (d['cantidad'] * d['precio']).sum())

ventas_por_mes = ventas_por_mes.sort_index()

print("Ventas por mes: ")
print(ventas_por_mes)


# Mas vendidos en cantidad total y mayor ingreso
df['ingreso'] = df['cantidad'] * df['precio']
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum', 
    'ingreso': 'sum'})

mas_vendido= ventas_prod['cantidad'].idxmax()
mayor_ingreso= ventas_prod['ingreso'].idxmax()

print(f"Productos mas vendidos en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'cantidad']})")
print(f"Productos con mayor ingreso: {mayor_ingreso} (total {ventas_prod.loc[mayor_ingreso, 'ingreso']})")

#graficar ventas x mes

plt.figure(figsize=(6, 4))
ventas_por_mes.plot(kind='bar')
plt.xlabel("Ventas por Mes")
plt.ylabel("Mes")
plt.ylabel("Ventas ($)")

plt.tight_layout()
plt.savefig('ventas_por_mes.png')
plt.show()

#graficar top 5 productos por ingresos

top5= ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(6, 4))
plt.bar(top5.index, top5['ingreso'])
plt.title("Top 5 productos por ingresos")
plt.ylabel("Ingresos ($)")
plt.xlabel("Producto")
plt.tight_layout()
plt.savefig('top5_productos.png')
plt.show()
