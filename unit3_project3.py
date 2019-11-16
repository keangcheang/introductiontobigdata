#Unit3 Individual Project 3
#Questions: 
# Which type product had the most complaints ordered by state?
# How many complaints have been filed for each company?
# Summarize the responses for each company. (i.e., 32 In Progress, 67 Closed, 22 Closed with Explanation).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Consumer_Complaints.csv")

data.head(5)
data.info()
data.columns
# #Date received', 'Product', 'Sub-product', 'Issue', 'Sub-issue','Consumer complaint narrative', 'Company public response', 'Company','State', 'ZIP code', 'Tags', 'Consumer consent provided?','Submitted via', 'Date sent to company', 'Company response to consumer','Timely response?', 'Consumer disputed?', 'Complaint ID'], dtype='object')

#change columns names
data.columns=['date_received', 'product', 'sub_product', 'issue', 'sub_issu', 'consumer_complaint_nar', 'company_pub_response', 'company', 'state', 'zip_code', 'tags', 'consumer_consent_provided', 'submitted_via', 'date_sent_to_com', 'com_response_to_consumer', 'timely_response', 'consumer_dis', 'complaint_id']

product_group= data.groupby(["state", "product"]).count()
product_group = product_group.sort_values(["state", "issue"], ascending=[True, False])
product_groupcsv = pd.DataFrame(product_group)
product_groupcsv.to_csv("product.csv", index=True)
#Q1: The product that had the most complaints sorted by the state are listed below: 
product_groupcsv.head(30)

data.groupby('product').size().plot.pie(figsize=[15,15], title='Pie Graph by Products', autopct='%1.1f%%')


company_group = data.groupby('company').count()
company_group= company_group.sort_values('company', ascending=True)
company_groupcsv = pd.DataFrame(company_group)
company_groupcsv.to_csv("company.csv", index=True)
#Q2: Complaints filed by each company: 
company_groupcsv.head(30)['issue']

response_group = data.groupby(['company', "com_response_to_consumer"]).count()
response_groupcsv = pd.DataFrame(response_group)
response_groupcsv.to_csv('response.csv', index=True)
#Q3: The response by each company: 
response_groupcsv.head(30)['issue']





