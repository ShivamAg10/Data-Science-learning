import seaborn as sns  
import matplotlib.pyplot as plt 

sns.set_theme()
# print(sns.get_dataset_names())

tips = sns.load_dataset("tips")
print(tips)

sns.relplot(
    data = tips,
    x = "total_bill",
    y = "tip",
    hue="smoker"
)
# plt.show()