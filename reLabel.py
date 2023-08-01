import pandas as pd

# ask user to input the file path information
FOLDER_NAME = input("please put the excel files into the same folder and then copy the file path") + "/"

# other related files and standard infomation
MERCHANT_INFO_NEW = 'merchant information.xlsx'
STANDARD_CATEGORY = ["Entertainment","Food & Beverage","Hotel/Resort","Others","Shopping","Transportation"]
STANDARD_CATEGORY_DETAIL = ["Amusement","Attractions","Travel agency","Convenient store","Dinning","Hotel/Resort","Logistics","Grocery/Supermarket",
"Others","University","Airport","Brand store","Cosmetics","Department store","Discount store/Group tour store","Duty free","Luxury store",
"Souvenir store","Specialties","Drugs/Health care","Beauty Clinic","Telecom","Shopping mall","Outlets","Transportation"]


# names of the excel fils
original_file = FOLDER_NAME + "NA_Chinese users.xlsx"
merchant_file_to_be_update = FOLDER_NAME + MERCHANT_INFO_NEW


def main():
    # import the file from downloaded files
    df1 = pd.read_excel(original_file)
    # import the file with the correct information and then update the above excel
    matching_file = FOLDER_NAME +'excel with the right info.xlsx'
    df2 = pd.read_excel(matching_file)

    #combine pid+mid+sid to add new column PMS
    fuction_explanation("the computer is combining pid with mid and sid ")
    add_PMS_change_type(df1)
    fuction_explanation("Done, move on to the next step")

    # update categoryfuction_explanationfuction_explanation in df1 and replace it with the corresponding category_detail_new in df2
    fuction_explanation("update the company information")
    update_info(df1, df2, 'PMS', 'brand', 'brand_New')
    fuction_explanation("update the category infor")
    update_info(df1, df2, 'PMS', 'category', 'category_New')
    fuction_explanation("update the category detail infor")
    update_info(df1, df2, 'PMS', 'category_detail', 'category_detail_New')


    # print the major infor
    fuction_explanation("here are the description of the file")
    print(df1.info())
    df1.describe()

    # Create pivot table using pandas
    pivot_table = pd.pivot_table(df1, values='TPV', index=['category','category_detail'], columns=['DATE'], aggfunc=sum, margins=True)
    # Format the numbers in the pivot table
    pd.options.display.float_format = '{:,.2f}'.format
    # Print the pivot table
    fuction_explanation("all the info are updated, here is the summary of the data, you can check whether it is right")    
    print(pivot_table)

    # export to an excel file
    fuction_explanation("begin to export the updated data")
    df1.to_excel(FOLDER_NAME + "FileUpdated_2023.xlsx")    



def check_wrong_label(df):
    for index, row in df.iterrows():
        if df.loc[index]['category'] not in STANDARD_CATEGORY:
            print("Attention, there are mistakes in",index + 1,"and the wrong value are:",row['category'])
        if df.loc[index]['category_detail'] not in STANDARD_CATEGORY_DETAIL:
            print("Attention, there are mistakes in",index + 1,"and the wrong value are:",row['category_detail'])
               

def fuction_explanation(comments):
    print("------------------------------------------------")
    print(comments)
    print("Working on it, will let you know once I finish your task.")

def replace_wrong_value(df,column,wrong_value, new_value):
    # Find and replace text in a specific column
    df[column] = df[column].str.replace(wrong_value, new_value)


# Add a new column to the DataFrame
# Change the data type of a column to string
def add_PMS_change_type(df):
    df['partner_id'] = df['partner_id'].astype(str)
    df['sec_merchant_id'] = df['sec_merchant_id'].astype(str)
    df['store_id'] = df['store_id'].astype(str)
    df['PMS'] = df['partner_id'] + df['sec_merchant_id'] + df['store_id']
    df['PMS'] = df['PMS'].astype(str)
    return df

def update_info(df1, df2, index_column, column_to_be_replaced, new_column):
    # Loop through the PMS values in df1
    print("Begining to update", column_to_be_replaced,"............")
    for pms in df1[index_column]:
        # Get row(s) from df2 that match the PMS
        df2_rows = df2[df2[index_column] == pms]
        # If a match is found, update the category column in df1 
        if not df2_rows.empty:
            # Get the new category value
            new_cat = df2_rows[new_column].values[0]
            # Update the category column 
            df1.loc[df1[index_column] == pms, column_to_be_replaced] = new_cat



if __name__ == "__main__":
    main()
