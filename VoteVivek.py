import streamlit as st

# Define the main page function
def main_page():
    st.title("Here's why you should vote for Vivek")

    # Create a button that leads to the second page
    if st.button("Find out why Vivek's the best option"):
        # Change the state to reflect the second page
        st.session_state.page = "second"

# Define the second page function
def second_page():
    st.subheader("Reasons to vote for Vivek:")
    reasons = [
        "Passionate about service and giving back to the community",
        "Hardworking and dedicated",
        "Will build up the school community and NPS's standing in Singapore",
        "Will bring the school to the forefront of Interact and community service in the country"
    ]
    for reason in reasons:
        st.write("- ", reason)
    st.markdown("### SO WHAT ARE YOU WAITING FOR? VOTE VIVEK AS YOUR INTERACT CLUB PRESIDENT NOW!!", unsafe_allow_html=True)

# Application Logic
if 'page' not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    main_page()
else:
    second_page()
