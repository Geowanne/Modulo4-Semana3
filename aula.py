from requests_html import HTMLSession

sessao = HTMLSession()
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

resposta = sessao.get(url)

anuncios = []

links = resposta.html.find  ("a[data-ds-component='DS-NewAdCard-Link']")
print('links:', links)

for link in links:

  # Extrai o URL de cada anúncio do atributo 'href' do elemento
  url_iphone = link.attrs['href']

  # Faz uma requisição GET ao URL de cada anúncio usando a sessão criada
  resposta_iphone = sessao.get(url_iphone)

  # Extrai o título e o preço de cada anúncio
  titulo = resposta_iphone.html.find('h1', first = True).text
  preco = resposta_iphone.html.find('span[class="ad__sc-1wimjbb-1 hoHpcC sc-bZQynM hYqmow"]', first=True).text

  # Adiciona as informações do anúncio na lista de anúncios
  anuncios.append({
      'url': url_iphone,
      'titulo': titulo,
      'preco': preco
  })