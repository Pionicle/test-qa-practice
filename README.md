# **Тестирование сайта effective-mobile.ru**

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-1.49-darkgreen.svg)
![Allure](https://img.shields.io/badge/Allure-2.13-yellow.svg)
![Pytest](https://img.shields.io/badge/Pytest-8.3.4-red.svg)

Проект предназначен для автоматизированного тестирования сайта [effective-mobile.ru](https://effective-mobile.ru) с использованием **Playwright**, **Pytest** и **Allure**.  
**Цель** - тестирование, проверяющие переход по всем блокам по клику (О нас, Контакты и пр.)

---

## Содержание

- [Требования](#требования)
- [Установка](#установка)
- [Локальный запуск](#локальный-запуск)
- [Запуск через Docker](#запуск-через-docker)
- [Структура проекта](#структура-проекта)

---

## Требования

- Python 3.12
- Java
- Allure

---

## Установка

1. Клонируйте репозиторий:

```sh
git clone https://github.com/Pionicle/test-qa-practice.git
cd test-qa-practice
```

2. Установите зависимости:

```sh
pip install -r requirements
```

3. Установите браузеры для **Playwright**:

```sh
playwright install --with-deps
```

4. Установите [**Allure**](https://allurereport.org/docs/install/):

- Windows

```sh
scoop install allure
```

- macOS

```sh
brew install allure
```

- Linux

```sh
brew install allure
```

---

## Локальный запуск

1. Убедитесь, что все зависимости установлены.
2. Запустите тесты:

```sh
pytest -v -s --alluredir=results
allure generate results --clean -o allure-report
allure open allure-report
```

---

## **Запуск через Docker**

1. Соберите Docker-образ (2,61 Гб):

```sh
docker build -t test-qa-practice .
```

2. Запустите контейнер и дождитесь окончания тестов (~1 мин.):

```sh
docker run -d -p {свободный_порт}:5952 test-qa-practice
```

3. Передите по ссылке http://localhost:{свободный_порт}
4. Пример `docker run -d -p 5952:5952 test-qa-practice` - http://localhost:5952

---

## **Структура проекта**

```
test-qa-practice/
│── tests/
│   ├── test_home_page.py   # Тесты главной страницы
│
│── pages/
│   ├── home_page.py       # Главная страница
│
│── conftest.py            # Фикстуры pytest
│── requirements.txt       # Зависимости
│── Dockerfile             # Описание проекта для сборки Docker-образа
│── README.md
│── .dockerignore
│── .gitignore
```

---
