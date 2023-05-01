import requests


headers = {'Authorization': 'Token beddec6af186cf36cc1e9fb6b5137b9ca140410a'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}6/',headers=headers)

#testando o codgio HTTP
assert resultado.status_code == 204


#testando se o tamanho do conteudo e retorno e 0
assert len(resultado.text) == 0