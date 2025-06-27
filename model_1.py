import requests
from bs4 import BeautifulSoup

#url = "https://www.mercadolivre.com.br/notebook-samsung-galaxy-book4-intel-u300-120-ghz-ate-44ghz-8-mb-l3-cache-windows-11-home-8gb-256gb-ssd-uhd-graphics-156-full-hd-led-155kg/p/MLB40347107#polycard_client=search-nordic&searchVariation=MLB40347107&wid=MLB5194930972&position=23&search_layout=grid&type=product&tracking_id=c041abe7-578e-4b0f-80bd-84902e4f3965&sid=search"
url = "<url-site>"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos os preços na página
prices = soup.find_all('span', class_='andes-money-amount__fraction')

# Exibir todos os preços encontrados para entender a estrutura
print("Preços encontrados:")
for i, price in enumerate(prices):
    print(f"{i + 1}: R${price.text}")

# Tentar pegar o segundo preço (geralmente o promocional)
if len(prices) >= 2:
    print(f"\n✅ Preço promocional: R${prices[1].text}")
elif prices:
    print(f"\n⚠️ Só um preço encontrado: R${prices[0].text}")
else:
    print("❌ Nenhum preço encontrado.")
