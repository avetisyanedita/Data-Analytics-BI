# 📊 Sales Performance Analytics

[![Data Analytics](https://img.shields.io/badge/Data_Analytics-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)](https://github.com)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://github.com)
[![Looker](https://img.shields.io/badge/Looker_Dashboard-4285F4?style=for-the-badge&logo=looker&logoColor=white)](https://github.com)
[![Sales Performance](https://img.shields.io/badge/Sales_Performance-2C3E50?style=for-the-badge)](https://github.com)

## 📌 Executive Summary
Sales performance tracking and inventory management are critical for maintaining healthy cash flow and operational stability. This project delivers an executive-level **Classic Models Sales Performance Dashboard** built in **Looker**. By evaluating product profitability, sales trends, credit utilization, and regional sales distribution, this analytics suite identifies key revenue drivers and exposes credit risk exposures.

---

## 🔍 Key Findings & Analytical Insights

* **High Profitability:** Achieved $9.80M in total sales, securing $3.83M in net profit with a strong 38.8% margin.
* **Fulfillment Stability:** Core revenue is secure with $8.88M fully shipped across 303 orders.
* **High-Value Exposure:** Only 3 orders are Disputed, but they carry the highest average value at $4,368 per order.
* **Asset Reserves:** A massive $30.53M is tied up in global stock, driven by top performers Gerard Hernandez and Pamela Castillo.
* **Regional Anchors:** Paris dominates global sales volume, heavily driven by top performers Gerard Hernandez and Pamela Castillo.
* **Credit Risk Alert:** Sales concentration spikes dangerously at two outlier accounts with credit limits exceeding $200K.

---

## 💡 Strategic Recommendations

1. **Monitor High-Limit Credit Accounts:** Implement strict credit control and regular reviews for the two outlier customer accounts exceeding $200K in credit limits.
2. **Optimize Inventory Turnover:** Address the $30.53M tied up in global stock by streamlining warehousing and aligning stock levels with regional demand in top hubs like Paris.
3. **Resolve Disputed High-Value Orders:** Prioritize resolution for the 3 disputed orders given their significantly higher average order value ($4,368).
4. **Leverage Regional Success:** Replicate the high-performing sales strategies seen in Paris across other major offices (e.g., San Francisco, NYC, Tokyo) to balance geographical revenue concentration.

---

## 🛠️ Data Architecture

Architected using a Snowflake schema, this sales data warehouse normalizes dimension tables to streamline complex relationships and eliminate data redundancy. It features comprehensive fact tables that preserve deep, low-level transactional granularity across product lines, offices, and business processes.

<img width="1169" height="1345" alt="Classicmodels_Schema" src="https://github.com/user-attachments/assets/45d28d96-6cac-44af-a0ba-b758bc76eacf" />



---

## 🧰 Toolkit
| Scope | Technology | Business Impact & Execution |
| :--- | :--- | :--- |
| **Data Extraction** | [![MYSQL](https://img.shields.io/badge/MYSQL-2E3856?style=for-the-badge&logo=mysql&logoColor=white)](https://github.com) | Connected directly to the operational Classic Models database to extract sales, customer, product line, and employee data using complex SQL queries with CTEs and multi-table joins. |
| **Data Transformation** | [![MYSQL / LOOKML](https://img.shields.io/badge/MYSQL_%2F_LOOKML-2E3856?style=for-the-badge&logo=looker&logoColor=white)](https://github.com) | Established a live connection from MySQL to Looker, writing custom queries, CTEs, and joins to structure data, standardize calculated fields, and define core dimensions and measures. |
| **Semantic Layer** | [![LOOKER MODEL](https://img.shields.io/badge/LOOKER_MODEL-2E3856?style=for-the-badge&logo=looker&logoColor=white)](https://github.com) | Centralized business logic using LookML, engineered core revenue KPIs, credit ratios, profitability margins, and order fulfillment metrics. |
| **Data Visualization** | [![LOOKER DASHBOARD](https://img.shields.io/badge/LOOKER_DASHBOARD-2E3856?style=for-the-badge&logo=looker&logoColor=white)](https://github.com) | Delivered an intuitive executive dashboard featuring custom themes, geographic maps, scatter plots, and dynamic filtering for real-time sales monitoring. |

---

## 📈 Dashboard

<img width="3077" height="3332" alt="Classicmodels_Edita_Avetisyan_Group_4_Ardy (2)_page-0001" src="https://github.com/user-attachments/assets/f03f6c56-afba-42d3-8eb3-ba96e3c4ce00" />


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
