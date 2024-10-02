# TourismDataAnalysis


## "고령화 마을의 새로운 숨결: 촌캉스 문화공간으로 재탄생”

출품작 요약 
: 고령화가 심화되고 있는 지역에서 폐건물을 리모델링하여 복합 문화·상업 공간으로 조성 및 이를 새로운 촌캉스(시골에서 즐기는 휴가) 테마의 관광자원으로 활용. 이를 통해 지역 관광 활성화와 노인 일자리 창출을 동시에 달성.



## 1. 경상남도 고령 인구/전체 인구 비율 구하기 & 시각화 ##
   분석에 사용한 데이터 : 202406_경상남도_고령인구비율.xlsx
   '행정기관', '고령인구비율’만 남기고 드랍해서 만든 데이터 : 경상남도_정리된_데이터.csv
![경상남도 고령 인구 대비 전체 인구 비율](https://github.com/user-attachments/assets/42f675fe-31e5-42b6-a239-7babbd804088)
![경상남도 지역별 고령인구비율](https://github.com/user-attachments/assets/b98dae92-2fd5-4f7e-bec5-0bdb00a5bb01)

## 2. 데이터 프레임 병합 & 클러스터링##
   분석에 사용한 데이터 : 고령인구비율_14이상_행정기관.csv
   고령인구비율과 빈집 데이터 병합하여 만든 데이터 : 고령인구빈집병합된_데이터.csv
![elbow 기법](https://github.com/user-attachments/assets/d8889616-5682-4ae7-b95e-1db24317f565)
→ 엘보우 기법으로 찾은 최적의 클러스터 개수 = 3
![클러스터링](https://github.com/user-attachments/assets/1b91a324-8831-4eea-b63a-18e385baff40)
![클러스터별 지역 출력](https://github.com/user-attachments/assets/8fe0b432-8e12-467d-a1fd-586626f6d583)
- **Cluster 0 :** 고령 인구 비율이 상대적으로 낮고 빈집 수가 적음
- **Cluster 1 :** 고령 인구 비율이 높으며, 빈집 수가 중간 정도로 존재
- **Cluster 2 :** 고령 인구 비율은 중간 정도지만 빈집 수가 매우 많음
→ Cluster 2 선택

## 3. Cluster 2 중 한 개의 지역 선택 ##
[한국관광공사 DATA LAB > 지역별 분석 > 지역별 현황 > 지역별 관광 현황 (visitkorea.or.kr)](https://datalab.visitkorea.or.kr/datalab/portal/loc/getAreaDataForm.do?SGG_CD=48125#)
→ 한국관광데이터랩에서 지역 별 관광자 수 데이터 가져옴

**Cluster 2 중 지역 선택 기준**
1. **관광 잠재력이 높은 지역 → 자연경관, 역사적/문화적 유산, 관광 명소가 있거나 교통 접근성 (대중교통, 주요 도로와의 접근성)이 좋은지 확인**
2. **지역 경제 활성화가 필요한 지역 → 지역 경제가 침체되어 있거나 새로운 활력이 필요한 지역을 우선적으로 고려 / 지역 내총생산(GRDP) 파악** [지역 내 총 생산(GRDP) (changwon.go.kr)](https://bigdata.changwon.go.kr/portal/statUse/stat/cwStat.do?menuDiv=10)
![grdp](https://github.com/user-attachments/assets/de09b81e-f939-4852-b0e6-70d598a3364a)
지역GRDP(지역내총생산(명목가격))과 총 방문자 수를 Standardscaler를 사용하여 0과 1사이로 정규화하고 그 합산 값이 가장 적은 지역을 선정
→ 밀양시 선정
