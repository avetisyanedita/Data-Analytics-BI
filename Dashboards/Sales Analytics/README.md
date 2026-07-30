# 📊 Classic Models Sales Performance Analytics

![Data Analytics](https://img.shields.io/badge/Data_Analytics-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Looker](https://img.shields.io/badge/Looker_Dashboard-4285F4?style=for-the-badge&logo=looker&logoColor=white)
![Sales Performance](https://img.shields.io/badge/Sales_Performance-2C3E50?style=for-the-badge)
![Business Intelligence](https://img.shields.io/badge/Business_Intelligence-E06D53?style=for-the-badge)

## 📌 Executive Summary
Sales performance tracking and inventory management are critical for maintaining healthy cash flow and operational stability. This project delivers an executive-level **Classic Models Sales Performance Dashboard** built in Looker. By evaluating product profitability, sales trends, credit utilization, and regional sales distribution, this analytics suite identifies key revenue drivers and exposes credit risk exposures.

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

## 🛠️ Data Architecture & Schema Model

Designed with a structured dimensional schema to streamline relationships, maintain transactional granularity across product lines and offices, and optimize reporting performance.
<img width="1142" height="695" alt="Schema" src="https://github.com/user-attachments/assets/025dc218-c346-40bb-9ff5-ab7456d100dd" />

---

## 🧰 Toolkit
| <div align="center"><h3>Scope</h3></div> | <div align="center"><h3>Technology</h3></div> | <div align="center"><h3>Business Impact & Execution</h3></div> |
| :--- | :---: | :--- |
| <div nowrap="nowrap">**Data Extraction**</div> | <img src="https://img.shields.io/badge/SQL_Database-4A607A?style=for-the-badge&logo=postgresql&logoColor=white"/> | Ingested relational sales, customer, product line, and employee operational data from the Classic Models database. |
| <div nowrap="nowrap">**Data Transformation**</div> | <img src="https://img.shields.io/badge/SQL_%2F_LookML-4285F4?style=for-the-badge&logo=looker&logoColor=white"/> | Modeled views and explores, standardized calculated fields, and defined dimensions and measures for financial reporting. |
| <div nowrap="nowrap">**Semantic Layer**</div> | <img src="https://img.shields.io/badge/Looker_Model-E06D53?style=for-the-badge&logo=looker&logoColor=white"/> | Centralized business logic using LookML, engineered core revenue KPIs, credit ratios, profitability margins, and order fulfillment metrics. |
| <div nowrap="nowrap">**Data Visualization**</div> | <img src="https://img.shields.io/badge/Looker_Dashboard-4285F4?style=for-the-badge&logo=looker&logoColor=white"/> | Delivered an intuitive executive dashboard featuring custom themes, geographic maps, scatter plots, and dynamic filtering for real-time sales monitoring. |

---

## 📈 Dashboard

<img width="1277" height="712" alt="Classic Models Sales Performance Overview" src="https://github.com/user-attachments/assets/0a0ee168-5fdb-4a06-b0bd-441f8432f0fa" />

---

## 👩‍💻 About the Author
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
