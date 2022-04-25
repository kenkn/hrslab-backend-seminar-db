## 動作
### JWT 生成のための secretkey 発行
```
openssl rand -hex 32 > secret_key.txt
```

docker-compose.yml の local-data-api service の environment に追加

```
environment:
    SECRET_KEY: <secret key>
```

### コンテナ起動
```
$ docker-compose up
```

### API コール例

#### OAuth クライアント作成
POST: http://localhost:8000/google-analytics/client
リクエストボディ

```json
{
    "client_id": ,
    "client_secret": ,
    "refresh_token": 
}
```

#### GA レポート取得

GET: http://localhost:8000/google-analytics/?tenant_id=<tenant_id>&account_id=<account_id>&property_id=<property_id>&end_date=<end_date>

#### pgAdmin
http://localhost:81
email : test@ficilcom.jp
pass : admin

### その他
M1 Mac だとコンテナ立ち上げ時に怒られるかも
