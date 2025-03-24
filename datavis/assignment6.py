import plotly.express as px
import pandas as pd 


df = pd.read_csv("affordable_housing.csv")
borough_rank = df.groupby("Borough")["Total Units"].sum().reset_index()

ranked_boro = borough_rank.nlargest(5, "Total Units")


fig = px.bar(
    ranked_boro, 
    x="Borough", 
    y="Total Units", 
    color="Borough",  
    title="Total New Affordable Units by Borough", 
    labels={"Projects": "Number of Projects", "Borough": "Borough"}
)

# Show the figure
fig.show()
