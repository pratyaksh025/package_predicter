import streamlit as st
import joblib

model=joblib.load('placement.pkl')

def main():
    st.title("Predictive Model")
    cgpa=st.slider("Enter CGPA", min_value=0.0, max_value=10.0)
    
    if st.button('Sumit'):
        result=model.predict([[cgpa]])
        
        formatted_package = f"{result[0][0]:.2f}"

        st.success(f'Your package will be {formatted_package} LPA')



if __name__=="__main__":
    main()

