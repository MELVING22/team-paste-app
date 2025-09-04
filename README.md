# Team Data Manager (Streamlit + Excel)

A simple **web app** that lets your team:
- Paste daily data directly (from Excel or CSV)
- Edit the table collaboratively
- Save updates into an Excel file
- Download the latest Excel anytime

---

## 🚀 Run Locally

1. Install Python 3.10+  
2. Unzip this project, open a terminal here.  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```
5. Open the local URL (shown in terminal).

---

## 🌐 Deploy Free (Streamlit Cloud)

1. Push this folder to a GitHub repo (e.g., `team-paste-app`).  
2. Go to **share.streamlit.io** → New App → choose your repo → set entry point `streamlit_app.py`.  
3. Deploy. Share the app URL with your team.

---

## 🧭 How to Use

- **Paste Data**: Copy rows from Excel/CSV and paste into the text box → click *Add*.  
- **Edit Table**: Add, update, delete rows directly in the web UI.  
- **Save Changes**: Persist updates into `team_data.xlsx` (stored on server).  
- **Download**: Export the latest table as Excel anytime.

---

⚠️ Note: If multiple people edit at the same exact time, the **last save wins**.  
Tip: Add an `Updated By` and `Updated At` column to track edits.

