import streamlit as st
import time
import random
from random import randint
import ast
import math

def draw_big_number(digits = 3):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return randint(range_start, range_end)


def draw_from_large_set(n):
    large_numbers = [25, 50, 75, 100]
    return random.sample(large_numbers, n)

def draw_from_small_set(n):
    small_numbers = [ 1 , 1 , 2 , 2 , 3 , 3 , 4 , 4 , 5 , 5 , 6 , 6 , 7 , 7 , 8 , 8 , 9 , 9 , 10 , 10]
    return random.sample(small_numbers, n)

def draw_numbers(n_large_numbers, total_numbers = 6):
    return draw_from_large_set(n_large_numbers) + draw_from_small_set(total_numbers - n_large_numbers)

def parse_calculation(calc_string):
    node = ast.parse(calc_string, mode='eval')
    result = eval(compile(node, '<string>', 'eval'))
    return result

def compute_score(user_input):
    # Replace this with your game logic to compute the score based on user input
    return len(user_input)

def main():
    st.title("My Simple Game")
    st.write("Welcome to the game!")

    large_numbers = st.selectbox("How many large numbers do you want to try? (0-4)", list(range(5)))

    if st.button("Start Game"):
        st.write("Game started!")

        # Generate the set of 6 numbers
        numbers = draw_numbers(large_numbers)

         # Calculate the dimensions for displaying the numbers
        num_boxes = len(numbers)
        box_size = 100 # Maximum size of each box is 200 pixels

        # Display the numbers in a row
        container_style = f"display: flex; flex-wrap: nowrap; gap: 5px; flex-direction: row; width: {num_boxes * box_size + 25}px;"

        with st.container():
            st.markdown(
                f'<div style="{container_style}">',
                unsafe_allow_html=True
            )

            for number in numbers:
                box_style = f"width: {box_size}px; height: {box_size}px; " \
                            f"background-color: blue; color: white; text-align: center; line-height: {box_size}px;"
                st.markdown(
                    f'<div style="{box_style}">{number}</div>',
                    unsafe_allow_html=True
                )

            st.markdown('</div>', unsafe_allow_html=True)

        # Display the timer
        timer_length = 30  # 30 seconds
        timer = st.empty()

        start_time = time.time()
        while time.time() - start_time < timer_length:
            remaining_time = int(timer_length - (time.time() - start_time))
            timer.text(f"Time remaining: {remaining_time} seconds")
            time.sleep(1)

        timer.text("Time's up!")

        # Display the text box for user input
        user_input = st.text_input("Enter a string")

        if st.button("Compute Score"):
            # Compute the score based on user input
            score = compute_score(user_input)
            st.write(f"Your score is: {score}")

if __name__ == "__main__":
    main()
