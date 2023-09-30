import streamlit as st
from text_hanlder import text_from_html

text = None

st.title('How long will take you to read an article?')

with st.sidebar:
    choice = st.radio(
        'Choose the way you want to measure reading time',
        ('URL', 'Manual Text')
    )
if choice == 'URL':
    # getting the url
    url = st.text_input('Enter a URL for an article, that you want to know how long will take you to read')
    
    
        
elif choice == 'Manual Text':
    text = st.text_area('Paste the text here or write it manualy')
    

# counting the number of time spend on the url
if st.button('Count the time'):
    if choice == 'URL':
        if url is not '':
            try:
                text = text_from_html(str(url))
            except:
                st.write('Please provide a valid URL')

    if text is not None:
        length = len(text.split())
        amount = int(length) // 200
        st.write(f'You will spend aproxemtly {amount} mintues to read the text')
    else:
        st.write('Please provide a valid URL')