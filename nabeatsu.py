# -*- coding: utf-8 -*-
#２か９がつく数字の時アホになる
numbers = ["","いち","に","さん","よん","ご","ろく","しち","はち","きゅう","じゅう"]

print("\nニクリーチで、２と９にちなんだ短いプログラムを書けと言われて書いた。")

print("\n２か９が付く数字の時は、あほになりまーす。")

for i in range(0,31):
    yomi = ""
    tens = ""
    juu = ""
    ones = ""

    if i >= 10:
        juu = "じゅう"

    if i >= 20:
        tens = numbers[int(i/10)]

    ones = numbers[i%10]

    yomi = tens + juu + ones

    if str(i).find("2") != str(i).find("9"):
        yomi = tens + "んん" + juu + "ｎんふう" + ones + "っ！"

    print(yomi)