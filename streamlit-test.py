import streamlit as st

# Embed Power BI Report
embed_url = "https://app.powerbi.com/reportEmbed?reportId=fe1ebbed-5307-47f7-b19f-11bd12528584&appId=46c96bf7-44b5-41cc-b302-803d7541d923&autoAuth=true&ctid=4ae48b41-0137-4599-8661-fc641fe77bea"
st.markdown(f'<iframe title="ProControl+" width="2000" height="900" src="https://app.powerbi.com/reportEmbed?reportId=fe1ebbed-5307-47f7-b19f-11bd12528584&appId=46c96bf7-44b5-41cc-b302-803d7541d923&autoAuth=true&ctid=4ae48b41-0137-4599-8661-fc641fe77bea" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
