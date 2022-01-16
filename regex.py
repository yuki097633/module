import re  #Regular Expression（正規表現）


email = "myemail@gmail.com"

# @の後に１文字以降のアルファベットの後に.がある
matched = re.search("@\w+\.", email)
if matched:
    print(matched)
    print("Matched")
else:
    print("Not found")


# [] 文字列の中の文字をサーチ
print(re.search("[abc]", "apple"))
print(re.search("[abc]", "01234"))
print(re.search("[a-c]", "apple"))
print(re.search("[1-4]", "7654"))

# ^ 最初の文字をサーチ
print(re.search("^[1-4]", "7654"))
print(re.search("^[1-4]", "4567"))

# {n} n回リピート
print(re.search("^[0-9]{4}", "2021/1/13"))

# {n,m} 最低n回, 最高m回リピート
print(re.search("^[0-9]{2,4}", "21/1/13"))

# $ 最後の文字
print(re.search("[0-9]{2}$", "2021/1/13"))

# * 左のパターンを0回以上繰り返す aを0回以上繰り返してbかどうか
print(re.search("a*b", "ab"))

# + 左のパターンを1回以上繰り返す
print(re.search("a+b", "ab"))

# + 左のパターンを0回か1回繰り返す
print(re.search("ab?c", "ababc"))

# | or
print(re.search("abc|012", "abc"))

# () グループ
print(re.search("te(s|x)t", "test"))

# . 任意の１文字
print(re.search("h.t", "hat"))

# \ エスケープ
print(re.search("h\.t", "h.t"))

# \w [1-zA-Z0-9_] 1文字の全てのアルファベット、数字およびアンダースコア
print(re.search("h\wt", "hat"))


pattern_deb = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])$"
while True:
    date = input("日付を入力してください yyyy/mm/dd")
    if re.search(pattern_deb, date):
        print("ok")
        break
    else:
        print("正しく入力してください")


pattern_email = "^(\w|\.|-)+@(\w|\.|-)+\.[a-zA-Z]{2,3}$"

