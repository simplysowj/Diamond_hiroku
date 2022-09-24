

import streamlit as st
import numpy as np
from pickle import load
import pandas as pd


scaler=load(open('Models/standard_scaler.pkl','rb'))
regressor_rf=load(open('Models/regressor_rf.pkl','rb'))
label_color=load(open('Models/label_color.pkl','rb'))
label_clarity=load(open('Models/label_clarity.pkl','rb'))
label_cut=load(open('Models/label_cut.pkl','rb'))

def show_predict_page():
    original_title = '<p style="font-family:cursive; color:white; font-size: 60px;">Diamond Price Prediction</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    #st.title("Diamond Price Prediction")
    original_title1 = '<p style="font-family:cursive; color:white; font-size: 30px;">We need some information for price prediction</p>'
    st.markdown(original_title1, unsafe_allow_html=True)

    #st.write("""### We need some information for price prediction""")

    cut={'Ideal','Premium','Good','Very Good','Fair'}

    color = {'E','I','J','H','F','G','D'}

    clarity={'SI2','SI1','VS1','VS2','VVS2','VVS1','I1','IF'}

    cut=st.selectbox("cut",cut)
    color=st.selectbox("color",color)
    clarity=st.selectbox("clarity",clarity)

   

    carat=st.slider("carat",0.1,5.0,0.2)
    length=st.slider("length",1.0,20.0,3.95)
    width=st.slider("width",1.0,20.0,3.98)
    depth=st.slider("depth",1.0,20.0,2.43)
    depthper=st.slider("depthper",0.1,100.0,61.5)
    tableper=st.slider("tableper",0.1,100.0,55.0)


    btn_click=st.button("Predict")


    if btn_click==True:
        if carat and cut and color and clarity and length and width and depth:
            query_point=np.array([float(length),float(width),float(depth),float(carat),float(depthper),float(tableper)]).reshape(1,-1)
            query_point_transformed=scaler.transform(query_point)
            query_point_transformed=pd.DataFrame(query_point_transformed)
        
            query_point_color_encode=label_color.transform(np.array(color).reshape(-1,1))
            query_point_color_encode=pd.DataFrame(query_point_color_encode)
            query_point_clarity_encode=label_clarity.transform(np.array(clarity).reshape(-1,1))
            query_point_clarity_encode=pd.DataFrame(query_point_clarity_encode)
            query_point_cut_encode=label_cut.transform(np.array(cut).reshape(-1,1))
            query_point_cut_encode=pd.DataFrame(query_point_cut_encode)
       
            X_train_transformed = pd.concat([query_point_transformed, query_point_color_encode,query_point_clarity_encode,query_point_cut_encode], axis=1)
        
           
            pred=regressor_rf.predict(X_train_transformed)
            st.success(pred)
            st.subheader(f"The estimated Price of a Diamond is ${pred[0]}")

        else:
            st.error("Enter the correct values")
