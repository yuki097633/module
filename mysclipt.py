import sys
# import mymodule as mm  # モジュールファイル丸ごと 自前のasは非推奨
from mymodule import myfunc, myvariable  # 特定のオブジェクトのみ
# from mymodule import *  # これでも可だがわからなくなるので非推奨

myfunc()
print(myvariable)


# sysはビルドインモジュール
# importするモジュールはsys.path内にある必要がある
print(sys.path)


# importする順番
# 標準ライブラリ、サードパーティのライブラリ、自分たちのライブラリ、ローカルのライブラリ