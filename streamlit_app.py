import streamlit as st

def calculate_logic_gate(gate, input1, input2=None):
    if gate == 'AND':
        return input1 and input2
    elif gate == 'OR':
        return input1 or input2
    elif gate == 'NOT':
        return not input1
    elif gate == 'NAND':
        return not (input1 and input2)
    elif gate == 'NOR':
        return not (input1 or input2)
    elif gate == 'XOR':
        return input1 != input2
    elif gate == 'XNOR':
        return input1 == input2

def main():
    st.title("論理回路シミュレータ")

    if 'step' not in st.session_state:
        st.session_state.step = 0

    gate = st.selectbox("論理回路を選択", ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"])

    input1 = st.checkbox("入力 1 (0 または 1)", value=False)
    input2 = st.checkbox("入力 2 (0 または 1)", value=False) if gate != 'NOT' else None

    if st.button("進む"):
        if st.session_state.step < 2:
            st.session_state.step += 1

    if st.button("戻る"):
        if st.session_state.step > 0:
            st.session_state.step -= 1

    if st.session_state.step == 0:
        st.write("入力を設定してください。")
    elif st.session_state.step == 1:
        st.write(f"選択した論理回路: {gate}")
        st.write(f"入力値: {input1}, {input2 if gate != 'NOT' else 'N/A'}")
    elif st.session_state.step == 2:
        result = calculate_logic_gate(gate, input1, input2)
        st.write(f"計算結果: {int(result)}")

if __name__ == "__main__":
    main()
