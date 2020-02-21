# flutter の学習

Refs: [Flutter 全部俺 Advent Calendar 2019 - Adventar](https://adventar.org/calendars/4140)

- [ ] 環境構築
  - [x] analysis-server-dart-snapshot を LSP として使う
    -  [vim-lsp-settings/install-analysis-server-dart-snapshot.sh at master · mattn/vim-lsp-settings](https://github.com/mattn/vim-lsp-settings/blob/master/installer/install-analysis-server-dart-snapshot.sh)
  - [x] [DevTools - Flutter](https://flutter.dev/docs/development/tools/devtools) をダウンロード
    - ブラウザでデバッグするためのツール
  - [x] [sdk/pkg/analyzer at master · dart-lang/sdk](https://github.com/dart-lang/sdk/tree/master/pkg/analyzer) をダウンロード
    - dartfmt とかある
  - [x] [dart-lang/dart-vim-plugin: Syntax highlighting for Dart in Vim](https://github.com/dart-lang/dart-vim-plugin) vim はこれで良さそう
    - [ ] vim-lsp と併用するのかこれだけでできるのか後に確認
- [ ] 構文
  - [ ] 高階関数
    - 理解ができなかった
    - `Widget Function(BuildContext) builder = (context) => Container();`
    - 見にくいからこうする
      ```dart
      typedef WidgetBuilder = Widget Function(BuildContext context);

      WidgetBuilder builder = (context) => Container();
      ```
  - [x] 型推論
    - `var a = 1;`
  - [x] `final int a = 1;`
    - 再代入不可
    - `List<T>` 内は変更できる
  - [x] `const`
    - 参照先の変更さえもさせない
    - 使える場合はこっちを使う
    - `dartanalyzer` でつけるべきとろこを確認できる
  - [x] クラス
    - `new` をつけなくてもつけてもインスタンスを生成できる
    - できるけど基本的につけない
    - コンストラクタのインスタンス変数初期化は省略を使う
    - インスタンス変数がすべて`final` だと`const constructor` にすることができる
    - `final`なフィールドはコンストラクタの`body`で初期化できない
      - `Initializer`を機能を使う
      - コロンに続いて、コンマ区切りの初期化処理を書く
        ```dart
        class Dog {
          final String name;
          final Owner owner;

          const Dog(this.name): owner = Owner('John');
        }
    ```
    - 名前付きコンストラクタ
    - 別のコンストラクタにリダイレクト(`Initializer` の最後に書く(`this()`))
      ```dart
      class Dog {
        String name;
        final Owner owner;

        Dog(this.name): this.owner = Owner('John');

        Dog.pochi(): this.name = 'Pochi',
                     this.owner = Owner('John');

        Dog.taro(String name): this(name);
      }
      ```
    - [x] 継承
      - `extends` => 実装全てを引き継ぐ
      - `implements` => インターフェイスを引き継ぐ
        - (クラスからインターフェイスのみを引き継ぐことも可能)
      - `Mixin`
        - `with` を `exteds` のあとに書く
        ```dart
        mixin Swimmer {
          void swim() { ... }
        }

        class Creature {}

        class Mammal extends Creature {}

        class Fish extends Creature {}

        class Dolphin extends Mammal with Swimmer {}

        class Shark extends Fish with Swimmer {}
        ```
    - [x]`Enum`
        - ドメインオブジェクトを作る

- [ ] [すぐにFlutterを始めたい人のためのDart入門(後編)](https://itome.team/blog/2019/12/flutter-advent-calendar-day4/) 明日はここから
