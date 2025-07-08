import streamlit as st
import pandas as pd
import requests
from PIL import Image
import io

# Configure the page
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
    }
    .movie-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎬 Movie Recommender System")
st.markdown("Discover your next favorite movie based on genre and language preferences!")

# Load the movie data
@st.cache_data
def load_data():
    # You can download this dataset from Kaggle: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
    df = pd.read_csv('tmdb_5000_movies.csv')
    df['genres'] = df['genres'].apply(eval)
    df['genres'] = df['genres'].apply(lambda x: [i['name'] for i in x])
    
    # Language mapping
    language_mapping = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'ja': 'Japanese',
        'ko': 'Korean',
        'zh': 'Chinese',
        'hi': 'Hindi',
        'ru': 'Russian',
        'pt': 'Portuguese',
        'nl': 'Dutch',
        'tr': 'Turkish',
        'pl': 'Polish',
        'ar': 'Arabic',
        'sv': 'Swedish',
        'da': 'Danish',
        'th': 'Thai',
        'cs': 'Czech',
        'hu': 'Hungarian',
        'vi': 'Vietnamese',
        'fa': 'Persian',
        'el': 'Greek',
        'he': 'Hebrew',
        'id': 'Indonesian',
        'no': 'Norwegian',
        'ro': 'Romanian',
        'fi': 'Finnish',
        'cn': 'Chinese'
    }
    
    # Add full language names
    df['language_full'] = df['original_language'].map(lambda x: language_mapping.get(x, x))
    return df

try:
    df = load_data()
    
    # Sidebar filters
    st.sidebar.header("Filter Movies")
    
    # Genre selection
    all_genres = set()
    for genres in df['genres']:
        all_genres.update(genres)
    selected_genre = st.sidebar.selectbox("Select Genre", sorted(list(all_genres)))
    
    # Language selection with full names
    languages = sorted(df['language_full'].unique())
    selected_language_full = st.sidebar.selectbox("Select Language", languages)
    
    # Get the language code back for filtering
    selected_language = df[df['language_full'] == selected_language_full]['original_language'].iloc[0]
    
    # Rating filter
    min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 5.0, 0.1)
    
    # Filter movies based on selection
    filtered_movies = df[
        (df['genres'].apply(lambda x: selected_genre in x)) &
        (df['original_language'] == selected_language) &
        (df['vote_average'] >= min_rating)
    ]
    
    # Display results in a grid
    if not filtered_movies.empty:
        st.subheader(f"Found {len(filtered_movies)} movies matching your criteria")
        
        # Create columns for grid display
        cols = st.columns(3)
        
        for idx, movie in filtered_movies.iterrows():
            with cols[idx % 3]:
                st.markdown("""
                    <div class="movie-container">
                        <h3>{}</h3>
                        <p><strong>Rating:</strong> ⭐ {:.1f}</p>
                        <p><strong>Release Date:</strong> {}</p>
                        <p>{}</p>
                    </div>
                """.format(
                    movie['title'],
                    movie['vote_average'],
                    movie['release_date'],
                    movie['overview'][:200] + '...' if len(movie['overview']) > 200 else movie['overview']
                ), unsafe_allow_html=True)
    else:
        st.warning("No movies found matching your criteria. Try adjusting the filters!")

except FileNotFoundError:
    st.error("""
    Please download the TMDB Movies Dataset from Kaggle:
    https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
    
    Save the 'tmdb_5000_movies.csv' file in the same directory as this script.
    """)