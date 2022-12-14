### Установка и настройка модуля Mysql_to_Clickhouse для репликации логов с основной БД Mysql
Изначально Clickhouse не поддерживал автоматическую репликацию с СУБД Mysql, пришлось использовать стороннюю [библиотеку](https://pypi.org/project/clickhouse-mysql/) на Python.
Установили согласно [инструкции](https://github.com/Altinity/clickhouse-mysql-data-reader/blob/master/docs/manual.md).

1. Делаем дамп столбцов необходимой таблицы

![](../img/2022-12-14_09-09-24.png)

2. Восстанавливаем дамп в базу Clickhouse

![](../img/2022-12-14_09-11-01.png)

3. Запускаем и долго ждем первую синхронизацию

![](../img/2022-12-14_09-12-17.png)