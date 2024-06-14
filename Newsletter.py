import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SSDP Newsletter", page_icon="Images/coke_icon.png", layout="wide")



date_col = st.columns(3)
with date_col[0]:
    st.image("Images/coke_logo.png")

with date_col[1]:
    st.write("# SSDP Newsletter")
with date_col[2]:
    st.write("## 06/14/2024")

st.write("Hello! Welcome to the SSDP newsletter. Join us to discover what's new at SSDP and upcoming features! We are "
         "happy to share with you all our progress, please if you have any questions do not hesitate to contact us, "
         "we will be more than happy to answer your questions, we hope you enjoy this space!")

cols = st.columns(2)
with cols[0]:
    st.write("## 2024 Data Engineering Trends")
    st.image("Images/data_image.jpg")

    st.write("#### Data Engineering and Architecture")
    st.write("As we embrace 2024, the proficiency in data engineering and architecture stands paramount for Azure Data "
             "Engineers. Mastery in designing robust, scalable, and secure data solutions on Azure is essential. This "
             "includes understanding Azure's data services ecosystem, such as Azure Data Lake, Azure Synapse Analytics, "
             "and Azure Databricks. Data Engineers must architect solutions that can handle the volume, velocity, and "
             "variety of data, ensuring performance and compliance. The ability to build and maintain a data architecture "
             "that supports both real-time and batch processing will be a defining factor in the success of data-driven organizations.")

    st.write("#### DevOps and Automation")
    st.write("Embracing DevOps practices and automation is crucial for Azure Data Engineers in 2024. The skill to "
             "implement continuous integration and delivery (CI/CD) pipelines for data solutions ensures faster deployment "
             "and higher quality. Familiarity with tools like Azure DevOps, GitHub Actions, and Terraform for infrastructure "
             "as code (IaC) will be important. Data Engineers who can automate workflows and streamline the data lifecycle "
             "will enhance agility and enable businesses to respond swiftly to market demands.")

    st.write("#### Real-time Data Processing and Streaming")
    st.write("The capability to process and analyze data in real-time is a highly sought-after skill for Azure Data "
             "Engineers in 2024. With the rise of IoT and the need for immediate insights, expertise in technologies "
             "like Azure Stream Analytics and Apache Kafka is essential. Data Engineers must build systems that can "
             "ingest, process, and analyze streaming data with low latency. Those who can harness real-time data streams "
             "will empower organizations to make quicker, more informed decisions.")

with cols[1]:
    st.write("#### Collaboration and Communication")
    st.write("Strong collaboration and communication skills are indispensable for Azure Data Engineers as they work in "
             "cross-functional teams and interact with stakeholders. The ability to translate technical details into "
             "business language and vice versa ensures that data solutions align with organizational goals. Data Engineers "
             "must effectively collaborate with data scientists, business analysts, and IT teams to deliver cohesive "
             "data strategies. Those who excel in communication will bridge the gap between complex data technologies "
             "and business needs, driving successful outcomes.")

    st.write("## What Skills Does a Azure Data Engineer Need?")
    st.image("Images/data_engineer.jpg")

    st.write("#### Cloud Computing and Azure Services Proficiency")
    st.write("A deep understanding of cloud computing concepts and hands-on experience with Azure services form the "
             "backbone of an Azure Data Engineer's skill set. This includes expertise in Azure storage solutions like "
             "Azure Blob Storage and Azure Data Lake, as well as data processing services such as Azure Data Factory, "
             "Azure Databricks, and Azure Synapse Analytics. Proficiency in these areas allows data engineers to build "
             "and maintain scalable data architectures within the Azure cloud environment.")

    st.write("#### Data Integration and ETL Processes")
    st.write("The ability to integrate data from various sources and construct robust ETL (Extract, Transform, Load) "
             "pipelines is crucial. Azure Data Engineers should be skilled in developing ETL processes that cleanse, "
             "transform, and load data into data stores, making it ready for analysis. Familiarity with Azure Data Factory, "
             "SSIS, and event-driven architectures using Azure Event Hubs or Azure Stream Analytics is important for "
             "enabling real-time data processing and insights.")

