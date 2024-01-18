import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import networkx as nx

# Streamlitアプリの設定
st.set_page_config(page_title="論理回路シミュレータ")

# アプリケーションのタイトルと説明
st.title("論理回路シミュレータ")
st.caption("Created by Dit-Lab.(Daiki Ito)")

# ヘルプテキスト
help_texts = {
    "AND": "ANDゲートは、すべての入力が1の場合にのみ1を出力します。",
    "OR": "ORゲートは、少なくとも1つの入力が1の場合に1を出力します。",
    "NOT": "NOTゲートは、単一の入力を反転させます。0は1に、1は0になります。"
}

# ゲート選択とヘルプ表示
gate = st.selectbox("論理回路を選択", ["AND", "OR", "NOT"])
if st.button('ヘルプ'):
    st.info(help_texts[gate])

# 入力値の選択
input1 = st.checkbox("入力 1 (0 または 1)", value=False)
input2 = st.checkbox("入力 2 (0 または 1)", value=False) if gate != 'NOT' else None

# 回路図の描画
def draw_logic_circuit(gate, input1, input2):
    G = nx.DiGraph()
    G.add_node("入力1", pos=(0, 1))
    if gate != 'NOT':
        G.add_node("入力2", pos=(0, 0))
    G.add_node(gate, pos=(1, 0.5))
    G.add_node("出力", pos=(2, 0.5))

    G.add_edge("入力1", gate)
    if gate != 'NOT':
        G.add_edge("入力2", gate)
    G.add_edge(gate, "出力")

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, arrows=True)

    plt.show()

draw_logic_circuit(gate, input1, input2)

# 結果の計算
result = None
if gate == 'AND':
    result = input1 and input2
elif gate == 'OR':
    result = input1 or input2
elif gate == 'NOT':
    result = not input1

# 出力の表示
st.header(f'出力（F）: {int(result)}')

# Copyright表示
st.markdown('© 2022-2023 Dit-Lab.(Daiki Ito). All Rights Reserved.')
