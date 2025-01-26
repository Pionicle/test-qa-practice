# **Тестирование сайта [qa-practice.com](https://www.qa-practice.com/)**

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-1.49-darkgreen.svg)
![Allure](https://img.shields.io/badge/Allure-2.13-yellow.svg)
![Pytest](https://img.shields.io/badge/Pytest-8.3.4-red.svg)

Проект предназначен для автоматизированного тестирования сайта [qa-practice.com](https://www.qa-practice.com) с использованием **Playwright**, **Pytest** и **Allure**.

**Цель** тестирование UI компонентов:

- Inputs
- Buttons
- Checkbox
- Select
- New tab
- Text area
- Alerts
- Drag and Drop
- Iframes
- Pop-up

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
pytest -v -s
allure generate results --clean -o allure-report
allure open allure-report
```

---

## **Запуск через Docker**

---

## **Структура проекта**

```
test-qa-practice/
│── components/            # Компоненты приложения
│
│── pages/                 # Страницы приложения
│
│── tests/                 # Основная папка с тестами
│   ├── tests_components/   # Тесты компонентов
│   ├── test_page/         # Тесты страниц
│
│── conftest.py            # Фикстуры для pytest
│── requirements.txt       # Зависимости проекта
│── README.md              # Документация проекта
│── .gitignore             # Игнорируемые файлы для Git
│── pytest.ini             # Конфигурация для pytest

```

---
