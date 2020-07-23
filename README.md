ローカルでビルド、起動
```
$ sam build --use-container
$ sam local start-api
```

AWS CLIにプロファイル情報書き込み
```
$ aws configure --profile local
AWS Access Key ID [None]: dummy
AWS Secret Access Key [None]: dummy
Default region name [None]: ap-northeast-1
Default output format [None]: json
```

DynamoDB Localにテーブルを配置(Docker)
```
$ docker network create lambda-local-test
$ docker run -itd --network lambda-local-test --name dynamoTest -p 8000:8000 amazon/dynamodb-local:latest -jar DynamoDBLocal.jar -sharedDb
$ aws dynamodb --profile local --endpoint-url http://localhost:8000 create-table --cli-input-json file://tabledata/db_local.json
```
