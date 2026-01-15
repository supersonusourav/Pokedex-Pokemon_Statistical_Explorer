import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from poke_api import PokeAPI

st.set_page_config(page_title="Advanced Pokédex Explorer", layout="wide")
poke_engine = PokeAPI()

st.title("📊 Pokémon Statistical Explorer")

tab1, tab2, tab3 = st.tabs(["🔍 Feature Analysis", "📂 Dataset Reference", "⚔️ Multivariate Comparison"])

# --- TAB 1 & 3 remain the same as previous version ---

with tab1:
    search = st.text_input("Enter Name or ID", value="Lucario")
    data = poke_engine.get_details(search)
    if data:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image(data['sprites']['other']['official-artwork']['front_default'], use_container_width=True)
            st.metric("Pokedex ID", f"#{data['id']}")
        with c2:
            st.header(data['name'].title())
            for stat in data['stats']:
                st.progress(stat['base_stat']/255, text=f"{stat['stat']['name'].title()}: {stat['base_stat']}")

# --- TAB 2: FULL LIBRARY (With Image Rendering) ---
with tab2:
    st.subheader("📚 Master Pokémon Reference Table")
    
    if st.button("🔄 Fetch/Refresh Entire Library"):
        with st.spinner("Accessing API database..."):
            library_data = poke_engine.get_full_library(1025)
            
            if library_data:
                df = pd.DataFrame(library_data).set_index("ID")
                
                # We use column_config to render the 'Sprite' URL as an actual Image
                st.dataframe(
                    df, 
                    use_container_width=True, 
                    height=600,
                    column_config={
                        "Sprite": st.column_config.ImageColumn("Icon", help="Pokémon Sprite"),
                        "Name": st.column_config.TextColumn("Pokémon Name"),
                        "Data Link": st.column_config.LinkColumn("Raw JSON Data")
                    }
                )
                st.success(f"Successfully loaded {len(df)} Pokémon with icons!")
            else:
                st.error("Could not retrieve library.")

# --- TAB 3: COMPARISON ---
with tab3:
    st.subheader("⚔️ Head-to-Head Comparison")
    c_in1, c_in2 = st.columns(2)
    p1 = poke_engine.get_details(c_in1.text_input("Pokémon 1", value="Gengar", key="p1"))
    p2 = poke_engine.get_details(c_in2.text_input("Pokémon 2", value="Alakazam", key="p2"))

    if p1 and p2:
        labels = [s['stat']['name'].title() for s in p1['stats']]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[s['base_stat'] for s in p1['stats']], theta=labels, fill='toself', name=p1['name'].title()))
        fig.add_trace(go.Scatterpolar(r=[s['base_stat'] for s in p2['stats']], theta=labels, fill='toself', name=p2['name'].title()))
        st.plotly_chart(fig, use_container_width=True)