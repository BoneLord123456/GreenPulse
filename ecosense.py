import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000,key="datarefresh")

SHEET_URL = "https://docs.google.com/spreadsheets/d/1OE7X1_M6obW9You92p-wm33jmNnUbhEZwyUdXSvstIk/export?format=csv"
df = pd.read_csv(SHEET_URL)
st.title("GreenPulse Dashboard")
latest = df.iloc[-1]





st.subheader("Current Status")
st.write("Status:", latest["Status"])
st.write("Recommended Action:", latest["Recommended Action"]) 




col1,col2=st.columns(2)
with col1:
    st.subheader("Noise Intensity Level: ")
    st.metric(label="Current",value=df["NoiseIntensityLevel"].tail(1).iloc[-1])
with col2:
    fig1, ax1 = plt.subplots()
    #ax1.plot(df["NoiseIntensityLevel"])
    ax1.plot(df["Time"].tail(8),df["NoiseIntensityLevel"].tail(8),color="blue",linestyle='solid',linewidth=2,marker="D",markersize=3,label='NoiseIntensityLevel')   
    plt.title("NoiseIntensityLevel vs Time")
    plt.xlabel("Time")
    plt.ylabel("NoiseIntensityLevel")
    plt.legend(loc="upper right")
    plt.grid()
    st.pyplot(plt)



col1,col2=st.columns(2)
with col1:
    st.subheader("Surface Condition Score")
    st.metric(label="Current",value=df["SurfaceConditionScore"].tail(1).iloc[-1])
with col2:
    fig2, ax2 = plt.subplots()
    ax2.plot(df["Time"].tail(8),df["SurfaceConditionScore"].tail(8),color="brown",linestyle='solid',linewidth=2,marker="D",markersize=3,label='SurfaceConditionScore')     
    plt.title("SurfaceConditiionScore vs Time")
    plt.xlabel("Time")
    plt.ylabel("SurfaceConditiionScore")
    plt.legend(loc="upper right")
    plt.grid()
    st.pyplot(plt)




col1,col2=st.columns(2)
with col1:
    st.subheader("Eco Metric Score (EMS)")
    st.metric(label="Current",value=df["EMS"].tail(1).iloc[-1])
with col2:
    fig3, ax3 = plt.subplots()
    ax3.plot(df["Time"].tail(8),df["EMS"].tail(8),color="green",linestyle='solid',linewidth=2,marker="D",markersize=3,label='Eco Matrix Score')     
    plt.title("Eco Matrix Score vs Time")
    plt.xlabel("Time")
    plt.ylabel("Eco Matrix Score")
    plt.legend(loc="upper right")
    plt.grid()
    st.pyplot(plt)