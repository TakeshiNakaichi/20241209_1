import streamlit as st


# カスタム幅のカラムを作成
col1, col2, col3 = st.columns([3, 1, 1])
 
with col1:
    st.header("12カラム 1 (幅3)")
    st.write("こちらはカラム1の内容です。")
    st.video('2022-06-15T05.45.03UTC.mp4')

 
with col2:
    st.header("カラム 2 (幅1)")
    st.write("こちらはカラム2の内容です。")
    st.video('2022-06-15T05.45.03UTC.mp4')

 
with col3:
    st.header("カラム 3 (幅1)")
    st.write("こちらはカラム3の内容です。")

#title = "Test2"



#st.title(title)

print('Hello, World!!!!!!!!!!!!!')
