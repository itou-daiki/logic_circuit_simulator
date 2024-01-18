import streamlit as st
import SchemDraw as schem
import SchemDraw.elements as e

# Streamlitアプリの設定
st.set_page_config(page_title="論理回路シミュレータ")

# アプリケーションのタイトルと説明
st.title("論理回路シミュレータ")
st.caption("Created by Dit-Lab.(Daiki Ito)")

# ゲート選択
gate = st.selectbox("論理回路を選択", ["AND", "OR", "NOT"])

# 回路図の描画
d = schem.Drawing()

if gate == "AND":
    g = d.add(e.AND2)
elif gate == "OR":
    g = d.add(e.OR2)
elif gate == "NOT":
    g = d.add(e.NOT)

d.add(e.LINE, to=g.in1)
d.add(e.LINE, to=g.in2)
d.add(e.LINE, to=g.out)

# SchemDrawは直接Streamlitに組み込めないため、一旦画像として保存し、それを読み込む
circuit_image = d.draw()  # 描画を実行
circuit_image_filename = 'circuit_image.png'
circuit_image.save(circuit_image_filename)
st.image(circuit_image_filename)

# Copyright表示
st.markdown('© 2022-2023 Dit-Lab.(Daiki Ito). All Rights Reserved.')
