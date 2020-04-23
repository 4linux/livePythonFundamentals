
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

#1: Conseguir fazer o python se comunicar o website da ALESP
url = "https://www.al.sp.gov.br/propositura/?id=1000252923&tipo=1&ano=2018"

with uReq(url) as pagina:
	conteudo = pagina.read()

#2: Extrair as informações em formato html e manipular as informações coletadas

pagina_estruturada = soup(conteudo, "html.parser")

#4: Filtrar os dados de interesse

div_alvo = pagina_estruturada.findAll("div", {"class": "ativo", "id":"referencias"})

tabela = div_alvo[0].table.tbody.find_all('td') 

#5: Armazenar os dados em dicionário

pl = {}

pl["num_legistativo"] = tabela[3].text.strip()
pl["ementa"] = tabela[5].text.strip()
pl["data_publicacao"] = tabela[7].text.strip()
pl["regime"] = tabela[9].text.strip()
pl["autores"] = tabela[11].text.strip()
pl["apoiadores"] = tabela[13].text.strip()
pl["indexadores"] = tabela[15].text.strip()
pl["etapa_atual"] = tabela[17].text.strip()


