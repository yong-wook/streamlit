# 라이브러리
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
# 데이터 전처리
df = pd.read_csv('life_expectancy_years.csv', index_col = 0)
df_korea = df.loc['South Korea']
meanlife = np.round(np.mean(df_korea))
years = pd.to_numeric(df_korea.index)
# Streamlit component, layout 구성
st.title('🇰🇷 Life expectancy of Korea') 
st.line_chart(df_korea)
# slider input을 통한 숫자 입력
number = st.slider(label = '연도를 선택하세요', min_value = int(np.min(years)), max_value = int(np.max(years)), step = 1)
number2 = int(df_korea.loc[[str(number)]])
# Metric
col1, col2 = st.columns(2)
with col1:   st.metric(label = 'Mean Life expectancy: All time', value = meanlife)
with col2:   st.metric(label = 'Life expectancy of selected year', value = number2, delta = number2 - meanlife)