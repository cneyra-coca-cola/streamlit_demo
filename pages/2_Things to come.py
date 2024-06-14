import streamlit as st

st.set_page_config(page_title="Things to come", page_icon="Images/coke_icon.png", layout="wide")

st.image("Images/coke_logo.png")
st.write("# Let's explore what's coming in SSDP")
st.write("## Release 2.1.6")

st.divider()

cols = st.columns(2)

with cols[0]:
    st.write("## Synapse Features")

    st.write("##### Changed data quality parquet table to a delta table")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** This feature will allow us to store the data quality data in Delta Tables with z-order on the date column to optimize the query time, improving the data quality report capabilities.")

    st.write("##### Onboarding logging and change tracking")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** This feature will allow us to integrate the custom logging into the onboarding pipelines and capture changes in metadata with logging, also create audit tables in Log Analytics to track changes in metadata.")

    st.write("##### Notification onboarding pipeline")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** This enhancement will allow us to send notification mails in case one of the steps in the onboarding process fails, so the audit user can receive the error information (code and failed activities) to give a faster solution.")
with cols[1]:
    st.write("## API Features")
    st.write("For this release we don't have any planned release from the API perspective.")

