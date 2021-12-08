import streamlit as st

from modules.simple_ml_models import SantimentModel

@st.cache
def load_model():
    print("Load model ...")
    return SantimentModel()

if __name__ == '__main__':
    model = SantimentModel()
    maping = {
        1: 'positive',
        -1: 'negative',
        0: 'neutral'
    }
    
    st.title("Santiment Model")

    with st.form('santiment form'):
        text = st.text_area('Text to analyze')

        submited = st.form_submit_button('Submit')
        if submited:
            prediction = model(text=text)
            label = maping[prediction]
            st.write(f'Santiment: {label}')
            if prediction == 1:
                st.balloons()