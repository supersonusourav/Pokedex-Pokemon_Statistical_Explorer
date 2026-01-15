# [📊 Pokémon Data Analytics & ETL Dashboard](https://pokedex-analytics-app.streamlit.app/)

A professional data-driven application that demonstrates the lifecycle of data from an external REST API to a structured analytical dashboard.

## 🧪 Data Science Objectives
- **ETL Integration:** Developed a modular Python backend (`poke_api.py`) to handle the Extraction, Transformation, and Loading of JSON data.
- **Multivariate Visualization:** Leveraged Plotly Radar Charts to perform "fingerprint" analysis of Pokémon base stats across 6 dimensions.
- **Data Integrity:** Implemented error handling and validation to ensure consistent data structures for analytical reporting.


## 🛠️ The Process
1. **Data Sourcing:** Live fetching from PokeAPI.
2. **Feature Scaling:** Normalizing base stats (0-255) for accurate visual comparison.
3. **Frontend Analytics:** Utilizing Streamlit to provide an interactive interface for Exploratory Data Analysis (EDA).

## 🚀 How to Run the Application

1. **Clone the repository:**
   ```bash
   git clone https://github.com/supersonusourav/pokedex-project.git
   cd pokedex-project
   ```
2. **Install dependencies:**

```pip
pip install -r requirements.txt
```

3. **Launch the app:**

```streamlit
streamlit run poke.py
```

🛠️ The Development Process
The project was built in three distinct phases:

1. Phase 1: Prototyping. Initial script focused on simple requests calls to PokeAPI to fetch basic JSON data.
2. Phase 2: Modularization. Refactored the code into a Two-File system (poke_api.py for logic and poke.py for UI) to ensure the code follows "Separation of Concerns."
3. Phase 3: Optimization. Integrated Plotly for comparative analytics and Streamlit ImageColumns for efficient table rendering.

⚠️ Challenges Faced & Solutions

* The "Batch Loading" Bottleneck:

  Problem: Loading images for 1000+ rows caused significant lag and 404 errors.

  Solution: Implemented a direct sprite URL mapping strategy instead of making 1000 individual API calls for each entry in the table.
* State Management:

  Problem: Switching between tabs would often reset the user's search or clear the data.

  Solution: Leveraged @st.cache_data to store API responses locally, making tab switches instant and reducing unnecessary network traffic.

📉 Drawbacks of this Integration

* Date Limiting: Since this app relies on the free version of PokeAPI, sending too many requests in a short time could lead to temporary IP blocking.
* Synchronous Requests: The current version fetches data synchronously. If the PokeAPI server is slow, the app UI may hang momentarily.
* Static Data: The app does not have a local database; if the API goes down, the entire application becomes non-functional.

🔮 Future Development (Roadmap)

* Type Filtering: Add a multi-select dropdown to filter the Library table by Pokémon types (e.g., Fire, Water).
* Evolution Chain Visualization: Use a tree-diagram to show how a Pokémon evolves.
* SQLite Integration: Implement a local database to cache data permanently, allowing the app to work offline.
* Comparison Sharing: Generate a unique URL so users can share their "Head-to-Head" comparison results.

Built by Sonu Sourav | 2026 Portfolio Project




