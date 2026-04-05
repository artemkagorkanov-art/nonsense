import re

text = """
Жирафы любять таскать
различные _СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ_
целый день напролет. Жирафы
также славяться тем, что поедают
прекрасные _СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ_, но
после этого у них часто
болит  _ЧАСТЬ ТЕЛА_. Если же
жирафы находят _ЧИСЛО_
_СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ_, у
них моментальное отваливается _ЧАСТЬ ТЕЛА_.
"""


def mad_libs(mls):
    hints = re.findall("_.*?_", mls)

    if hints is not None:
        for word in hints:
            q = "Введите {}".format(word)
            new = input(q)
            mls = mls.replace(word, new)
        print("\n")
        mls = mls.replace("\n", " ")
        print(mls)
    else:
        print("Ошибка ввода")
        mad_libs(text)


mad_libs(text)
