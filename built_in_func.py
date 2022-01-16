# dir() 使えるattributeを一覧表示する

print(dir("1"))

print(dir(__builtins__))

__builtins__.print("hello world")  # 本当はこうなっている

# __始まり__終わりの関数を定義することはできない
# built_in関数は__builtins__の中で定義されている
