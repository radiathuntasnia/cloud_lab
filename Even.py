import streamlit as st

def get_even_numbers():
    p = []
    for j in range(200, 300, 1):
        if j % 2 == 0:
            p.append(j)
    return p

def main():
    """Return a friendly HTTP greeting."""
    st.title("Even Numbers Generator")
    st.write("This app generates a list of even numbers between 200 and 300.")

    # Get the list of even numbers
    even_numbers = get_even_numbers()

    # Display the list on the web interface
    st.write("List of Even Numbers:")
    st.write(even_numbers)

if __name__ == '__main__':
    main()
