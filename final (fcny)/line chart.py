import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('master_cb2.xlsx', sheet_name='master_cb2') 



plt.figure(figsize=(10, 6))
plt.plot(data['year_count'], data['count'], marker='o', linestyle='-')


plt.title('Change in Number of Rent Stablized Units by Year')
plt.xlabel('Year')
plt.ylabel('Number of Rent Controlled Units')
plt.grid(True)
plt.tight_layout()

# Show the chart
plt.show()