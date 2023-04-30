import  requests

headers =  {'Authorization' :'Token beddec6af186cf36cc1e9fb6b5137b9ca140410a'}
cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/',headers= headers)

print(cursos.status_code)
print(cursos.json())