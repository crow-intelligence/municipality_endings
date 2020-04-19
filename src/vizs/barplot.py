import altair as alt
import pandas as pd

df = pd.read_csv("data/processed/suffix_counts_final.tsv", encoding="utf-8",
                 sep="\t")[:40]

bars = (
    alt.Chart(df)
    .mark_bar(color="#985baa", opacity=0.2)
    .encode(x="Count:Q", y="Ending:N")
)

text = bars.mark_text(align="left", baseline="middle", dx=3).encode(text="Count:Q")

plot = (bars + text).properties(height=1200, width=500)
# plot = bars.properties(height=900)
plot.save("vizualizations/barplot.png")

# import altair as alt
# from vega_datasets import data
#
# source = data.barley()
