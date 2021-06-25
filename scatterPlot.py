import pandas as pd
import plotly.express as px

df = pd.read_csv("CovidData.csv")
fig = px.scatter(df, x="date", y="cases",
	          size="cases",color="country",
                   size_max=15,title="Covid Cases")
fig.show()