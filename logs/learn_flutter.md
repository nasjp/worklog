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
  - [x] androidstudio のインストール
    - [x] emulator の作成
    - 適当にプロジェクトを作ってそっから作る
    - `~/Library/Android/sdk/emulator/emulator -avd Pixel_3a_API_R`
  - [x] xcode のインストール
    - `open -a Simulator`
  - エミュレータを指定したローカル実行
    ```sh
    $ flutter emulators
    2 available emulators:

    Pixel_3a_API_R      • Pixel 3a API R • Google • android
    apple_ios_simulator • iOS Simulator  • Apple  • ios

    $ flutter emulators --launch apple_ios_simulator
    $ flutter run
    ```
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
    - [x] `Enum`
        - ドメインオブジェクトを作る
    - [x] Null-aware演算子
      - `nullableObject?.doSomething();`
        - null じゃないときだけ実行
      - `var something = nullableObject?.something;`
        - フィールドにも使える
      - `String str = nullableNum?.toString() ?? '';`
        - 三項演算子の短縮(系)みたいなの
      - 左辺が null のときだけ右辺を代入する
        ```dart
        String str = null;
        str ??= '';
        ```
    - [x] カスケード演算子
      - map みたいな感じ?
      ```dart
      var list = [0, 1, 2, 3];
      list
        ..add(4)
        ..addAll([5, 6, 7]);
      ```
    - [ ] Stream
      - RxJava を勉強する
      - 知らない
      - RxDart をあわせて
    - [ ] asnyc / await
      ```dart
      import 'package:http/http.dart' as http;

      // Futureのメソッドチェーン <- 使わない
      void sendRequest() {
        http
          .get(url)
          .then((response) {
            print(response);
          })
          .catchError((error) => print(error));
      }

      // async / await
      Future<void> sendRequest() async {
        try {
          final response = await http.get(url);
          print(response);
        } on Exception caach (error) {
          print(error);
        }
      }
      ```
    - [ ] await for
    ```dart
    Future<int> sumStream(Stream<int> stream) async {
      var sum = 0;
      await for (var value in stream) {
        sum += value;
      }
      return sum;
    }
    ```
    - [ ] async\*/yield
      - 後で確認
    - [ ] 新しい構文
      - スプレッド演算子
        ```dart
          var list1 = [0, 1, 2, 3];
          var list2 = [4, 5, 6];
        ```
      - `Collection if`
        ```dart
          Widget build(BuildContext context) {
            return Row(
              children: [
                IconButton(icon: Icon(Icons.menu)),
                Expanded(child: title),
                if (isAndroid)
                  IconButton(icon: Icon(Icons.search)),
              ],
            );
          }
        ```
      - `Collection for`
        ```dart
        Widget build(BuildContext context) {
          return Row(
            children: [
              for (final title in titles) Text(title),
            ],
          );
        }
        ```
      - `Static extension methods`
        - 既存のクラスにあとから関数を追加
        ```dart
          extension MyFancyList<T> on List<T> {
            /// Whether this list has an even length.
            bool get isLengthEven => this.length.isEven;
          }

          [0, 1, 2].isLengthEven // -> false
        ```
      - プロジェクト構成
        - `lib` ディレクトリにソースコードを置く
        - ディレクトリがパッケージ
        - インポート
          - `import 'pakcage:{package_name}/{file_path}.dart';`
          - `import 'package:flutter/material.dart';`
          - 基本的にすべて絶対パスインポートだけしてれば良い
        - `パッケージマネージャ`
          - `pubspec.yaml`
          - `pubspec.lock` も含める
            - `dev_dependencies` と `dependencies`
              - `dev_dependencies` に テストやLintツール、Utility系のパッケージなど、成果物のアプリに含まれないパッケージ
          - `flutter pub get` でパッケージインストール
-[ ] 参考
  - プロジェクト作成
    - [Test drive - Flutter](https://flutter.dev/docs/get-started/test-drive?tab=terminal#androidstudio)
    - `flutter create myapp`
  - [Flutter開発環境構築(Mac編) - Qiita](https://qiita.com/akatsukaha/items/3b8a5a6d94a3cdb1e047)

