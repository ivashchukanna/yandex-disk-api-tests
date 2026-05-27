import requests

# Инструкция по запуску:
# 1. Библиотеки: pip install pytest requests
# 2. Получить токен на https://yandex.ru/dev/disk/poligon/
# 3. Вставить токен в переменную TOKEN вместо "токен_с_полигона"
# 4. Запустить тест

TOKEN = "токен_с_полигона"
url = "https://cloud-api.yandex.net/v1/disk/resources"
headers = {"Authorization":f"OAuth {TOKEN}"}
path_name = "My_new_path"

def test_1_create_path():
    params = {"path":path_name}
    response = requests.put(url, params = params, headers = headers)
    assert response.status_code == 201

def test_2_get_path_information():
    params = {"path":path_name}
    response = requests.get(url, params = params, headers = headers)
    assert response.status_code == 200
    val = response.json()
    assert val["name"] == path_name
    assert val["type"] == "dir"

copy_url = "https://cloud-api.yandex.net/v1/disk/resources/copy"
new_path_name = "My_new_path_copy"

def test_3_copy_path():
    params = {"from":path_name, "path":new_path_name}
    response = requests.post(copy_url, headers=headers, params = params)
    assert response.status_code == 201

def test_4_delete_copy():
    params = {"path":new_path_name}
    response = requests.delete(url, headers = headers, params = params)
    assert response.status_code == 204

upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
file_name = "file"

def test_5_upload_file():
    params = {"path":f"{path_name}/{file_name}.txt"}
    response = requests.get(upload_url, headers = headers, params = params)
    assert response.status_code == 200
    href = response.json()["href"]

    upload_response = requests.put(href, data = "Hello, world!!!")
    assert upload_response.status_code == 201

list_url = "https://cloud-api.yandex.net/v1/disk/resources/files"

def test_6_get_files_list():
    response = requests.get(list_url, headers = headers)
    assert response.status_code == 200


