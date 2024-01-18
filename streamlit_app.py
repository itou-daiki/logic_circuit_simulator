import streamlit as st
from PIL import Image

# アプリケーションのタイトルを設定
st.title("論理回路シミュレータ")

# 論理ゲートの選択
gate = st.selectbox("論理回路を選択", ["AND", "OR", "NOT"])

# 入力値の選択
input1 = st.checkbox("入力 1 (0 または 1)", value=False)
input2 = st.checkbox("入力 2 (0 または 1)", value=False) if gate != 'NOT' else None

# 結果の計算と画像の表示
if st.button("計算"):
    if gate == 'AND':
        if not input1 and not input2:
            image = Image.open('/Image/AND00.png')
            result = False
        elif not input1 and input2:
            image = Image.open('/Image/AND01.png')
            result = False
        elif input1 and not input2:
            image = Image.open('/Image/AND10.png')
            result = False
        elif input1 and input2:
            image = Image.open('/Image/AND11.png')
            result = True
    elif gate == 'OR':
        if not input1 and not input2:
            image = Image.open('/Image/OR00.png')
            result = False
        elif not input1 and input2:
            image = Image.open('/Image/OR01.png')
            result = True
        elif input1 and not input2:
            image = Image.open('/Image/OR10.png')
            result = True
        elif input1 and input2:
            image = Image.open('/Image/OR11.png')
            result = True
    elif gate == 'NOT':
        if not input1:
            image = Image.open('/Image/NOT0.png')
            result = True
        else:
            image = Image.open('/Image/NOT1.png')
            result = False

    # 画像と計算結果の表示
    st.image(image, caption=f'{gate} gate with input {input1} {"and " + str(input2) if gate != "NOT" else ""}')
    st.write(f'出力: {int(result)}')
