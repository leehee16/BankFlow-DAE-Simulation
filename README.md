# 📊 Mobile Customer Analytics

고객 생애가치(Customer Lifetime Value), 리텐션 분석(Retention), 코호트 분석(Cohort Analysis) 등 모바일 서비스 분석에 필수적인 지표와 모델링을 Python + SQL 기반으로 학습하고 실습하는 프로젝트입니다.

---

## 배워야 할 개념들

### Retention Analysis
- **Retention**: 사용자가 특정 시점 이후에도 계속 서비스에 머무는 비율. Day 1, Day 7, Day 30 등으로 측정함.
- **Retention Curve**: 시점별 사용자 잔존 비율을 시각화한 그래프. 사용자 이탈 시점을 파악하는 데 유용함.
- **Rolling Retention vs. N-Day Retention**: 특정 날짜에 여전히 남아있는 비율(Rolling)과 특정 날짜에만 남아있는 비율(N-Day)을 구분해야 함.
- **Segmented Retention**: 사용자 유형/채널/기기별 잔존율을 비교해 마케팅 효율성을 분석함.

---

### Cohort Analysis
- **Cohort**: 동일한 시점 또는 조건으로 그룹화된 사용자 집단. 예: 가입 월 Cohort, 첫 구매 Cohort.
- **Cohort Retention Table**: Cohort별 잔존율을 주차/월차 기준으로 테이블화해 분석함.
- **Behavioral Cohort**: 단순 가입일이 아니라 특정 행동(예: 첫 결제) 기준으로 그룹을 정의할 수도 있음.
- **Cohort 간 비교**: 제품 변경, 프로모션 효과, 기능 출시 전후의 영향을 그룹 간 비교 가능.

---

### Customer Lifetime Value (CLV)
- **CLV (Customer Lifetime Value)**: 사용자가 서비스에 머무는 동안 발생시킬 것으로 예상되는 총 수익.
- **RFM 분석**: 최근성(Recency), 빈도(Frequency), 금액(Monetary)를 기반으로 사용자를 분류하고 CLV를 추정.
- **BG/NBD 모델**: 고객의 생존 여부 및 구매 횟수를 확률적으로 예측하는 모델 (Python 라이브러리 `lifetimes` 사용).
- **Gamma-Gamma 모델**: 고객이 거래 시 사용하는 금액을 예측하기 위한 보완 모델.
- **CLV 기반 세그먼트**: 고객군을 CLV로 나눠서 마케팅 예산을 전략적으로 집행 가능.

---

### Funnel Analysis (선택적 학습)
- **Funnel**: 유저의 전환 경로를 시각화해 이탈 구간을 파악하는 분석법.
- **Conversion Rate**: 단계 간 전환율을 계산하여 병목 구간을 찾아냄.
- **이벤트 로그 기반 분석**: 클릭, 탐색, 구매 등 이벤트 데이터를 기반으로 퍼널 구성.

---

### 데이터 모델링 및 전처리
- **Session/Visit 정의**: Retention 및 Funnel 분석에 필요한 시간 단위 정의.
- **User Event Log 가공**: SQL 또는 Python으로 시간 순 정렬, 그룹화 등.
- **Cohort 기준 설정**: SQL에서 JOIN + WHERE 조건으로 그룹 정의.

---

## 기술 스택

### Language
- **Python**
- **SQL (MySQL or BigQuery 등)**

### Python Libraries
- `pandas`, `numpy`: 데이터 처리
- `matplotlib`, `seaborn`, `plotly`: 시각화
- `lifetimes`: CLV 예측 모델 (BG/NBD, Gamma-Gamma 등)
- `cohortretention` 또는 커스텀 시각화 함수

---

## 실습 흐름
1. SQL로 유저 가입 Cohort 및 이벤트 로그 추출
2. Python에서 Retention Curve 시각화
3. Cohort별 CLV 누적 비교
4. BG/NBD 모델로 생존/재구매 확률 추정
5. 유저 세그먼트 정의 및 마케팅 전략 도출

### 🎯 Retention & Cohort Analysis
- **Amplitude: Blog – Retention**  
  다양한 리텐션 사례 및 분석 인사이트 제공. Day N, 커스텀 bracket 등 다양한 방식 소개  [oai_citation:0‡amplitude.com](https://amplitude.com/blog/tag/retention?utm_source=chatgpt.com)
- **Amplitude: Cohorts to Improve Your Retention**  
  획득·행동·예측 Cohort 구분을 통해 이탈 방지 전략 제시  [oai_citation:1‡amplitude.com](https://amplitude.com/blog/cohorts-to-improve-your-retention?utm_source=chatgpt.com)
- **Amplitude: The Amplitude Guide to Building a Successful Customer Retention Strategy** (Mar 31 2025)  
  retention 프로그램 구축 실전 가이드, KPI 및 전략 체계 제시  [oai_citation:2‡amplitude.com](https://amplitude.com/blog/customer-retention-strategy?utm_source=chatgpt.com)

### 🚀 Growth & Retention Frameworks
- **Reforge: Analyze Cohort Retention**  
  성장 대응 관점에서 Cohort 분석 및 가설 검증을 위한 실천 방식 소개  [oai_citation:3‡reforge.com](https://www.reforge.com/guides/analyze-cohort-retention?utm_source=chatgpt.com)
- **CleverTap 인터뷰 – Brian Balfour** (Reforge CEO/WP):  
  “Retention is the center of the growth engine” — retention과 acquisition, monetization 간 상관관계 강조  [oai_citation:4‡clevertap.com](https://clevertap.com/blog/brian-balfour-reforge-retention-matters/?utm_source=chatgpt.com)

### 🔬 Customer Lifetime Value (CLV)
- **Omniconvert: 10 KPIs with major impact on CLV**  
  CAC, Margins, Cohort Stickiness 등 CLV에 직접 영향을 주는 KPI 정리  [oai_citation:5‡omniconvert.com](https://www.omniconvert.com/blog/10-kpis-major-impact-customer-lifetime-value/?utm_source=chatgpt.com)

### 🧩 Retention Modeling
- **Amplitude: How to Build a Retention Model** (Jul 11 2023)  
  Duolingo 사례 기반 retention 모델 구성 워크플로우 공유  [oai_citation:6‡amplitude.com](https://amplitude.com/blog/build-retention-model?utm_source=chatgpt.com)
