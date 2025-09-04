import streamlit as st
import pandas as pd
import os
import io

st.set_page_config(page_title="Team Data Manager", layout="wide")
st.title("📊 Team Data Manager")

EXCEL_FILE = "team_data.xlsx"

# Load existing data or create empty
if os.path.exists(EXCEL_FILE):
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.DataFrame(columns=["Date", "Item", "Quantity", "Notes"])

# --- Paste Data ---
st.subheader("Paste new data (CSV/Excel style)")
pasted = st.text_area("Paste rows here (comma-separated or tab-separated)", height=150)

if st.button("📥 Add Pasted Data"):
    if pasted.strip():
        try:
            new_df = pd.read_csv(io.StringIO(pasted), sep=None, engine="python")
            df = pd.concat([df, new_df], ignore_index=True)
            df.to_excel(EXCEL_FILE, index=False)
            st.success("Pasted data added successfully!")
        except Exception as e:
            st.error(f"Could not parse pasted data: {e}")

# --- Edit Table ---
st.subheader("Edit Data")
edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")

if st.button("💾 Save Changes"):
    edited_df.to_excel(EXCEL_FILE, index=False)
    st.success("All changes saved.")
    df = edited_df

# --- Download ---
st.subheader("Download Current Data")
buffer = io.BytesIO()
df.to_excel(buffer, index=False)
st.download_button(
    "⬇️ Download Excel",
    data=buffer.getvalue(),
    file_name="team_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
