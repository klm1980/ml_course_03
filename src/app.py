import streamlit as st
import pandas as pd
import numpy as np

if __name__ == "__main__":
    st.title('Experiments')
    st.text('Table 1')
    df2 = pd.DataFrame(np.random.randn(15, 13), columns=(f'col_{i}' for i in range(13)))
    df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6]})
    st.dataframe(df)
    st.text('Table 1')
    st.dataframe(df2)