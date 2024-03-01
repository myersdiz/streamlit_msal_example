import streamlit as st
from streamlit_msal import Msal
import os
import platform

st.write(platform.system())

try:
    client_id = os.getenv("AZURE_CLIENT_ID")
except:
    st.write("Please set the environment variable AZURE_CLIENT_ID")
    st.stop()

try:
    authority = "https://login.microsoftonline.com/" + os.getenv("AZURE_TENANT_ID")
except:
    st.write("Please set the environment variable AZURE_TENANT_ID")
    st.stop()

with st.sidebar:
    auth_data = Msal.initialize_ui(
        client_id=client_id,
        authority=authority,
        scopes=[], # Optional
        # Customize (Default values):
        connecting_label="Connecting",
        disconnected_label="Disconnected",
        sign_in_label="Sign in",
        sign_out_label="Sign out"
    )

if not auth_data:
    st.write("Authenticate to access protected content")
    st.stop()

if st.sidebar.button("Revalidate"):
    Msal.revalidate() # Usefull to refresh "accessToken"

access_token = auth_data["accessToken"]

account = auth_data["account"]
name = account["name"]
username = account["username"]
account_id = account["localAccountId"]

st.sidebar.write(f"Hello {name}!")
st.sidebar.write(f"Your username is: {username}")
st.sidebar.write(f"Your account id is: {account_id}")
st.sidebar.write("Your access token is:")
st.sidebar.code(access_token)

st.image("https://www.thewordfinder.com/wof-puzzle-generator/puzzle.php?bg=1&ln1=&ln2=JULIE ANDREWS&ln3=AS MARY&ln4=POPPINS&cat=ACTOR AND ROLE&")

st.write("Auth data:")
st.json(auth_data)