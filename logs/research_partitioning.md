# マルチテナントSaaSデータベース

Refs: <https://docs.microsoft.com/ja-jp/azure/sql-database/saas-tenancy-app-design-patterns>

![Selecting the Database Model for our App](https://miro.medium.com/max/2062/1*F4sJPy51tT90R3gOzlsxjA.png)

- Mysql パーティショニング
  - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-types.html>
  - パーティションのキーにしたいカラムをプライマリーキーに含める必要がある
  - 事業者の追加ごとに ALTER する必要がある
  - パーティショニングの種類
    - RANGE パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-range.html>
        - table 定義にそれぞれのパーティションの定義を書く
        - id が 1~ 99999999 はXXみたいな感じになる
        - SaaSは使えない
    - LIST パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-list.html>
        - これも table 定義にそれぞれのパーティションの定義を書く
        - id も
        - SaaSは使えない
    - COLUMNS パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-columns.html>
        - RANGE パーティショニング と LIST パーティショニング は id だったがそれを別のカラムにできる
        - これは使えるかも
    - HASH パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-hash.html>
        - hash 値を格納するカラムとパーティショニングする数を定義に書く
        - 1000 とかで作っておくのか?
        - 基本的に一つのカラム、線形関数を用いると早い
        - 普通にcompany_id みたいな感じで使える
        - 保留
    - LINEAR HASH パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-linear-hash.html>
      - HASH パーティショニングとほぼ同じ
      - 線形ハッシュによるパーティショニングの利点は、パーティションの追加、削除、マージ、および分割の速度が向上する
      - 非常に大量 (テラバイト) のデータが含まれるテーブルを扱うときに利点になることがある
      - 欠点は、通常のハッシュパーティショニングを使用して獲得される配分と比べて、データがパーティションに均等に配分される可能性が低い
    - KEY パーティショニング
      - <https://dev.mysql.com/doc/refman/5.6/ja/partitioning-key.html>
        - 仕組みはHASHパーティショニングと同じ
        - ハッシュ関数がMysqlから提供される
    - サブパーティショニング
      - パーティショニングをさらにパーティショニング
        - SaaSは使えない
