import speedtest

test = speedtest.Speedtest()

# Faz o teste de Download e converte em mb/s
down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

# Faz o teste de Upload e converte em mb/s
upload = test.upload()
rsUpload = round(upload)
fUpload = int(rsUpload / 1e+6)

# Mostra resultados
print(f"Sua velocidade de Download é de: {fDown} mb/s")
print(f"Sua velocidade de Upload é de: {fUpload} mb/s")