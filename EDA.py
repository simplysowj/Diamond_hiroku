import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

@st.cache
def load_data():


    df = pd.read_csv('diamonds.csv')
    df.rename(columns={"x": "length", "y": "width", "z" : "depth","depth" : "depth %", "table": "table %"},inplace = True)
    df['L/W'] = df['length']/df['width']
    df[['length','width','depth','L/W']]=df[['length','width','depth','L/W']].replace(0,np.NaN)
    df.dropna(inplace=True)
    return df

df=load_data()

def show_explore_page():

    st.title("Explore Diamond Dataset")
    
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(y='price',data=df,x='color',palette ='Set1',width =0.3,order = ['D','E','F','G','H','I','J'] )
    st.pyplot(fig)

    st.write("""### From the above plot, we can see that G, H, I and J type color has less number of outliers compared to D and E""")
    
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(y='price',data=df,x='cut',palette ='Set1', width =0.5,order =['Ideal' ,'Premium' ,'Very Good' ,'Good' ,'Fair'] )
    st.pyplot(fig)

    st.write("""### From the above plot, we can see that the lower the quality of cut, the higher the number of outliers except for the Ideal cut type. Also, each category type has the same maximum and minimum price.""")
    
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(y='price',data=df,x='clarity',palette ='Set1', width =0.7,linewidth=3,order =['IF','VVS1','VVS2','VS1','VS2','SI1','SI2','I1'])
    st.pyplot(fig)

    st.write("""### we can see that IF, VVS1 and VVS2 have a high number of outliers compared to other categories of color. Moreover VS1,VS2 are having less number of outliers compared to others.Also, each category type has the same maximum and minimum price.""")

    fig = plt.figure(figsize=(10, 4))
    corr = df.corr()
    sns.heatmap(data=corr, square=True , annot=True, cbar=True)
    st.pyplot(fig)

    st.title("CONCLUSIONS :")
    st.subheader("1. Depth is inversely related to Price.")

    st.write("""### This is because if a Diamond's Depth percentage is too large or small the Diamond will become 'Dark' in appearance because it will no longer return an Attractive amount of light.""")

    st.subheader("2. The Price of the Diamond is highly correlated to Carat, and its Dimensions.")
    st.subheader("3. The Weight (Carat) of a diamond has the most significant impact on its Price.")
    st.write("""### Since, the larger a stone is, the Rarer it is, one 2 carat diamond will be more 'Expensive' than the total cost of two 1 Carat Diamonds of the same Quality.""")
    st.subheader("4. The Length(x) , Width(y) and Height(z) seems to be higly related to Price and even each other.")

    from PIL import Image
    st.title("CUT : ")
    image = Image.open('cut.png')
    st.image(image, caption='Cut')
    st.title("Cut Vs Price")
    
    image = Image.open('cutvsprice.png')

    st.image(image, caption='Cut Vs Price')
    st.write("""### Premium Cut on Diamonds as we can see are the most Expensive, followed by Excellent / Very Good Cut.    """)

    st.title("COLOR : ")
    image = Image.open('color.png')
    st.image(image, caption='color')

    st.title("Color Vs Price : ")
    image = Image.open('colorvsprice.png')
    st.image(image, caption='color vs price')

    st.title("Clarity : ")
    image = Image.open('clarity.png')
    st.image(image, caption='Clarity')

    st.title("clarity vs Price : ")
    image = Image.open('clarityvsprice.png')
    st.image(image, caption='clarity vs price')
    st.write("""### It seems that VS1 and VS2 affect the Diamond's Price equally having quite high Price margin.""")

    st.title("clarity : ")
    image = Image.open('claritycolor.png')
    st.image(image, caption='clarity')
    st.write("""###We can see that from above that most of the people prefer G color followed by E, F, and H.In that the clarity they mostly prefer SI1 or SI2 category.Therefore from above all the plots, we can conclude that carat has high importance followed by cut, color, and clarity in predicting the price of a diamond.""")