当リポジトリはPython向けのオニオンアーキテクチャの雛型です。


以下が各レイヤと機能群についての概要となります。
```
domain layer
    domain model
        ビジネスロジックを表現するオブジェクトやクラス
    domain service
        ドメインモデルを操作するためのサービスクラス
    repository
        データの永続性を管理し、データベースとのインタラクションを提供するクラス
```
```
application layer
    usecase
        特定のユーザー操作やビジネスロジックを実行するクラス
    service
        UIや外部リクエストに対する操作を提供するAPIクラス
```
```
infrastructure layer
    filesystem API
        ファイルアクセスを提供するクラス
    database API
        データベース接続を提供するクラス
    external API
        外部サービス接続を提供するクラス
```
```
ui layer
    controller
        ユーザーのリクエストをapplication serviceへ転送するクラス(cli, pysimplegui, flask, ...)
    router
        ユーザーのリクエストをコントローラにルーティングするクラス
    viewer
        ユーザーの情報を渡し、ユーザーの情報を受ける部分
```

