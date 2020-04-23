from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# Mapear os links (urls) das PLs
## URL que contém os links das PLs de 2018
url = "https://www.al.sp.gov.br/alesp/projetos/?tipo=1&ano=2018"

# requisicao da página
with uReq(url) as pagina:
	conteudo = pagina.read()

# transformando a página em objetos manipuláveis
pagina_html = soup(conteudo, "html.parser") 	

#filtrando os links	
lista_links = pagina_html.findAll("ul" , {"class":"listaNP_itens"})

#para cada item da lista, armazenar os links em uma lista
lista_urls = []

for item in lista_links[0].find_all('a'):
	lista_urls.append("https://www.al.sp.gov.br{}".format(item['href']))
	
# escalar a coleta: coletar os 100 primeiros projetos de lei
lista_dic = []
 
for item in range(100):
	with uReq(lista_urls[item]) as pagina:
		conteudo = pagina.read()

	html = soup(conteudo, "html.parser") 

	div = html.findAll("div", {"class": "ativo", "id":"referencias"}) 
	
	tabela = div[0].table.tbody.find_all('td')
	
	pl = {}
	pl['num_legislativo'] = tabela[3].text.strip() 
	pl['ementa'] = tabela[5].text.strip()
	pl['data']= tabela[7].text.strip()
	pl['regime']= tabela[9].text.strip()
	pl['autores'] = tabela[11].text.strip()
	pl['apoiadores']= tabela[13].text.strip()
	pl['indexadores']= tabela[15].text.strip().split(',') 
	pl['estapa_atual'] = tabela[17].text.strip()
	
	lista_dic.append(pl)



