import requests


headers = {'Authorization': 'Token beddec6af186cf36cc1e9fb6b5137b9ca140410a'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes= 'http://127.0.0.1:8000/api/v2/cursos/'


resultado = requests.get(url=url_base_cursos,headers=headers)

print(resultado.json())
# #testando o endpoint esta correto
#
# assert  resultado.status_code == 200
# #testando a quantidade de registros
assert  resultado.json()['count'] == 6
#
# #testando se o titulo do primeiro curso esta correto

assert resultado.json()['results'][0] ['titulo'] == 'Python API'