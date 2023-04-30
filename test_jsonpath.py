import requests
import jsonpath

headers = {'Authorization': 'Token beddec6af186cf36cc1e9fb6b5137b9ca140410a'}
cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)

avaliacoes = jsonpath.jsonpath(cursos.json(), 'results[*].avaliacoes')
print(avaliacoes)
