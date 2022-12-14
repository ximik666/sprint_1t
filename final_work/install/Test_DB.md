### Cравнение производительности запросов в Mysql и Clickhouse

Попробуем сравнить стандартые запросы выборки в Mysql и Clickhouse. Запросы для обоих СУБД будут идентичны.

1. ```select count(*) from XXXX.mdl_logstore_standard_log;```

|Запрос/Время выполнения запроса | Mysql | Clickhouse|
|-------------------------|-------|-----------|
|```select count(*) from XXXX.mdl_logstore_standard_log;```                         | 1 min 53.74 sec      | 0.139 sec|
|```select ip,count(*) cc from XXXX.mdl_logstore_standard_log group by ip order by cc desc limit 50;```||2.854 sec|
|```select distinct userid from XXXX.mdl_logstore_standard_log where courseid = 21143 and eventname like '%attempt_start%';```||3.975 sec|     