myvariable = "my global valiable"

def myfunc():
    print("my function")


# _始まりにするとノンパブリックの慣習（importされない）
def _anotherfunc():
    print("another function")

# importされた時に実行されないようにする
if __name__ == "__main__":
    print("This is mymodule")
    print(f"mymodule.__name__: {__name__}")