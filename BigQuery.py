#pip install --upgrade google-cloud-bigquery
#pip install pandas-gbq
#Create new environment variable called GOOGLE_APPLICATION_CREDENTIALS and set its path to JSON file with prvate key. gbq is reading this to authenticate
from google.cloud import bigquery

from pandas.io import gbq
from scipy.stats import linregress
import pandas as pd
import sklearn.preprocessing as pp
import numpy as np


Query = "select Original_Retailer_Name, Competitor_Retailer_Name, Times_Together \
from a_temp.DSS_Competitor_Set_Spend Where Times_Together >= 1000"
df = gbq.read_gbq(query=Query, project_id="studied-radar-148816")
print(df)


Satisfaction = ['Product_Specific_CPM_quality','Product_Specific_CPM_durability','Product_Specific_CPM_range_of_colours','Product_Specific_CPM_range_of_styles','Product_Specific_CPM_ease_of_care','Product_Specific_CPM_offers_in_size_body_shape','Product_Specific_CPM_comfort','Product_Specific_CPM_stylish_on_trend','Product_Specific_CPM_suit_my_style','Product_Specific_CPM_ethical_position','Service_CPM_how_clean_tidy_store','Service_CPM_how_long_to_pay_queue','Service_CPM_how_busy_store','Service_CPM_availability_condition_fitting_rooms','Service_CPM_availability_items_in_stock_your_size','Service_CPM_how_easy_to_navigate_find_items_in_store','Service_CPM_helpfulness_knowledge_staff','Service_CPM_return_refund_policy','Service_CPM_convenience_store_location','Service_CPM_product_reviews','Service_CPM_images_videos_of_products','Service_CPM_text_description_of_products','Service_CPM_personalized_customer_service','Service_CPM_delivery_options','Service_CPM_shipping_cost_speed','Service_CPM_how_easy_to_navigate_find_items_on_website','Service_CPM_checkout_process_payment_options','Service_CPM_products_resembled_expectations','Prices_CPM_overall_prices_at_retailer','Prices_CPM_prices_at_cheaper_end_of_retailers_range','Prices_CPM_prices_at_premium_end_of_retailers_range','Prices_CPM_number_of_reduced_price_products_available','Prices_CPM_number_of_special_offers_and_discounts_offered','Prices_CPM_offers_targeted_directly_to_you','Prices_CPM_regular_price_of_products_not_on_sale','Prices_CPM_range_of_prices_of_products_budget_treat','Prices_CPM_sales_discounts_promotions_on_products']
Demand_Usage = ['Purchase_frequency_instore','Purchase_frequency_online','Purchase_frequency_overall','Instore_spend','Online_spend','Overall_spend']

#Query = "select * \
#from a_temp.DSS_Brand_Satisfaction"
Query = "select * \
from a_temp.DSS_Brand_Satisfaction_UK where Retailer in (3,4,22,24,30,56,63,74,75,76,78,87,89,93,116,225)"
df = gbq.read_gbq(query=Query, project_id="studied-radar-148816")
#scaler = pp.MinMaxScaler(feature_range=(0,10))
df = df[Satisfaction + Demand_Usage]
columns = {'Relationship','slope', 'intercept', 'r_value', 'p_value', 'std_err'}
reg_output_df = pd.DataFrame(columns=columns)

row = 0
for metric in range(0,len(Demand_Usage)):
    for column in range(0,len(Satisfaction)):
        qstr = Demand_Usage[metric] + " >= 0 & " + Satisfaction[column] + " >= 0"
        tf = df.query(qstr)
        column_pair = [Demand_Usage[metric], Satisfaction[column]]
        tf = tf[column_pair]
        tf = tf.apply(pd.to_numeric)
        #tf = scaler.fit_transform(tf)
        print(Demand_Usage[metric] + " and " + Satisfaction[column])
        slope, intercept, r_value, p_value, std_err = linregress(tf[Demand_Usage[metric]],tf[Satisfaction[column]])

        reg_output_df.loc[row, 'Relationship'] = Demand_Usage[metric] + " and " + Satisfaction[column]
        reg_output_df.loc[row, 'slope'] = slope
        reg_output_df.loc[row, 'intercept'] = intercept
        reg_output_df.loc[row, 'r_value'] = r_value
        reg_output_df.loc[row, 'p_value'] = p_value
        reg_output_df.loc[row, 'std_err'] = std_err
        row = row + 1
        print(linregress(tf[Demand_Usage[metric]],tf[Satisfaction[column]]))

reg_output_df.to_excel("reg_output_demand_and_satisfaction_drivers.xlsx")




