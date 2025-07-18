# 📊 BankFlow DAE Simulation  
> **유저 행동 기반 DW 구축 및 분석 환경 설계**

## dataset(https://huggingface.co/datasets/ai-lab/MBD)
#  Multimodal Banking Dataset (MBD)

| 파일명                | 용량      | 설명                                      | 비고                           |
|-----------------------|-----------|-------------------------------------------|--------------------------------|
| `detail.tar.gz`       | **38.2GB** | 거래, 위치, 상담 등 원시 로그 전체        | ✅  DAE 실습의 핵심 데이터 |
| `client_split.tar.gz` | **39MB**   | 클라이언트별 Fold/샘플 정보               | ✅ 필수 (CV, join용)           |
| `targets.tar.gz`      | **62MB**   | 예측 라벨 및 부가 지표 포함               | ✅ KPI, supervised 분석용      |
| `ptls.tar.gz`         | **30.7GB** | 벡터 임베딩 포함된 모델 입력용 구조       | ❌  DAE 목적상 사용하지 않음 |

-> 60기가만 빌렸는데, 용량 컨트롤이 관건

## 📌 데이터셋 개요

Multimodal Banking Dataset(MBD)은 **은행 고객의 거래/위치/상담 이력 데이터를 기반으로**,  
**향후 1개월 내 금융상품 구매 가능성을 예측**하는 목적의 대규모 멀티모달 데이터셋

12개월간의 실제 로그 기반 데이터로 구성되어 있으며, 모든 정보는 익명화

> TDAE 실습을 위한 목적에 맞춰 벡터 임베딩을 제외한 **데이터 처리, 분석, 마트 설계** 중심으로 가져옴(임베딩 제외)

---


## 🧱 주요 데이터 구성

### ✅ client_split

| 컬럼명        | 설명                                  |
|---------------|---------------------------------------|
| `client_id`   | 클라이언트 고유 식별자                 |
| `fold`        | 5-Fold 교차검증용 그룹 번호             |
| `is_balanced` | 균형 샘플 여부 (1이면 균형 포함 클라이언트) |

---

### ✅ detail

#### 🔹 trx: 거래 이력

| 컬럼명        | 설명                        |
|---------------|-----------------------------|
| `client_id`   | 고객 ID                     |
| `event_time`  | 거래 발생 시점               |
| `amount`      | 거래 금액                   |
| `event_type`  | 거래 유형                   |
| `currency`    | 통화 구분                   |
| `src_*`, `dst_*` | 송신/수신자의 특성 정보 다수 포함 |
| `fold`, `is_balanced` | Fold 및 샘플 구분 정보 |

---

#### 🔹 geo: 위치 정보 (Geohash 기반)

| 컬럼명        | 설명                      |
|---------------|---------------------------|
| `client_id`   | 고객 ID                   |
| `event_time`  | 이벤트 발생 시점          |
| `geohash_4~6` | 지역 정밀도별 위치 코드   |
| `fold`, `is_balanced` | Fold 및 샘플 구분 정보 |

---

#### 🔹 dialog: 상담 이력 (벡터 제외)

| 컬럼명        | 설명                       |
|---------------|----------------------------|
| `client_id`   | 고객 ID                    |
| `event_time`  | 대화 발생 시점             |
| (임베딩은 사용하지 않음) | –               |
| `fold`, `is_balanced` | Fold 및 샘플 구분 정보 |

---

### ✅ targets (예측 라벨 및 보조 지표)

| 컬럼명            | 설명                                      |
|-------------------|-------------------------------------------|
| `client_id`       | 고객 ID                                   |
| `mon`             | 보고 기준 월                              |
| `target_1~4`      | 각 금융상품에 대한 구매 여부 (0 또는 1)     |
| `trans_count`     | 월 기준 거래 횟수                          |
| `diff_trans_date` | 거래 간 평균 시간 간격                     |
| `fold`, `is_balanced` | Fold 및 샘플 구분 정보                  |

→ 예측용 라벨 및 특성 조합 기반 KPI 정의 가능  
→ 전환율, 상품별 구매율 등으로 마트 설계

---

## 목적 

유저 행동 기반 거래 데이터를 바탕으로 **신뢰할 수 있는 DW(Data Warehouse)**와  활용성 높은 Data Mart를 구축하고,  
이를 통해 조직 구성원이 **쉽게 데이터를 찾고, 신뢰하며, 효율적으로 분석할 수 있는  DAE 실무 기반 데이터 환경**을 구현한다.

---

## 목표

### 1. DW 구조 설계 및 구현
- 도메인 중심의 정규화 테이블 설계 (Fact / Dim)
- 사용자, 거래, 상품, 채널, 시간 등 핵심 엔터티 구성

### 2. Data Mart 구축 (OLAP)
- 고객별 월별 거래 추이
- 채널별 이용율, 상품군별 매출 요약 등 KPI용 마트 생성

### 3. ETL 자동화 파이프라인 구성
- Airflow DAG 기반 `raw → dw → mart` 변환 흐름 구성
- 주기적 백필, 변경사항 반영 등 자동화 포함

### 4. 데이터 품질 관리 및 모니터링
- Great Expectations 활용 룰 기반 검증 시스템 구성
- 품질 실패 리포트 자동화 및 알림 로직 포함

### 5. 시각화 및 분석 지원
- Streamlit / Superset 연결
- 마트 기반 KPI 트렌드 시각화 및 사용자 인터페이스 제공

### 6. 문서화 및 데이터 오너십 체계 수립
- ERD, 마트 스키마, 품질 룰, ETL 흐름 등 전 과정 문서화

## 스택

| 영역            | 도구                                   | 선택 이유 / 목적                                                 | 제약사항 및 고려                             |
| ------------- | ------------------------------------ | ---------------------------------------------------------- | ------------------------------------- |
| **데이터 저장소**   | `HDFS` / `Parquet` / `DuckDB`        | 대용량 분산 파일 저장 (HDFS), 컬럼형 압축 저장 (Parquet), 경량 OLAP (DuckDB) | HDFS는 클러스터 필요 / DuckDB는 단일 머신 한계      |
| **데이터 처리**    | `Apache Spark (PySpark)`             | 대규모 병렬 데이터 처리, 유연한 전처리, 집계, 변환 가능                          | 리소스 요구 높음, 클러스터 환경 필요 (로컬 실행은 한계)     |
| **ETL 자동화**   | `Apache Airflow`                     | DAG 기반 파이프라인 관리, 스케줄링, 의존성 제어                              | 셋업 복잡, 오버헤드 있음 (경량용은 Prefect 등 고려 가능) |
| **데이터 품질 관리** | `Great Expectations (Spark backend)` | 룰 기반 데이터 검증, validation 자동화, 알림 설정 가능                      | 룰 작성 난이도 다소 있음, 셋업 필요                 |
| **메타데이터 관리**  | `Hive Metastore`, `Markdown`         | 테이블 정의 일관성 확보 (Hive), 문서화 관리 (Markdown)                    | Hive는 설치 부담, Markdown은 협업 제한          |
| **시각화 & 분석**  | `frontend`              | 대시보드 구축, KPI 시각화, 분석가 인터페이스 제공                             | next.js + ai코딩툴  |

| 환경 조건        | 제약 / 요구 조건                            |
| ------------ | ------------------------------------- |
| 클라우드 인프라 없음  | Hadoop 클러스터, Impala 등 실습 어려움          |
| 로컬 머신 제한     | Spark 로컬 실행은 가능하나 성능 제한 큼             |
| t2-small 환경 -> gcp로 변경  | Airflow + Spark 병행 어려움    |

