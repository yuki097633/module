# よほど長くない限りこの書き方が推奨される
import myfirstpackage.module1
import myfirstpackage.subdir.module2

# 以下でもかける
# from myfirstpackage.subdir import module2

# from myfirstpackage.module1 import myfunc

myfirstpackage.module1.myfunc()
myfirstpackage.subdir.module2.myfunc()

# __init__にimport文を書いた
import myfirstpackage

myfirstpackage.myfunc()
