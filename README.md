# コピーされた重複ファイルのリストアップ
例えば"D3321.JPG"というファイルがあるとして、同じ場所に同じものをコピーしてしまったときに、  

"D3321-2.JPG"  
"D3321-3.JPG"...  
や、使うソフトによっては  
"D3321 2.JPG"  
"D3321 3.JPG"...  
とかいうファイルが作成されます。

それらを見つけて(パス付きで)リストアップするスクリプトです。  

拡張子は画像以外でも指定できます。

## 動作
同じディレクトリに例えば   
"D3321.JPG"  
"D3321-2.JPG"  
"D3321 3.JPG"  
があるときに、  
"D3321-2.JPG"や"D3321 3.JPG"のほうをリストアップします



## どんなときに使うか
Adobe Lightroomで、同じ写真がなぜか何枚も増えてしまっており、それらを削除するのに使いました。

[Teekesselchen](http://www.bungenstock.de/teekesselchen/)というプラグインもありますのでよく仕様を理解した上で使えば似たようなことができると思います。  
  
(が、こちらは撮影日時や機種や設定などから同じ写真を探すプラグインであり、  
「同じディレクトリに"D3321.JPG"と"D3321-2.JPG"や"D3321 3.JPG"が存在するときのみ、"D3321-2.JPG"や"D3321 3.JPG"のほうをduplicatedとする」  
と言う風な指定はできないっぽいです。そのためスクリプトを作成しました。もしかしたらできたのかもしれませんが。)

## usage
以下のようにディレクトリも再帰的に辿る`--recursive`オプションや、扱うファイルの拡張子をリストで指定する`--extention_list`オプションがあります。

```
$ python3 pickup_copied_file_by_name.py -h
usage: pickup_copied_file_by_name.py [-h] [-r]
                                     [-e EXTENSION_LIST [EXTENSION_LIST ...]]
                                     [--debug]
                                     arg1

listup duplicate photos

positional arguments:
  arg1                  target dircotry.

optional arguments:
  -h, --help            show this help message and exit
  -r, --recursive       traverse directory recursively.
  -e EXTENSION_LIST [EXTENSION_LIST ...], --extension_list EXTENSION_LIST [EXTENSION_LIST ...]
                        target extensions.
  --debug               enable debug mode.

```

リストアップさせて削除  
(名前に空白を含むファイルは、そこで区切られてしまうので、`tr`コマンドや`xargs`の`-x0`オプションを使ったりしている)  

```
$ python3 pickup_copied_file_by_name.py ~/picture/ > rmvlist.txt  
$ cat rmvlist.txt | tr "\n" "\0" | xargs -x0 -n1 sh -c 'rm "$0"'
```
