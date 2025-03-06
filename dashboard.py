import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("./assets/cereal.csv")
    return df

df = load_data()

st.sidebar.header("Filtros")
manufacturers = st.sidebar.multiselect("Fabricante", df["mfr"].unique(), df["mfr"].unique())
type_filter = st.sidebar.multiselect("Tipo", df["type"].unique(), df["type"].unique())
calories_range = st.sidebar.slider("Calorias", int(df["calories"].min()), int(df["calories"].max()), (50, 200))

df_filtered = df[df["mfr"].isin(manufacturers) & df["type"].isin(type_filter) & df["calories"].between(calories_range[0], calories_range[1])]

st.title("📊 Dashboard de Cereais")
st.write("Explore os dados nutricionais dos cereais de diferentes fabricantes.")

st.subheader("Dados Filtrados")
st.dataframe(df_filtered)

st.subheader("Distribuição de Calorias")
fig = px.histogram(df_filtered, x="calories", nbins=20, title="Distribuição de Calorias nos Cereais")
st.plotly_chart(fig)

st.subheader("Comparação Nutricional")
nutrition_fig = px.histogram(df_filtered, x="mfr", y="protein", title="Proteína por Fabricante")
st.plotly_chart(nutrition_fig)

best_cereal = df.loc[df['rating'].idxmax()]
st.subheader("🥇 Melhor Cereal")
st.write(f"O cereal com maior rating é **{best_cereal['name']}**, com nota **{best_cereal['rating']}**!")
