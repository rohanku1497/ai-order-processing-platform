# Database Design

## Overview

The AI-Powered Order Processing & Tracking Platform stores data across multiple storage systems based on the nature of the data.

The platform follows the principle of using the most appropriate storage technology for each data type.

| Storage | Purpose |
|----------|---------|
| PostgreSQL | Structured business data (like orders)|
| Vector Database | Embeddings for Retrieval-Augmented Generation (RAG) |
| AWS S3 | Unstructured documents such as PDFs (Purchase order docs) and invoices |

---

# PostgreSQL Database

The relational database stores all business entities and transactional information.

## 1. Users

Stores application users.

### Columns

| Column | Description |
|----------|-------------|
| user_id (PK) | Unique user identifier |
| name | User name |
| email | Email address |
| role | Customer / Operations / Manager / Admin |
| created_at | User creation timestamp |

---

## 2. Orders

Stores the official business record of an order.

The Orders table contains validated business information after AI extraction and business rule validation.

### Columns

| Column | Description |
|----------|-------------|
| order_id (PK) | Unique order identifier |
| user_id (FK) | Customer placing the order |
| document_id (FK) | Uploaded purchase order document |
| customer_name | Customer name |
| total_amount | Total order amount |
| currency | Currency |
| priority | Normal / High / Urgent |
| status | Pending / Processing / Shipped / Delivered / Cancelled |
| approval_status | Pending / Approved / Rejected |
| ai_confidence | AI confidence score for extracted information |
| created_at | Order creation timestamp |
| updated_at | Last update timestamp |

The Orders table stores the final validated business information and not the raw AI output.

---

## 3. Shipments

Stores shipment information after an order has been approved.

### Columns

| Column | Description |
|----------|-------------|
| shipment_id (PK) | Unique shipment identifier |
| order_id (FK) | Associated order |
| carrier | Logistics provider |
| tracking_number | Shipment tracking number |
| shipment_status | Created / In Transit / Delivered / Delayed |
| estimated_delivery | Estimated delivery date |
| actual_delivery | Actual delivery date |

Shipment information is linked to Orders through the order_id foreign key.

---

## 4. Documents

Stores metadata for uploaded documents.

The actual files are stored in AWS S3.

### Columns

| Column | Description |
|----------|-------------|
| document_id (PK) | Unique document identifier |
| document_type | Purchase Order / Invoice / Policy |
| s3_path | Location of file in AWS S3 |
| uploaded_by | User who uploaded the document |
| upload_time | Upload timestamp |

Only metadata is stored in PostgreSQL.

---

# Relationships

```
Users

   │

   │ 1 : Many

   ▼

Orders

   │

   │ 1 : 1 (initial version)

   ▼

Shipments

Orders

   │

   │ 1 : 1

   ▼

Documents
```

---

# Vector Database

The vector database stores semantic embeddings generated from company knowledge documents.

Examples include:

- Shipping Policies
- Return Policies
- Approval Policies
- SLA Documents
- Delivery Guidelines

Each stored vector contains:

- Chunk embedding
- Chunk text
- Metadata
- Source document reference
- Page number

The vector database is used exclusively for semantic retrieval within the RAG pipeline.

---

# AWS S3

AWS S3 stores all uploaded documents.

Examples:

- Purchase Order PDFs
- Invoice PDFs
- Shipping Documents
- Policy Documents

The relational database stores only metadata and references to these files.

---

# Data Flow

The high-level data flow is shown below.

```
Customer Upload

       │

       ▼

AWS S3

       │

       ▼

AI Extraction

       │

       ▼

Business Validation

       │

       ▼

Orders Table

       │

       ▼

Shipment Creation

       │

       ▼

Shipments Table
```

---

# Design Decisions

## Why store documents in AWS S3?

PDFs and invoices are unstructured files and are better suited for object storage than relational databases.

---

## Why use a Vector Database?

Policy documents are converted into embeddings and stored in the vector database to enable semantic retrieval through Retrieval-Augmented Generation (RAG).

---

## Why store AI confidence in Orders?

The confidence score helps determine whether an order can be automatically approved or requires manual review.

The platform stores only the AI confidence score in Version 1.

Raw LLM responses and prompts are intentionally not persisted to keep the design simple.

---

# Future Enhancements

Future versions of the platform may introduce additional entities such as:

- AI Processing History
- Order Approval Workflow
- Notification History
- Chat History
- Audit Logs
- Payment Information

These have intentionally been excluded from Version 1 to maintain a clean and focused database design.