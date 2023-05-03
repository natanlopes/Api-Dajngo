import requests



class TestCursos:
    headers = {'Authorization': 'Token beddec6af186cf36cc1e9fb6b5137b9ca140410a'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta =  requests.get(url=self.url_base_cursos,headers=self.headers)
        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta =  requests.get(url= f'{self.url_base_cursos}2/',headers=self.headers)

    def test_post_curso(self):
        novo={
            "titulo":"Curso de Ruby",
            "url":"https://infinityschool.eadplataforma.com/test/start/200/1325/4590/1970/"

        }
        resposta = requests.post(url=self.url_base_cursos,headers=self.headers,data=novo)
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "novo curso de ruby",
            "url":"https://www.infinityschool.app/boletim"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}2/',headers=self.headers,data=atualizado)
        assert resposta.status_code== 200
    def test_put_titulo_curso(self):
        atualizado ={
            "titulo": "novo curso de ruby 2",
            "url": "https://www.infinityschool.app/boletim2"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}2/',headers=self.headers,data=atualizado)
        assert resposta.json()["titulo"] == atualizado["titulo"]

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}2/',headers=self.headers)
        assert resposta.status_code== 204 and len(resposta.text)==0