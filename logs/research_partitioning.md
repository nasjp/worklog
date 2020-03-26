# マルチテナントSaaSデータベース

Refs: <https://docs.microsoft.com/ja-jp/azure/sql-database/saas-tenancy-app-design-patterns>

- Mysql パーティショニング
  - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-types.html>
  - パーティショニングの種類
    - RANGE パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-range.html>
        - table 定義にそれぞれのパーティションの定義を書く
        - 事業者の追加ごとに ALTER する必要がある
        - id が 1~ 99999999 はXXみたいな感じになる
        - 使えない
    - LIST パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-list.html>
        - これも table 定義にそれぞれのパーティションの定義を書く
        - 事業者の追加ごとに ALTER する必要がある
        - id も
        - 使えない

    - COLUMNS パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-columns.html>
        - RANGE パーティショニング と LIST パーティショニング は id だったがそれを別のカラムにできるだけ
        - つまり使えない
    - HASH パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-hash.html>
        - hash 値を格納するカラムとパーティショニングする数を定義に書く
        - 1000 とかで作っておくのか?
        - 基本的に一つのカラム、線形関数を用いると早い
        - 普通にcompany_id みたいな感じで使える
        - 保留
    - LINEAR HASH パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-linear-hash.html>
    - KEY パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-key.html>
        - 仕組みはHASHパーティショニングと同じ
        - ハッシュ関数がMysqlから提供される
    - サブパーティショニング
