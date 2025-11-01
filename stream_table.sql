-- Example: Read from a silver streaming table and create gold layer tables

-- Gold table: Aggregate total transaction amount by user
CREATE OR REFRESH STREAMING TABLE gold1_total_amount_by_currency
COMMENT 'Total transaction amount group by currency from silver layer'
AS
SELECT
  currency,
  SUM(amount) AS total_amount
FROM STREAM(local_stream_s3.silver.cls_transactions)
GROUP BY currency;

-- Gold table: Count of transactions per city
CREATE OR REFRESH STREAMING TABLE gold1_transaction_count_by_city
COMMENT 'Transaction count by city from silver layer'
AS
SELECT
  city,
  COUNT(*) AS transaction_count
FROM STREAM(local_stream_s3.silver.cls_transactions)
GROUP BY city;

-- Gold table: Top 10 users by transaction amount
CREATE OR REFRESH STREAMING TABLE gold1_top_3_nations
COMMENT 'Top 3 nations by total transaction amount from silver layer'
AS
SELECT
  username,
  SUM(amount) AS total_amount
FROM STREAM(local_stream_s3.silver.cls_transactions)
GROUP BY username
ORDER BY total_amount DESC
LIMIT 3;

CREATE OR REFRESH STREAMING TABLE gold1_total_transactions
COMMENT "total of transactions"
AS
SELECT count(*) as total_transactions
FROM STREAM(local_stream_s3.silver.cls_transactions)
