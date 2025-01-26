import streamlit as st
import random
import time

# Set screen dimensions
WIDTH, HEIGHT = 560, 500

# Initialize game state
if 'luffy_x' not in st.session_state:
    st.session_state.luffy_x = WIDTH // 2 - 10
    st.session_state.luffy_y = HEIGHT // 2 - 10
    st.session_state.gumgum_x = random.randint(0, WIDTH - 100)
    st.session_state.gumgum_y = random.randint(0, HEIGHT - 100)
    st.session_state.score = 0
    st.session_state.start_time = time.time()

# Game Timer (60 seconds)
elapsed_time = int(time.time() - st.session_state.start_time)
if elapsed_time >= 60:
    st.warning("Game Over! Your score: " + str(st.session_state.score))
    st.stop()

# Title
st.title("🍖 Eat the Gum-Gum!")
st.write(f"Score: {st.session_state.score} | Time Left: {60 - elapsed_time} sec")

# Display images
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("room.jpg", width=WIDTH)
    st.image("luffy.png", width=100, caption="Luffy", use_column_width=False)
    st.image("gumgum.png", width=70, caption="Gum-Gum Fruit", use_column_width=False)

# Move Luffy
move = st.radio("Move Luffy:", ["Left", "Right", "Up", "Down", "Stay"])
if move == "Left" and st.session_state.luffy_x > 0:
    st.session_state.luffy_x -= 20
elif move == "Right" and st.session_state.luffy_x < WIDTH - 100:
    st.session_state.luffy_x += 20
elif move == "Up" and st.session_state.luffy_y > 0:
    st.session_state.luffy_y -= 20
elif move == "Down" and st.session_state.luffy_y < HEIGHT - 100:
    st.session_state.luffy_y += 20

# Check collision with gum-gum
if (abs(st.session_state.luffy_x - st.session_state.gumgum_x) < 50 and
    abs(st.session_state.luffy_y - st.session_state.gumgum_y) < 50):
    st.session_state.score += 1
    st.session_state.gumgum_x = random.randint(0, WIDTH - 100)
    st.session_state.gumgum_y = random.randint(0, HEIGHT - 100)
    st.success("Luffy ate a Gum-Gum Fruit! 🍖")

# Refresh
st.experimental_rerun()
