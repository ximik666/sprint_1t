### Cравнение производительности запросов в Mysql и Clickhouse

Попробуем сравнить стандартые запросы выборки в Mysql и Clickhouse. Запросы для обоих СУБД будут идентичны.

1. ```select count(*) from XXXX.mdl_logstore_standard_log;```

|Время выполнения запроса | Mysql | Clickhouse|
|                         | 1 min 53.74 sec      | 0.139c     