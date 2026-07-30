## 🛠️ Data Architecture & Schema Model

Designed with a star schema architecture featuring centralized fact tables and supporting dimension tables to optimize relationship cardinality, streamline entity filtering across product lines, offices, and orders, and maximize Power BI performance.

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#111827',
    'primaryTextColor': '#ffffff',
    'primaryBorderColor': '#2563EB',
    'lineColor': '#2563EB',
    'secondaryColor': '#111827',
    'tertiaryColor': '#111827',
    'mainBkg': '#111827',
    'nodeBkg': '#111827',
    'clusterBkg': '#111827',
    'edgeLabelBackground': '#111827'
  }
}}%%
graph TD
    subgraph Dimensions ["Dimension Tables"]
        offices["<b>offices</b><br/>━━━━━━━━━━━<br/>string officeCode (PK)<br/>string city"]
        employees["<b>employees</b><br/>━━━━━━━━━━━<br/>int employeeNumber (PK)<br/>string officeCode (FK)"]
        customers["<b>customers</b><br/>━━━━━━━━━━━<br/>int customerNumber (PK)<br/>int salesRepEmployeeNumber (FK)"]
        productlines["<b>productlines</b><br/>━━━━━━━━━━━<br/>string productLine (PK)"]
        products["<b>products</b><br/>━━━━━━━━━━━<br/>string productCode (PK)<br/>string productLine (FK)<br/>string productName"]
        orders["<b>orders</b><br/>━━━━━━━━━━━<br/>int orderNumber (PK)<br/>int customerNumber (FK)<br/>string status"]
    end

    subgraph Fact ["Fact Tables"]
        orderdetails["<b>orderdetails</b><br/>━━━━━━━━━━━<br/>int orderNumber (PK, FK)<br/>string productCode (PK, FK)<br/>decimal Sales<br/>decimal Profit"]
        payments["<b>payments</b><br/>━━━━━━━━━━━<br/>int customerNumber (PK, FK)<br/>string checkNumber (PK)<br/>decimal amount"]
    end

    offices -->|houses| employees
    employees -->|manages| customers
    productlines -->|contains| products
    customers -->|places| orders
    customers -->|makes| payments
    products -->|includes| orderdetails
    orders -->|has| orderdetails

    style orderdetails fill:#111827,stroke:#2563EB,stroke-width:2px,color:#ffffff
    style payments fill:#111827,stroke:#2563EB,stroke-width:2px,color:#ffffff
    style productlines fill:#111827,stroke:#2563EB,stroke-width:2px,color:#ffffff
    style products fill:#111827,stroke:#2563EB,stroke-width:2px,color:#ffffff
    style offices fill:#111827,stroke:#2563EB,stroke-width:2px,color:#ffffff
    style employees fill:#111827,stroke:#2563EB,stroke-width:2px,color:#ffffff
    style customers fill:#111827,stroke:#2563EB,stroke-width:2px,color:#ffffff
    style orders fill:#111827,stroke:#2563EB,stroke-width:2px,color:#ffffff
    style Fact fill:#0f172a,stroke:#334155,stroke-dasharray: 5 5,color:#94a3b8
    style Dimensions fill:#0f172a,stroke:#334155,stroke-dasharray: 5 5,color:#94a3b8
