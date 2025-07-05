import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

# Autenticar com Google Sheets via secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("CX - Pesquisa para conhecer o avatar").sheet1
