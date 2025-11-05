import streamlit as st
import random

st.set_page_config(page_title='Wordle Clone', layout='centered')

# --- Word list (keep it simple)
WORDS = ['apple', 'grape', 'pearl', 'stone', 'light', 'candy', 'pride', 'queen']

# --- Initialize game state
if 'target' not in st.session_state:
    st.session_state.target = random.choice(WORDS)
if 'guesses' not in st.session_state:
    st.session_state.guesses = []
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

st.title(' Streamlit Wordle')

# --- Function to color letters
def colorize_guess(guess, target):
    result = []
    for i, letter in enumerate(guess):
        if letter == target[i]:
            result.append(f":green[{letter.upper()}]")  # correct spot
        elif letter in target:
            result.append(f":orange[{letter.upper()}]")  # wrong spot
        else:
            result.append(f":grey[{letter.upper()}]")   # not in word
    return ' '.join(result)

# --- Input
if not st.session_state.game_over:
    guess = st.text_input(
        'Enter a 5-letter word:',
        max_chars=5,
        key=f'guess_{len(st.session_state.guesses)}'
    ).lower()

    if st.button('Submit Guess'):
        if len(guess) != 5:
            st.warning('Word must be 5 letters long, honey 💅')
        elif guess not in WORDS:
            st.warning('That word ain’t in the list, girl 😘')
        else:
            st.session_state.guesses.append(guess)
            if guess == st.session_state.target:
                st.success(f'Yaaas! You guessed it! The word was **{st.session_state.target.upper()}** 👑')
                st.session_state.game_over = True
            elif len(st.session_state.guesses) >= 6:
                st.error(f'No more guesses! The word was **{st.session_state.target.upper()}** 💀')
                st.session_state.game_over = True

# --- Show guesses
st.subheader('Your guesses:')
for g in st.session_state.guesses:
    st.markdown(colorize_guess(g, st.session_state.target))

# --- Restart
if st.session_state.game_over:
    if st.button('Play Again'):
        st.session_state.target = random.choice(WORDS)
        st.session_state.guesses = []
        st.session_state.game_over = False
        st.experimental_rerun()
