# Кейс 4 — Пример (простая версия)

## Что есть
- `sql/schema_mssql.sql` — скрипт БД (Customers, Products, Orders).
- `delphi_isapi/` — исходники ISAPI-проекта (Delphi WebBroker).

## Как использовать
1. Развернуть MS SQL Server, выполнить `sql/schema_mssql.sql`.
2. В Delphi открыть проект `ProjectISAPI.dpr`, поправить строку подключения (пока заглушка).
3. Собрать DLL и настроить IIS для ISAPI.
4. Проверить в браузере: `/` и `/orders`.
