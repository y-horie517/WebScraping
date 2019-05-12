# webスクレイピング学習用プログラム
* Python 3.7.3
* Yahoo!ニュースのトップニュースのタイトルを取得し、カテゴリ別にテキストファイルへ書き込みするプログラム

## クローリングとは
クローリングとは、複数のウェブサイトのリンクをなぞってウェブページを探すことでそれを行うプログラムをクローラーと呼びます。

## スクレイピングとは
またスクレイピングとは、ウェブサイトのHTMLから必要なデータを取得することでそれを行うプログラムをスクレイパと呼びます。

* クローラによって必要な情報のページまでいき
* スクレイパによって実際に取得する

## スクレイピングの大別
* 標準ライブラリを用いて生書きでスクレイピング
  * 標準ライブラリを用いる方法は、スクレイピングの基礎となる考え方や方法を学べますが、文字コード問題の対応がめんどくさかったり、大規模なスクレイピングをするときには大変です。


* 強力なライブラリを用いてスクレイピング
  * 強力なライブラリを用いる方法は、ライブラリによってかなり楽をでき、サクッとスクレイピングできます。
* フレームワークを用いてスクレイピング
  * フレームワークを使う方法は、PythonではScrapyというフレームワークが有名ですが、そのものの学習コストもありますし、大型のフレームワークですので、小規模なスクレイピングには向いていません

## Pythonの代表的なライブラリ
* Requests: Webページを取得して、そのWebページを解析する
* Beautiful Soup: HTMLからその情報をスクレイピングするためのもの