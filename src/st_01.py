import streamlit as st

from modules.simple_ml_models import HousePriceModel

if __name__ == '__main__':
    model = HousePriceModel()
    
    st.title("House Price Model")

    with st.form('house_price_form', clear_on_submit=True):
        n_floors = st.number_input('n_floors', 1,10, value=1)
        area = st.slider('area', 1, 250, value=10)
        heating = st.radio('heating', ('A', "B", "C", 'D'))

        submited = st.form_submit_button('Submit')
        

        if submited:
            prediction = model(n_floors=n_floors, area=area, heating=heating)
            st.write(f'House price: {prediction} $')
            description = st.text_area(label='Description', value={'n_floors': n_floors, 'area': area, 'heating': heating})
            # description.