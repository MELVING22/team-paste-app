import streamlit as st
import pandas as pd
import os
import io
from datetime import datetime

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Daily IN&OUT NG parts",
    page_icon="📊",
    layout="wide"
)

# -----------------------
# Sidebar Menu
# -----------------------
st.sidebar.title("⚙️ Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["📥 Paste Data", "📝 Edit Data", "⬇️ Download Data", "ℹ️ About"]
)

EXCEL_FILE = "team_data.xlsx"

# Load or create
if os.path.exists(EXCEL_FILE):
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.DataFrame(columns=["Line", "Description", "Issue", "In","Out","Balance"])


# -----------------------
# Paste Data Section
# -----------------------
if menu == "📥 Paste Data":
    st.title("📥 Paste New Data")
    st.info("Paste rows copied from Excel/CSV (comma or tab separated).")

    pasted = st.text_area("Paste your rows here:", height=150)

    if st.button("➕ Add Pasted Data", use_container_width=True):
        if pasted.strip():
            try:
                new_df = pd.read_csv(io.StringIO(pasted), sep=None, engine="python")
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_excel(EXCEL_FILE, index=False)
                st.success("✅ Data added successfully!")
            except Exception as e:
                st.error(f"❌ Could not parse pasted data: {e}")
        else:
            st.warning("⚠️ Nothing was pasted.")


# -----------------------
# Edit Data Section
# -----------------------
elif menu == "📝 Edit Data":
    st.title("📝 Edit Team Data")

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic"
    )

    if st.button("💾 Save Changes", use_container_width=True):
        edited_df.to_excel(EXCEL_FILE, index=False)
        st.success("✅ Changes saved successfully!")
        df = edited_df


# -----------------------
# Download Section
# -----------------------
elif menu == "⬇️ Download Data":
    st.title("⬇️ Download Current Data")
    st.info("Export the latest version of your team data as Excel.")

    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)

    st.download_button(
        "📂 Download Excel",
        data=buffer.getvalue(),
        file_name=f"team_data_{datetime.today().date()}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )


# -----------------------
# About Section
# -----------------------
elif menu == "ℹ️ About":
    st.title("ℹ️ About This App")
    st.write("""
    - 📊 Manage your daily Excel data with your team.  
    - 📥 Paste from Excel → 📝 Edit → 💾 Save → ⬇️ Download.  
    - Built with **Streamlit + Pandas**.  
    """)
    st.success("Developed for flexible team collaboration 🚀")
