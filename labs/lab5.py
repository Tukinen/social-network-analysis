import networkx as nx  # Граф боловсруулах сан
import warnings  # Санамж (warning) мессежүүдийг дарах сан
import pandas as pd  # Өгөгдөл боловсруулах сан (энэ кодонд ашиглаагүй)
import numpy as np  # Тоон өгөгдөл тооцоолох сан (энэ кодонд ашиглаагүй)
import matplotlib.pyplot as plt  # График дүрслэх сан
import powerlaw  # Эрчим хүчний хууль (power law) тархалтыг шинжлэх сан (энэ кодонд ашиглаагүй)

# Санамж мессежүүдийг дарах
warnings.filterwarnings('ignore')  # Санамж мессежүүдийг харуулахгүй болгох

# Эрдос-Реньийн санамсаргүй граф үүсгэх (100 зангилаа, 6% холболтын магадлалтай)
er = nx.erdos_renyi_graph(100, 0.06)  # 100 зангилаатай граф, хоёр зангилаа хоорондын холболт 6%

# Графыг дүрслэх (хар шугамтай, 30 пикселийн зангилаатай, шошгогүй)
nx.draw(er, node_size=30, edge_color="black", with_labels=False)

# Зураг харуулах
plt.show()  # Графын зургийг дэлгэцэнд харуулах

# Хувийн сүлжээний CSV файлыг унших
g = nx.read_edgelist("E:/Niigmiin medeelel ba suljeenii/lab zaavar/network (1).csv", delimiter=",", nodetype=int)


# Бодит графын degree тархалтыг тохируулах
sequence = [i[1] for i in g.degree()]  # Графын зангилааны түвшингийн жагсаалт

# Configuration Model үүсгэх
cm = nx.configuration_model(sequence)

# Бодит граф болон Configuration Model-ийн degree тархалтыг тооцоолох
hist_o = nx.degree_histogram(g)  # Бодит графын degree тархалт
hist = nx.degree_histogram(cm)  # Configuration Model-ийн degree тархалт

# Хоёр графын тархалтыг харуулах
fig = plt.figure(figsize=(16, 6))  # Зургийн хэмжээ
plt.subplot(1, 2, 1)  # 1-р хэсэг
plt.plot(range(0, len(hist_o)), hist_o, ".")  # Бодит графын degree тархалтыг дүрслэх
plt.title("Degree Distribution Real Graph")  # Гарчиг
plt.xlabel("Degree")  # X таг
plt.ylabel("#Nodes")  # Y таг
plt.loglog()  # Лог-лог масштабтай

plt.subplot(1, 2, 2)  # 2-р хэсэг
plt.plot(range(0, len(hist)), hist, ".")  # Configuration Model-ийн degree тархалтыг дүрслэх
plt.title("Degree Distribution Configuration Model")  # Гарчиг
plt.xlabel("Degree")  # X таг
plt.ylabel("#Nodes")  # Y таг
plt.loglog()  # Лог-лог масштабтай

# Зураг харуулах
plt.tight_layout()  # Зургуудын зайг зохицуулах
plt.show()  # Зураг харуулах
