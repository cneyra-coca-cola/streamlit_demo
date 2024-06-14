import streamlit as st

st.set_page_config(page_title="What's new?", page_icon="Images/coke_icon.png", layout="wide")

st.image("Images/coke_logo.png")

st.write("# Let's explore what's new in SSDP")

st.write("## Release 2.1.5 > 05/13/2024")


cols = st.columns(2)

with cols[0]:
    st.write("## Synapse Features")

    st.write("##### Customized error email messages")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** This change include more details in the notifications about pipelines executions, like errors and failed stages in the process. This will be available in our Power BI dashboard.")

    st.write("##### Log Ingestion Status")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** This change include more details in the notifications about pipelines executions, like errors and failed stages in the process. This will be available in our Power BI dashboard.")

    st.write("##### Logging and Error Handling")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** Custom log enablement to centralize the log monitoring of notebooks using Log Analytics to improve the error handling and analysis.")

    st.write("##### Ingestion Notifications")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** Enhancement implemented to lower the number of notifications received during the ingestion process, from several to one notifications.")

    st.write("##### New Serverless Data Model")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** This feature creates several databases per collection so the tables can be separated by client and by tenant in each database.")

with cols[1]:
    st.write("## API Features")

    st.write("##### Get Pipeline Run Status")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** The users of the API are now allowed to obtain the pipeline run status using this endpoint, using the run id provided in the notification email.")

    st.write("##### Get Trigger Run")
    st.write("- **Impact and severity:** This feature has no impact in the business operation, no actions needed from the consumers perspective.")
    st.write("- **Description:** The users of the API are now allowed to obtain the trigger details using the trigger name of their list of triggers.")