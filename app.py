import streamlit as st
import pandas as pd


@st.cache_data
def load_data(csv):
    return pd.read_csv(csv, sep=";")


def download_data():
    return st.session_state.df.to_csv(sep=";", index=False)


def next_item(col="text", init=False):
    if not init:
        st.session_state.df.loc[st.session_state.row_index, "label"] = st.session_state.radio_choice
    
    empty_label_rows = st.session_state.df[st.session_state.df["label"].isna()]
    
    if empty_label_rows.shape[0] == 0:
        st.info(
            "All data are labelled! Consider downloading the CSV using 'Download CSV' in the sidebar. Cycling "
            "randomly now.")
        row = st.session_state.df.sample()
        st.session_state.row_index = int(row.index[0])
        st.session_state.row = row[[col, "label"]]
        return row[[col, "label"]]
    
    row = empty_label_rows.sample()
    st.session_state.row_index = int(row.index[0])
    st.session_state.row = row[[col, "label"]]
    return row[[col, "label"]]


def main():
    with st.sidebar:
        input_data = st.file_uploader("Upload a **CSV** file", type=["csv"])
        input_labels = st.slider("How many labels?", min_value=2, max_value=10, step=1)
        
        button_start = st.sidebar.button("Start Labelling")
    
    if button_start:
        
        df = load_data(input_data)
        if "label" not in df.columns:
            df["label"] = None
        
        st.session_state.df = df
        
        st.session_state.labels = [x for x in range(0, input_labels)]
        st.session_state.row = next_item("text", init=True)
    
    if st.session_state.get('df') is None:
        st.warning("Data not loaded yet.")
    else:
        st.write(st.session_state.row)
        st.session_state.radio_choice = st.radio("Label", options=st.session_state.labels)
        st.session_state.row["label"] = st.session_state.radio_choice
        st.session_state.df.loc[st.session_state.row_index, "label"] = st.session_state.radio_choice
        
        st.button("Next", on_click=next_item)
        
        st.sidebar.download_button("Download CSV", data=download_data(), file_name="output.csv", mime="text/csv")


if __name__ == '__main__':
    main()
