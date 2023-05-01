import requests


headers = {'Authorization': 'Token beddec6af186cf36cc1e9fb6b5137b9ca140410a'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


curso_atualizado ={
    "titulo": "Novo Curso de Scrum 3",
    "url":"http://www.geekuniversity.com.br/ncc3"
}
# #buscando se o curso com ID 6
# curso = requests.get(url=f'{url_base_cursos}6/',headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)
print(resultado.status_code)


# resultado = requests.put(url=f'{url_base_cursos}6/',headers=headers,data=curso_atualizado)
#
#
# #testando o codigo de status HTTP
#
# assert  resultado.status_code == 200
#
# #testando o titulo
# assert resultado.json()['titulo']== curso_atualizado['titulo']