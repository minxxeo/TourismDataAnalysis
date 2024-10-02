import pandas as pd
import os
import chardet
from sklearn.preprocessing import StandardScaler

# Define the file paths
file_paths = [
    "C:/Users/lms26/TourismDataCompetition/창원시_방문자 수(연인원) 추이.csv",
    "C:/Users/lms26/TourismDataCompetition/밀양시_방문자 수(연인원) 추이.csv",
    "C:/Users/lms26/TourismDataCompetition/진주시_방문자 수(연인원) 추이.csv",
]

# Load the GRDP data
grdp_file_path = "C:/Users/lms26/TourismDataCompetition/★2021년기준시군별지역내총생산(GRDP)추계결과.xlsx"
grdp_data = pd.read_excel(grdp_file_path)

# Extract relevant columns and filter for the required regions
regions = ['창원시', '진주시', '밀양시']
filtered_grdp_data = grdp_data[grdp_data['구분'].isin(regions)][['구분', 'Unnamed: 7']]
filtered_grdp_data.columns = ['지역', '지역내총생산(명목가격)']  # Rename columns for consistency

# Save the filtered GRDP data to a new CSV file
filtered_grdp_csv_path = "C:/Users/lms26/TourismDataCompetition/2021_1인당_GRDP_창원시_진주시_밀양시.csv"
filtered_grdp_data.to_csv(filtered_grdp_csv_path, index=False, encoding='utf-8-sig')

# Load the visitor data
visitor_data_file_path = "C:/Users/lms26/TourismDataCompetition/2023_지역별_총방문자수.csv"
visitor_data = pd.read_csv(visitor_data_file_path, encoding='utf-8-sig')

# Merge the GRDP data with the visitor data
merged_data = pd.merge(filtered_grdp_data, visitor_data, on='지역')

# Normalize the GRDP and visitor count columns
scaler = StandardScaler()
merged_data[['지역내총생산(명목가격)', '총 방문자 수']] = scaler.fit_transform(merged_data[['지역내총생산(명목가격)', '총 방문자 수']])

# Calculate the combined score
merged_data['combined_score'] = merged_data['지역내총생산(명목가격)'] + merged_data['총 방문자 수']

# Find the region with the lowest combined score
lowest_combined_region = merged_data.loc[merged_data['combined_score'].idxmin()]

# Display the results
print("Filtered GRDP Data:")
print(filtered_grdp_data)
print("\nMerged Data:")
print(merged_data)
print(f"\nRegion with the lowest combined score: {lowest_combined_region['지역']}")

filtered_grdp_csv_path, lowest_combined_region['지역']
