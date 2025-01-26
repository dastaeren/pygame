import streamlit as st
import random
import time
from PIL import Image

# Game settings
WIDTH, HEIGHT = 560, 500
game_duration = 60  # Game time in seconds

# Initialize game state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# Load images
room_img = Image.open("room.jpg").resize((WIDTH, HEIGHT))
luffy_img = Image.open("luffy.png").resize((150, 130))
gumgum_img = Image.open("gumgum.png").resize((70, 120))

# Display background image
st.image(room_img, caption="Background Room", use_column_width=True)

# Game logic
def start_game():
    st.session_state.game_started = True
    st.session_state.start_time = time.time()
    st.session_state.score = 0

# Game timer and scoring
if st.session_state.game_started:
    elapsed_time = time.time() - st.session_state.start_time
    remaining_time = max(0, game_duration - int(elapsed_time))
    
    if remaining_time <= 0:
        st.session_state.game_started = False
        st.write(f"Game Over! Your score is: {st.session_state.score}")
        st.button("Start Again", on_click=start_game)
    else:
        # Display game timer
        st.write(f"Time Remaining: {remaining_time} seconds")

        # Game logic for moving Luffy to catch the GumGum fruit
        luffy_position = st.slider("Move Luffy (Position X)", 0, WIDTH-150, WIDTH//2)
        gumgum_position_x = random.randint(0, WIDTH - 70)
        gumgum_position_y = random.randint(0, HEIGHT - 120)

        st.image(luffy_img, width=150, use_column_width=False, caption="Luffy", use_container_width=False)
        st.image(gumgum_img, width=70, use_column_width=False, caption="Gum Gum", use_container_width=False)

        # Check if Luffy catches the GumGum fruit
        if abs(luffy_position - gumgum_position_x) < 100:
            st.session_state.score += 1
            st.write(f"Score: {st.session_state.score}")
        
else:
    st.write("Welcome to 'Eat the GumGum' game!")
    st.write("Move Luffy to catch the Gum-Gum fruit within 60 seconds!")
    st.button("Start Game", on_click=start_game)

