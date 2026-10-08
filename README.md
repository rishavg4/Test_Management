# QA & Test Management Dashboard

Interactive, enterprise-grade QA and Test Management reporting dashboard built for tracking test execution, defect lifecycles, traceability, automated discrepancy audits, and sign-off readiness.

---

## 🚀 Features

- **Executive Metrics & KPIs**: Total TCs, executed count, pass/fail/blocked breakdown, pass rate %, defect counts by priority (P1–P4).
- **Execution Trend & Progress Visualizations**:
  - Execution trend line chart with smoothed curves.
  - Defect status doughnut & priority distribution charts.
  - Module coverage pass rate % horizontal bar chart.
  - Separated cumulative execution (Planned vs Actual) and daily execution breakdown.
  - Daily progress detail table with directional trend indicators.
- **Data Ingestion Options**:
  - **Jira / Azure DevOps / HP ALM API Connector**: Direct live REST API synchronization for project work items, test runs, and defect backlog using project keys, custom endpoints, and tokens.
  - **Excel Workbook Upload**: Drag-and-drop `.xlsx`/`.xls` files with automatic multi-sheet detection (`All TC`, `Defect List`, `Defect vs TC`).
  - **Screenshot/Image OCR**: Embedded OCR table parser powered by Tesseract.js (`.png`, `.jpg`, `.jpeg`, `.webp`).
  - **IBM Box & SharePoint Importer**: Direct ingestion from cloud URLs and shared folder links.
  - **1-Click Sample & Demo Presets**: Instant load of enterprise test suites and defect tracking matrices.
- **Discrepancy Audit ("Discrip" Tab)**:
  - Real-time audit engine scanning for inconsistent defect statuses, duplicate TCs with contradictory outcomes, passed test cases with unresolved blockers, failed TCs lacking defects, and premature closure dates.
- **Traceability & Defect Modals**: Detailed defect drill-down with bidirectional linked test case resolution and interactive filters.
- **Interactive Layout Customization**:
  - Drag-and-drop block reordering (up, down, left, right) with visual drop boundaries.
  - Resizable dashboard cards and chart panels.
  - Remove/dismiss cards (`✕`) with instant restoration (`👁️ Restore Removed Blocks`).
- **AI QA Assistant**: Domain-restricted interactive chatbot for querying metrics, root causes, tester workloads, and release recommendations.
- **PDF Export**: Single-click PDF export powered by `html2pdf.js`.

---

## 📁 Repository Structure

```
├── .gitignore
├── README.md
├── test-management/
│   ├── index.html               # Main QA Test Management Dashboard
│   ├── HUB_Test_Data.xlsx       # Sample Excel workbook (TCs, Defects, Mappings)
│   └── generate_test_data.py   # Python script to generate sample test datasets
```

---

## 🛠️ Quick Start / Usage

No server installation or build steps required. The dashboard runs directly in modern web browsers:

1. **Open in Browser**:
   - Open [`test-management/index.html`](test-management/index.html) in Google Chrome, Microsoft Edge, Mozilla Firefox, or Safari.
2. **Load Data**:
   - Click **"📂 Click to browse or drag & drop .xlsx / .xls"** to load your QA report workbook.
   - Or click **"✨ Quick Load Sample Data"** to explore all dashboard features immediately.
   - Or click **"🖼️ Load Screenshot Sample"** / upload a screenshot table for OCR table extraction.

---

## 🐍 Generating Custom Test Workbooks (Optional)

You can generate custom Excel test datasets using Python:

```bash
cd test-management
pip install pandas openpyxl
python generate_test_data.py
```

---

## 🔒 Security & Privacy

- **Client-Side Only**: All data parsing (Excel, OCR, calculations) runs entirely in the browser memory. No data is sent to external servers.
- **Zero Secrets**: No API keys, credentials, or sensitive configurations stored in the codebase.
