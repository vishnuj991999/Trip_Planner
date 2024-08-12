# main.py

import streamlit as st
from tasks import generate_trip_plan

def main():
    st.title('VJ Holidays')

    source = st.text_input('Enter Source City')
    destination = st.text_input('Enter Destination City')
    mode = st.selectbox("Mode Of Transport", ["Flight", "Train", "Bus", "Car"])
    days = st.number_input('Number of Days', min_value=1, max_value=30)
    ih = st.multiselect("Interest", ["Temple", "Music", "Architecture", "Party", "Adventure", "Sports"])

    if st.button('Generate Trip Plan'):
        with st.spinner('Generating trip plan...'):
            filename = generate_trip_plan(source, destination, mode, days, ih)
            st.success('Trip details have been generated successfully!')
            st.download_button(
                label="Download Word Document",
                data=open(filename, 'rb').read(),
                file_name=filename
            )

if __name__ == "__main__":
    main()
