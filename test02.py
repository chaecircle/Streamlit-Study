import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

################ st.write() 사용 #################

# df = pd.DataFrame(np.random.randn(10, 3), columns=['first', 'second', 'third'])

# plot은 write 명령어로 그려지지 않음!
# st.write(plt.plot([1, 2, 3, 4]))
# plot = plt.plot(df)
# st.write(plot)


# 양끝에 :를 붙여서 이모티콘 사용 가능!
st.write(':smile:')
st.write(':cry:')
st.write(':sunglasses:')
st.write(":moon:")



############ streamlit의 layout 살펴보기 #############

# 사이드바 옵션
st.sidebar.selectbox(
    'Select category.'
    ('Main Home', 'Category 1', 'Category 2')
)






