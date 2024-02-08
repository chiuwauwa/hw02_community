# yatube_project
### Описание
Делаем свою твитату
### Технологии
Python 3.9
Django 2.2.19

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone git@github.com:chiuwauwa/hw02_community.git
```
Переходим в папку с проектом:

```bash
cd hw02_community
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/bin/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
```
```bash
python yatube/manage.py migrate
```

Создаем супер пользователя:

```bash
python yatube/manage.py createsuperuser
```

Не забываем добавить в .gitingore файлы:

```bash
.env
.venv
```

Запускаем проект:

```bash
python yatube/manage.py runserver
```

После чего проект будет доступен по адресу в терминале

Заходим в http://что-то/admin и создаем группы и записи.
После чего записи и группы появятся на главной странице.

Запускаем тестов:

```bash
pytest
```

### Авторы
Никитка и Колюшка