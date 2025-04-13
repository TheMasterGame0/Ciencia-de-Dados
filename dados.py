import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Lê o arquivo CSV
df = pd.read_csv('dados_consulta.csv')

# Primeira tabela
# Relação entre Consumo Mensal ao longo do tempo no Nordeste

df_filtrado = df[df["Subsistema"] == "Nordeste"][["Ano", "Mes", "Consumo_Mensal"]]
df_filtrado["Data"] = df_filtrado["Ano"].astype(str) + " - " + df_filtrado["Mes"].astype(str)

df_filtrado = df_filtrado.drop(["Ano", "Mes"], axis=1)

plt.plot(df_filtrado["Data"], df_filtrado["Consumo_Mensal"], marker='o')
plt.title("Consumo Mensal ao longo do tempo no Nordeste")
plt.xlabel("Tempo")
# Mostra cada 24th label
plt.xticks(ticks=range(0, len(df_filtrado["Data"]), 24), labels=df_filtrado["Data"][::24])
plt.ylabel("Consumo Mensal")
plt.show()

# Segunda tabela
# Consumo total de cada região
Consumo_Nordeste = df[df["Subsistema"] == "Nordeste"]["Consumo_Mensal"].sum()
Consumo_Sul = df[df["Subsistema"] == "Sul"]["Consumo_Mensal"].sum()
Consumo_Norte = df[df["Subsistema"] == "Norte"]["Consumo_Mensal"].sum()
Consumo_Sudeste = df[df["Subsistema"] == "Sudeste / Centro-Oeste"]["Consumo_Mensal"].sum()

plt.bar(["Nordeste", "Sul", "Norte", "Sudeste / Centro-Oeste"], [Consumo_Nordeste, Consumo_Sul, Consumo_Norte, Consumo_Sudeste], color='skyblue')
plt.title("Consumo Total por região")
plt.xlabel("Região")
plt.ylabel("Consumo Total")
plt.show()

# Terceira tabela
# Consumo de cada região
sns.boxplot(x='Subsistema', y='Consumo_Mensal', data=df)

plt.title("Consumo Mensal por região")
plt.xlabel("Região")
plt.ylabel("Consumo Mensal")
plt.show()