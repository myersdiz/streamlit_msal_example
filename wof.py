import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers
from streamlit_javascript import st_javascript

headers = _get_websocket_headers()
access_token = headers.get("X-Access-Token")
st.write(headers)

st.write(st.experimental_user.email)

def read_aad_username():
    js_code = """(await fetch("/.auth/me")
                    .then(function(response) {return response.json();}).then(function(body) {return body;}))"""

    return_value = st_javascript(js_code)

    username = None
    if return_value == 0:
        pass # this is the result before the actual value is returned 
    elif isinstance(return_value, list) and len(return_value) > 0:
        username = return_value[0]["user_id"]
        st.write(f"Logged in as {username}")
    else:
        st.warning(f"could not directly read username from azure active directory: {return_value}.")
        st.warning(f"A workaround to this is to clear your browser cookies for this site and reloading it.")
    return username

st.write(read_aad_username())

st.image("https://www.thewordfinder.com/wof-puzzle-generator/puzzle.php?bg=1&ln1=Streamlit&ln2=Wheel of&ln3=Fortune&ln4=&cat=SHOW TITLE&")