import pandas as pd
import random

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})

# Преобразование в one-hot кодировку
categories = pd.unique(data["whoAmI"])
one_hot = pd.DataFrame(0, columns=categories, index=data.index)
one_hot = one_hot.add(pd.get_dummies(data["whoAmI"]), fill_value=0)

# Объединение исходного DataFrame с one-hot кодировкой
data = data.join(one_hot)
data.head()
