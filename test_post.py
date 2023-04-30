import requests


headers = {'Authorization': 'Token beddec6af186cf36cc1e9fb6b5137b9ca140410a'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


novo_curso ={
    "titulo": "AWS na pratica",
    "url": "https://www.udemy.com/course/aws-na-pratica/"
           }
# Verifica se o curso já existe antes de criar um novo
resultado = requests.get(url=f'{url_base_cursos}?search={novo_curso["titulo"]}', headers=headers)
if resultado.status_code == 200 and resultado.json()['count'] > 0:
    print("Curso já existe")
else:
    resultado = requests.post(url=url_base_cursos,headers=headers,data=novo_curso)
    # testando o codigo de status HTTP 201
    assert resultado.status_code == 201
    # testando se o titulo do curso retornado e o mesmo do informado
    assert resultado.json()['titulo'] == novo_curso['titulo']
    print("Novo curso criado com sucesso")