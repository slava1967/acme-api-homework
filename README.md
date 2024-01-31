## запуск приложения

```
./venv/bin/flask --app ./acme/server.py run
```


## cURL тестирование

### добавление новой заметки
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-01|title|text"
```

### получение всего списка заметок
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### обновление текста заметки по идентификатору / ID == 1 /  новый текст == "new text"
```
curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "2024-01-01|title|new text"
```

### удаление заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-01|title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|2024-01-01|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2024-01-01|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-01|title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|title|new text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-01|title|looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: text lenght > MAX: 200

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-01|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 20

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/calendar/
-- пусто --
```
