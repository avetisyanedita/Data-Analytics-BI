# 🚕 Yandex Go — Taxi Ride Fare & Route Analytics

![ETL](https://img.shields.io/badge/ETL-0078D4?style=for-the-badge)
![Python](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/POWER_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![UI/UX Design](https://img.shields.io/badge/UI%2FUX_DESIGN-E06D53?style=for-the-badge)

## 📌 Executive Summary

This project delivers an interactive **Yandex Go Taxi Ride Fare & Route Analytics Report** designed to evaluate how ride fares vary across **routes, distances, ride categories, trip duration, and operating conditions**.

Built in **Power BI**, the solution transforms route-level ride data into an executive analytics experience that enables users to compare fare structures, identify pricing patterns, investigate route-level performance, and understand how ride characteristics influence the final fare.

The dashboard consists of two analytical views:

- **Dashboard** — executive-level KPIs and visual analysis of fare behavior.
- **Details** — granular route-level fare and trip analysis with week-over-week comparisons.

The analysis focuses on **Yerevan City**, covering **30 business-hub routes** during the selected reporting period.

---

## 🎯Stakeholder Objectives

The report is designed to help **end-users understand and compare taxi ride fares** across different routes, distances, ride categories, and trip conditions.

The analysis focuses on questions that matter when evaluating a ride:

- **How much does a ride cost?** — Understand average starting and total fares across trips.
- **How does distance affect the fare?** — Compare the cost of shorter and longer journeys and identify changes in the effective fare per kilometer.
- **Which ride category offers the best fit?** — Compare fare levels across Start, Comfort, Comfort+, Minivan, and Premier categories.
- **How does the route affect the price?** — Explore fare differences between routes and understand how trip characteristics influence the final cost.
- **How does trip duration relate to the fare?** — Compare journey time and distance with the total amount paid.
- **How have fares changed over time?** — Track week-over-week changes in start fare, total fare, and trip duration.
- **How do trip conditions influence the journey?** — Consider factors such as weather and travel conditions when interpreting fare and duration differences.

---

## 🔍 Key Findings & User Takeaways

- **Average ride:** Start Fare **981 AMD**, Total Fare **2,205 AMD**, Distance **4.39 km**, and Duration **21.3 min**.
- **Fare vs. distance:** The effective fare per kilometer generally decreases as trip distance increases, from approximately **868 AMD/km** for 1–2 km trips to **333 AMD/km** for 9–12 km trips.
- **Ride categories:** Fare structures vary across **Start, Comfort, Comfort+, Minivan, and Premier**, allowing users to compare price differences between service levels.
- **Route variation:** The **30 analyzed routes** show noticeable differences in fare, duration, distance, and markup, even for trips with similar characteristics.
- **Period changes:** Average Total Fare increased **6.2%**, while average trip duration increased **17.2%**, indicating that longer journey times did not translate proportionally into higher fares.
- **Trip conditions:** Temperature and weather provide additional context when comparing fare and duration across rides.

Overall, the report helps users **compare ride costs, understand fare-per-distance patterns, and evaluate price differences across routes and ride categories**.

---
## 🛠️ Toolkit

| <div align="center"><h3>Data</h3></div> | <div align="center"><h3>Technology</h3></div> | <div align="center"><h3>Business Impact & Execution</h3></div> |
| :--- | :---: | :--- |
| <div nowrap="nowrap">**Collection**</div> | <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> | Collected and consolidated ride-level data programmatically to create a structured dataset for fare and route analysis. |
| <div nowrap="nowrap">**Preparation**</div> | <img src="https://img.shields.io/badge/Google_Sheets-34A853?style=for-the-badge&logo=googlesheets&logoColor=white"/> | Organized, validated, and prepared the collected data for downstream analysis and reporting. |
| <div nowrap="nowrap">**Modeling**</div> | <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/> | Designed a **star schema** to structure ride, route, fare, and supporting dimensions for efficient analysis and reporting. |
| <div nowrap="nowrap">**Analysis**</div> | <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/> | Developed analytical KPIs and views to evaluate fares, fare-per-kilometer, trip duration, route variation, and period-over-period changes. |
| <div nowrap="nowrap">**UI/UX Design**</div> | <img src="https://img.shields.io/badge/Pen.dev-2C3E50?style=for-the-badge"/> | Designed and prototyped the dashboard interface in **Pen.dev**, focusing on visual hierarchy, intuitive navigation, usability, and a consistent user experience. |

---

## 📊 Report Preview

### 01 — Executive Dashboard

The main dashboard provides a high-level view of taxi ride economics and enables interactive analysis by **distance, ride category, route, weather condition, and trip characteristics**.

<img width="1195" height="671" alt="Yandex 1" src="https://github.com/user-attachments/assets/12b2c494-a5ea-446e-93f7-c6987fba84fb" />



### 02 — Route-Level Details

The details page provides granular analysis of individual rides and routes.

This view allows users to move from **high-level trends to individual route-level observations**.

<img width="1192" height="667" alt="Yandex 2" src="https://github.com/user-attachments/assets/1c02a1d9-a85a-4267-89b6-6b2b07e23e81" />


---


## 👩‍💻 About the Analyst

<table width="100%" style="border: none; border-collapse: collapse;">
  <tr>
    <td align="center" style="border: none; padding: 15px;">
      <p style="margin: 0 0 15px 0; line-height: 1.6; max-width: 600px;">
        Hi, I'm <b>Edita Avetisyan</b>—I bridge the gap between finance, operations, and analytics, combining business thinking with technical BI capabilities to turn complex data into strategic insights. Beyond data, I believe in genuine human connections.
      </p>
      <p style="margin: 0 0 20px 0; line-height: 1.6; max-width: 600px; color: #555; font-size: 0.95em;">
        <em>💡 Feel free to reach out via LinkedIn if you'd like to request project files or datasets for your learning journey!</em>
      </p>
      <a href="https://www.linkedin.com/in/edita-avetisyan" target="_blank" rel="noopener noreferrer">
        <img src="https://img.shields.io/badge/Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile" />
      </a>
    </td>
  </tr>
</table>
