import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="TEST APP",
    page_icon="🧊",
    layout="wide"
)

st.title("🎈Streamlitで国土地理院地図を表示するテスト")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

fig = go.Figure()

L1 = go.Scattermapbox(
    lat=[35.699],
    lon=[139.744],
    mode='markers',
    text=['hoge'],
    marker = dict(
    size = 30
    )
)
fig.add_trace(L1)

fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
    {
    "below": 'traces',
    "sourcetype": "raster",
    "source": [
    "https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png"
    ]
    }
    ],
    mapbox = {
    "zoom" : 13,
    "center" : {'lon': 139.744, 'lat': 35.699}
    },
    width=1000,
    height=1000
)


st.plotly_chart(fig)