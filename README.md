# MoexClickHouse

Проект для загрузки тестовых данных в ClickHouse с Московской биржи.

### Установка зависимостей

```shell
cd MoexClickHouse
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Установка ClickHouse

#### Docker

```shell

docker volume create volume-clickhouse
docker run -d --name some-clickhouse-server -v volume-clickhouse:/etc/clickhouse-server -p 8123:8123 -p 9000:9000 -p 9009:9009 --ulimit nofile=262144:262144 clickhouse/clickhouse-server
```

#### Ubuntu

```shell
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
curl -fsSL 'https://packages.clickhouse.com/rpm/lts/repodata/repomd.xml.key' | sudo gpg --dearmor -o /usr/share/keyrings/clickhouse-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg] https://packages.clickhouse.com/deb stable main" | sudo tee \
    /etc/apt/sources.list.d/clickhouse.list
sudo apt-get update

sudo apt-get install -y clickhouse-server clickhouse-client
sudo service clickhouse-server start
clickhouse-client # or "clickhouse-client --password" if you've set up a password.
```

### Создание базы и таблицы в базе

```sql
CREATE DATABASE moex

GRANT ALL PRIVILEGES ON moex.records TO default

CREATE TABLE moex.records (
    board_id String,
    trade_date Date,
    short_name String,
    sec_id String,
    num_trades Nullable(UInt64),
    value Nullable(Float64),
    open_val Nullable(Float64),
    low_val Nullable(Float64),
    high_val Nullable(Float64),
    legal_close_price Nullable(Float64),
    wap_price Nullable(Float64),
    close_val Nullable(Float64),
    volume Nullable(Float64),
    market_price_2 Nullable(Float64),
    market_price_3 Nullable(Float64),
    admittedquote Nullable(Float64),
    mp_2_val_trd Nullable(Float64),
    market_price_3_trades_value Nullable(Float64),
    admittedvalue Nullable(Float64),
    waval UInt32 DEFAULT 0,
    trading_session Nullable(Float64),
    curren_cyid String,
    trendclspr Nullable(Float64)
) ENGINE = MergeTree()
    Partition by toYYYYMM(trade_date)
    ORDER BY (trade_date, sec_id);
```

### Запуск скрипта для загрузки данных

```shell
python load_data
```