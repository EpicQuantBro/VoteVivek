import streamlit as st

# Set the title of the webpage
st.title("Here's why you should vote for Vivek")

# Create a button
if st.button("Find out why Vivek's the best option"):
    # Display candidate information when button is clicked
    st.subheader("Reasons to vote for Vivek:")
    reasons = [
        "Passionate about service and giving back to the community",
        "Hardworking and dedicated",
        "Will build up the school community and NPS's standing in Singapore",
        "Will bring the school to the forefront of Interact and community service in the country"
    ]
    for reason in reasons:
        st.write("- ", reason)
    # Add call to action
    st.markdown("### SO WHAT ARE YOU WAITING FOR? VOTE VIVEK AS YOUR INTERACT CLUB PRESIDENT NOW!!", unsafe_allow_html=True)