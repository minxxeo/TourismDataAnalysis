import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "c:/Windows/Fonts/malgun.ttf"  # 시스템에 맞는 한글 폰트 경로를 설정하세요.
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


# Load the Excel file
file_path = "C:/Users/lms26/TourismDataCompetition/202406_경상남도_고령인구비율.xlsx"
data = pd.read_excel(file_path)

# Clean and process the data
data.columns = ['행정기관코드', '행정기관', '전체', '남자', '여자', '65세이상전체', '65세이상남자', '65세이상여자']
data_cleaned = data.drop([0, 1]).reset_index(drop=True)

# Convert relevant columns to numeric values
data_cleaned['전체'] = data_cleaned['전체'].str.replace(',', '').astype(int)
data_cleaned['65세이상전체'] = data_cleaned['65세이상전체'].str.replace(',', '').astype(int)

# Calculate the elderly population ratio
data_cleaned['고령인구비율'] = data_cleaned['65세이상전체'] / data_cleaned['전체'] * 100

print(data_cleaned[['행정기관', '고령인구비율']])

# Calculate the correlation between total population and elderly population ratio
correlation = data_cleaned[['전체', '고령인구비율']].corr()

# Select only the columns '행정기관' and '고령인구비율'
data_selected = data_cleaned[['행정기관', '고령인구비율']]

# Save the selected data to a new CSV file
data_selected.to_csv('경상남도_정리된_데이터.csv', index=False)

# 막대 그래프 시각화
plt.figure(figsize=(14, 8))
plt.bar(data_selected['행정기관'], data_selected['고령인구비율'], color='skyblue')
plt.xlabel('행정기관')
plt.ylabel('고령 인구 비율 (%)')
plt.title('지역별 고령 인구 비율')
plt.xticks(rotation=90)
plt.tight_layout()

# 그래프 보여주기
plt.show()
