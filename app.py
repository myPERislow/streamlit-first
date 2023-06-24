import streamlit as st

check = st.checkbox("チェックボックス")

if check:
    st.button("ボタン")
    st.selectbox("メニューリスト", ("選択肢1","選択肢2","選択肢3"))
    st.multiselect("メニューリスト（複数選択可）", ("選択肢1","選択肢2","選択肢3"))
    st.radio("ラジオボタン", ("選択肢1","選択肢2","選択肢3"))
    st.text_input("テキスト入力")
    st.text_area("テキストエリア")
    # 以下にサイドバーを表示

st.sidebar.button("文字入力欄")
st.sidebar.text_area("テキストエリア")