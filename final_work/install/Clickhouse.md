### Установка и настройка Clickhouse
Для установки и настройки используем [инструкцию](https://clickhouse.com/docs/en/install/) от "оффициального производителя".

```
sudo apt-get install -y apt-transport-https ca-certificates dirmngr
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 8919F6BD2B48D754

echo "deb https://packages.clickhouse.com/deb stable main" | sudo tee \
    /etc/apt/sources.list.d/clickhouse.list
sudo apt-get update

sudo apt-get install -y clickhouse-server clickhouse-client

sudo service clickhouse-server start
clickhouse-client # or "clickhouse-client --password" if you've set up a password.
```
Не забываем установить пароль на подключение.
![](../img/2022-12-14_08-59-32.png)