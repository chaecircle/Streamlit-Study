import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(20, 3), columns=['first', 'second', 'third'])

## plot은 write 명령어로 그려지지 않음!
# st.write(plt.plot([1, 2, 3, 4]))
# plot = plt.plot(df)
# st.write(plot)


# 양끝에 :를 붙여서 이모티콘 사용 가능!
st.write(':smile:')
st.write(':cry:')
st.write(':sunglasses:')
st.write(":moon:")