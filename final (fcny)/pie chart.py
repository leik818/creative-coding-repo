### 2017 ####

# import pandas as pd
# import matplotlib.pyplot as plt


# data = pd.read_excel('master_cb2.xlsx', sheet_name='master_cb2') 


# data = data.dropna(subset=['type_2017', 'sub_2017'])
# data['sub_2017'] = pd.to_numeric(data['sub_2017'], errors='coerce')
# data = data.dropna(subset=['sub_2017'])


# labels = data['type_2017']
# sizes = data['sub_2017']


# explode = [0.03] * len(sizes)


# plt.figure(figsize=(10, 8))
# wedges, texts, autotexts = plt.pie(
#     sizes,
#     explode=explode,
#     autopct='%1.1f%%',
#     startangle=90,
#     textprops={'fontsize': 8}
# )


# plt.legend(wedges, labels, title="Type of Loss", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# plt.title('Subtractions from Rent-Stabilized Housing Stock in Manhattan, 2017')
# plt.axis('equal')  
# plt.tight_layout()
# plt.show()




#####2023######
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
data = pd.read_excel('master_cb2.xlsx', sheet_name='master_cb2') 

# Clean the data
data = data.dropna(subset=['type_2023', 'sub_2023'])
data['sub_2023'] = pd.to_numeric(data['sub_2023'], errors='coerce')
data = data.dropna(subset=['sub_2023'])

# Extract labels and sizes
labels = data['type_2023']
sizes = data['sub_2023']

# Optional: explode slices slightly
explode = [0.03] * len(sizes)

# Create the pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    sizes,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 8}
)

# Add legend to the side
plt.legend(wedges, labels, title="Type of Loss", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.title('Subtractions from Rent-Stabilized Housing Stock in Manhattan, 2023')
plt.axis('equal')
plt.tight_layout()
plt.show()
