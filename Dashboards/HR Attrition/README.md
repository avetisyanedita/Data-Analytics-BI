# 📊 Enterprise HR Attrition & Retention Analytics

![Data Analytics](https://img.shields.io/badge/Data_Analytics-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![HR Analytics](https://img.shields.io/badge/HR_Analytics-E06D53?style=for-the-badge)
![Retention Strategy](https://img.shields.io/badge/Retention_Strategy-2C3E50?style=for-the-badge)

## 📌 Executive Summary
Employee attrition poses significant financial, operational, and operational-culture risks to modern organizations. This project delivers an executive-level **HR Attrition & Workforce Retention Dashboard** built in Power BI. By evaluating demographic factors, job roles, tenure, salary brackets, and work-life balance indicators, this analytics suite identifies key turnover drivers and provides actionable retention strategies.

---

## 🔍 Key Findings & Analytical Insights

* **Tenure Attrition Spike:** Attrition peaks significantly during **Year 1** and **Year 3–5** of tenure, highlighting critical windows during onboarding and mid-level career progression.
* **Role Vulnerability:** Sales Representatives, Laboratory Technicians, and Research Scientists demonstrate higher turnover rates compared to leadership roles.
* **Overtime Impact:** Employees working consistent overtime exhibit a dramatically higher rate of voluntary departure compared to non-overtime peers.
* **Compensation vs. Satisfaction:** Low-to-mid salary tiers show elevated sensitivity to job dissatisfaction, pointing to compensation band compressed friction.

---

## 💡 Strategic Recommendations

1. **Structured 30-60-90 Day Onboarding:** Mitigate early-stage turnover (Year 1) by establishing formal mentorship and integration checkpoints.
2. **Mid-Career Pathway Reviews:** Implement structured growth and internal mobility reviews at the **2-to-3 year mark** to address mid-level stagnation.
3. **Overtime & Burnout Guardrails:** Monitor high-overtime departments; reallocate workloads or leverage contract staffing to prevent burnout in frontline roles.
4. **Targeted Retention Bonuses:** Focus compensation adjustments and stay-interviews on critical, high-attrition roles (e.g., Lab Technicians, Sales Reps).

---

## 🛠️ Data Architecture & Schema Model

Designed as a **Snowflake Schema** to streamline relationships, preserve lookup granularity for education and dates, and maximize DAX query performance.
<img width="1142" height="695" alt="Schema" src="https://github.com/user-attachments/assets/025dc218-c346-40bb-9ff5-ab7456d100dd" />

---

## 🧰 Toolkit & Business Value Stack

| Domain | Technology | Implementation & Strategic Impact |
| :--- | :--- | :--- |
| <div nowrap="nowrap">**Data Extraction**</div> | <img src="https://img.shields.io/badge/CSV_Files-2C3E50?style=for-the-badge&logo=file-type-csv&logoColor=white"/> | Consolidated raw HR records covering employee demographics, tenure history, and engagement feedback into a central data pipeline. |
| <div nowrap="nowrap">**Data Transformation**</div> | <img src="https://img.shields.io/badge/Power_Query-4A607A?style=for-the-badge&logo=powerbi&logoColor=white"/> | Cleaned and standardized multi-source data, structuring complex survey metrics to enable fast, cross-departmental analysis. |
| <div nowrap="nowrap">**Semantic Layer**</div> | <img src="https://img.shields.io/badge/DAX-E06D53?style=for-the-badge&logo=powerbi&logoColor=white"/> | Built business logic and automated calculations to monitor retention rates, track employee sentiment, and pinpoint attrition risk factors. |
| <div nowrap="nowrap">**Data Visualization**</div> | <img src="https://img.shields.io/badge/Power_BI-F2C94C?style=for-the-badge&logo=powerbi&logoColor=black"/> | Delivered an intuitive executive dashboard with dynamic filtering, enabling HR leaders to make proactive, data-backed retention decisions. |
