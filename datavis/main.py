import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns  
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

###    PLOTLY   ###
## class exercise ## 
df = pd.read_csv("pokemon.csv")
top_fire_pokemon = df[df["Type 1"] == "Fire"].nlargest(10, "Attack")
top_water_pokemon = df[df["Type 1"] == "Water"].nlargest(10, "Attack")

fig = make_subplots(
    rows=1, 
    cols=2, 
    subplot_titles=["Top 10 Fire Pokémon by Attack", 
        "Top 10 Water Pokémon by Attack"])

fig.add_trace(
    go.Bar(
        x=top_fire_pokemon["Name"],
        y=top_fire_pokemon["Attack"],
        marker_color='darksalmon',
        text=top_fire_pokemon["Attack"],
        textposition='auto',
        hoverinfo="text",
        hovertext=[f"{name}<br>Attack: {attack}" for name, attack in 
                  zip(top_fire_pokemon["Name"], top_fire_pokemon["Attack"])]),
    row=1, col=1)

fig.add_trace(
    go.Bar(
        x=top_water_pokemon["Name"],
        y=top_water_pokemon["Attack"],
        marker_color='darkseagreen',
        text=top_water_pokemon["Attack"],
        textposition='auto',
        hoverinfo="text",
        hovertext=[f"{name}<br>Attack: {attack}" for name, attack in 
                  zip(top_water_pokemon["Name"], top_water_pokemon["Attack"])]),
    row=1, col=2)

fig.update_layout(
    title_text="Top 10 Pokemon by Attack for Fire and Water Types",
    height=500,
    width=1000,
    showlegend=False)

fig.update_xaxes(tickangle=45)

fig.show()




## bar chart ## 

# df = pd.read_csv("pokemon.csv")
# top_attack_pokemon = df.nlargest(10, "Attack")  

# fig = px.bar(
#     top_attack_pokemon, 
#     x= "Name", 
#     y = "Attack", 
#     color= "Name")

# fig.show()

 ## scatter plot## 
# df = pd.read_csv("pokemon.csv") 

# fig = px.scatter(df, x="Attack", y="Speed", color="Type 1", size_max= 10, size= "Defense",
#                  hover_name="Name", hover_data= ["HP", "Defense"],  title="Pokémon Attack vs. Speed")
# fig.show()





 ### panda ###
# df = pd.read_csv("pokemon.csv")

# selected_types = ["Fire", "Water", "Grass", "Electric"]
# filtered_df = df[df["Type 1"].isin(selected_types)]
# types_palette={"Fire": "red", "Water": "blue", "Grass": "green", "Electric": "yellow"}

# sns.scatterplot(x="Attack", y="Defense", hue="Type 1", data=filtered_df, palette=types_palette)

# plt.title("Attack vs. Defense of Selected Pokémon Types")
# plt.xlabel("Attack")
# plt.ylabel("Defense")
# plt.legend(title="Type 1")


# plt.show()


###nmaking data set w a csv ###

# df = pd.read_csv("pokemon.csv")
# unique_types= df["Type 1"].value_counts().index
# type_counts =df["Type 1"].value_counts().values
# colors= sns.color_palette("tab20", n_colors=len(unique_types))

# plt.bar(unique_types, type_counts, color = colors )
# plt.xlabel("Primary Type")
# plt.xticks(rotation=45)
# plt.ylabel("Count")
# plt.title("Distribution of Pokémon by Type 1")
# plt.show()



### basic matplotlib stuff ##
#import matplotlib.pyplot as plt 

### TWO plots ###

# fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# ax[0].bar(['a', 'b', 'c'], [10, 20, 15])
# ax[0].set_title("my chart")

# ax[1].plot([1, 2, 3], [5, 10, 15] , marker='*', color='green', linestyle='-.',)
# ax[1].set_title("my other chart")


# plt.show()


#### scatter plot ###
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# y = [5, 15, 10, 20, 18, 25, 30, 22, 28, 35]  
# sizes = [value * 10 for value in y ]
# colors=x

# plt.scatter(x, y, s=sizes,c=colors,cmap='gist_rainbow')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Scatter Plot")
# plt.colorbar(label="Color Scale")
# plt.show()





### scatter plot ###
# x = ["a", "b", "c", "d", "e"]
# y = [10, 20, 25, 30, 40]
# colors = ["red", "green", "blue", "orange", "purple"]

# plt.plot(x, y, marker='o', linestyle='-', color='m', label='my line plot')
# plt.xlabel("categories")
# plt.ylabel("values")
# plt.title("my first chart")
# plt.legend()
# plt.show()

