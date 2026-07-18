# PostgreSQL Application Setup, Administration & Flask Deployment Guide

# For AWS
```
DB_HOST = os.environ.get("DB_HOST", "database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com")
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com:5432/?Action=connect&DBUser=postgres&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAXZEFIC7NELACRMWI%2F20260616%2Fus-east-1%2Frds-db%2Faws4_request&X-Amz-Date=20260616T035059Z&X-Amz-Expires=900&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIHE5h9HyMDrfjGYVI%2FABPdlHS2MaEVvoiCAo2myqHTicAiEAx0DED1oSFDqEMZ6DlELX3TCY8p3ITmlK5DffG30otHoq3AIIbRAAGgw1MzUwMDI4Nzk5NjIiDDJQlqQwm9hsEmbuoyq5Ajwkc6tR5NSGCt9N6CknSbqzNUtxW9W6aiwQs205gKQ8FCRKoAEh9j0Z3CZRkorwMOoxHnJN8c2nVr07i%2F7ZUbvWuZ7%2FTxk9wKDSH%2FeoADW87yMCFtYlyp5YuIhXSHiSzQyva%2FRJeFcS8LWrvanLVS5whddcV9aLfI%2Bj6CKAUSN5wO7JxjBgloqAGdZoVGTH9wSsAvW8ASSRVKk4cII4%2BuRFGpSXulMLlwrsac6wrK06wQUEwKCwMmQcT46sGYRdaAEjuXZ45QP%2FOGlnDZye7tfb6UlN%2F6YYVCk6dRiCRa4zmLm57ikDoTgHRyS2mb9hbpviORRoCfvIrNgAwdhSFP9pLnIW4IQnFomIsZxXU6duM76Pe2O74mUURJcXXwHddKNNhgalb%2BTXJXJFvyY8R%2B3u4LNvbGdpOswwj%2FbC0QY6rQKmRPMT9%2BeEiGAIkjGhlTRLEEI3kzwbietSC%2FlVlWJWzsqHMNRo9H%2BWTvoNJylY0eeN2zpktjDeLSl6sLYBLDPayThzT%2B252XT4I%2FCwmDZCTVDsw%2BPglwAQf2MiuxRmHBuAjC9%2B6Gk7lxUpOc%2FwJwoBaxqc5HQqwNjZ%2BtmeXYlB76vWEUhlJ2MLxm4A1bzU3O9wT2Y71QxkK47UGqM1Mn5MqOf%2FX1RLY33%2Btb6x5wyA4yGTk1fEMSyp2SYsh4fVQlKcs1Oc5hYZZZZxTtQRrVZJjMRGwli99bjgFZTPwpj96oAr6N%2FfyBs7CvUO3A6rjGom3GhSCgULyWEcsRNgLeU6OSyOXHASGgiJJWGcDkEHpvUuXB5AI%2FcT8mS7eA4wiLZUMFhi6NoRzrPNr4bV&X-Amz-Signature=0afaa7626586409260d1320ef29e16e62da635b2bb78e88167a0f126ba6f58c7&X-Amz-SignedHeaders=host")

```

# For Azure 
```
DB_HOST = os.environ.get("DB_HOST", "myserver98600.postgres.database.azure.com")
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "atul")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "Password@123")
```
```
Postgrsql flexible server 

1. select configurations 
dev/test
PostgreSQL and Microsoft Entra authentication

2. create user and set password from Microsoft Entra ID 

demo@atulkamblehotmail.onmicrosoft.com

3. create user and password

Mumu0503

4. powershell run as admin >> choco install postgresql -y


git --version 
git clone https://github.com/atulkamble/postgresql-app.git
cd postgresql-app
postgres -V

5. // modify and check connections

export PGHOST=myserver98600.postgres.database.azure.com
export PGUSER=atul
export PGPORT=5432
export PGDATABASE=postgres
export PGPASSWORD=Password@123

6. connect from terminal

psql "host=myserver98600.postgres.database.azure.com port=5432 dbname=postgres user=atul sslmode=require" -W

7. create database and table

CREATE DATABASE university;

\l

CREATE TABLE student(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO student(name)
VALUES
('Atul'),
('Ravi'),
('Amit');

SELECT * FROM student;


python --version
pip --version
pip install -r requirements.txt 
python app.py
```
---

# Architecture

```text
                    +------------------+
                    |     Browser      |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |   Flask App      |
                    | Amazon Linux EC2 |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | PostgreSQL       |
                    | AWS RDS / EC2    |
                    +------------------+
```

---

# Prerequisites

## Required Software

| Software            | Purpose                |
| ------------------- | ---------------------- |
| Git                 | Source Control         |
| Python 3            | Application Runtime    |
| Pip                 | Package Manager        |
| PostgreSQL          | Database Server        |
| AWS CLI             | RDS IAM Authentication |
| Virtual Environment | Python Isolation       |

---

# Step 1: Clone Repository

```bash
git clone https://github.com/atulkamble/postgresql-app
cd postgresql-app
```

Verify:

```bash
ls -lrt
```

---

# Step 2: Create Virtual Environment

## Ubuntu / Amazon Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Verify:

```bash
which python
which pip
```

Deactivate:

```bash
deactivate
```

---

# Step 3: Install Python Packages

```bash
pip install flask
pip install psycopg2-binary
pip install gunicorn
```

or

```bash
pip install -r requirements.txt
```

---

# Step 4: Create requirements.txt

```bash
vi requirements.txt
```

Contents:

```text
Flask==3.0.3
psycopg2-binary==2.9.10
gunicorn==23.0.0
```

Install:

```bash
pip install -r requirements.txt
```

Generate Automatically:

```bash
pip freeze > requirements.txt
```

Verify:

```bash
cat requirements.txt
```

---

# Step 5: Install PostgreSQL

## Ubuntu

```bash
sudo apt update

sudo apt install postgresql postgresql-contrib -y
```

## Amazon Linux 2023

```bash
sudo dnf install postgresql15-server postgresql15 -y
```

Initialize Database:

```bash
sudo postgresql-setup --initdb
```

Enable Service:

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

Verify:

```bash
sudo systemctl status postgresql
```

---

# Step 6: Verify Installation

PostgreSQL Version

```bash
postgres -V
```

Python Version

```bash
python --version
```

Pip Version

```bash
pip --version
```

AWS CLI Version

```bash
aws --version
```

---

# Step 7: Install AWS CLI

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install
```

Configure:

```bash
aws configure
```

Provide:

```text
AWS Access Key
AWS Secret Key
Region
Output Format
```

---

# Step 8: Connect PostgreSQL

## Local PostgreSQL

```bash
sudo -i -u postgres

psql
```

---

## AWS RDS PostgreSQL IAM Authentication

Set Endpoint:

```bash
export RDSHOST="database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com"
```

Connect:

```bash
psql "host=$RDSHOST \
port=5432 \
dbname=postgres \
user=postgres \
sslmode=require \
password=$(aws rds generate-db-auth-token \
--hostname $RDSHOST \
--port 5432 \
--username postgres \
--region us-east-1)"
```

---

# Step 9: Database Administration

## Create Database

```sql
CREATE DATABASE university;
```

## List Databases

```sql
\l
```

or

```sql
SELECT datname FROM pg_database;
```

## Connect Database

```sql
\c university
```

## Delete Database

```sql
DROP DATABASE university;
```

## Exit PostgreSQL

```sql
\q
```

---

# Step 10: User Administration

Create User:

```sql
CREATE USER atul
WITH PASSWORD 'Password@123';
```

Change Password:

```sql
ALTER USER atul
WITH PASSWORD 'NewPassword@123';
```

Grant Database Access:

```sql
GRANT ALL PRIVILEGES
ON DATABASE university
TO atul;
```

Grant Schema Access:

```sql
GRANT ALL ON SCHEMA public TO atul;
```

List Users:

```sql
\du
```

or

```sql
\dg
```

Delete User:

```sql
DROP USER atul;
```

---

# Step 11: Create Flask Application

Create file:

```bash
vi app.py
```

## app.py

```python
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME", "university")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

@app.route('/')
def home():
    conn = None

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            sslmode='require'
        )

        with conn.cursor() as cur:

            cur.execute("""
            CREATE TABLE IF NOT EXISTS student(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100)
            );
            """)

            conn.commit()

            cur.execute("SELECT COUNT(*) FROM student;")

            count = cur.fetchone()[0]

        return f"Connected Successfully! Total Records: {count}"

    except psycopg2.OperationalError as e:
        return f"Database connection failed: {e}", 500

    except Exception as e:
        return f"An error occurred: {e}", 500

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

---

# Step 12: Configure Environment Variables

## AWS RDS PostgreSQL

```bash
export DB_HOST="database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com"

export DB_NAME="postgres"

export DB_USER="postgres"

export DB_PASSWORD="YourPassword"
```

Verify:

```bash
echo $DB_HOST

echo $DB_NAME

echo $DB_USER
```

---

# Step 13: Run Flask Application

```bash
sudo python3 app.py
```

Output:

```text
* Running on http://0.0.0.0:80
```

---

# Step 14: Security Groups

## Application Server

| Type  | Port | Source    |
| ----- | ---- | --------- |
| SSH   | 22   | Your IP   |
| HTTP  | 80   | 0.0.0.0/0 |
| HTTPS | 443  | 0.0.0.0/0 |

## PostgreSQL Server

| Type       | Port | Source                    |
| ---------- | ---- | ------------------------- |
| PostgreSQL | 5432 | App Server Security Group |

---

# Step 15: Test Application

Open Browser:

```text
http://APP-PUBLIC-IP
```

Expected Output:

```text
Connected Successfully! Total Records: 0
```

---

# Step 16: Sample Data Operations

Connect:

```bash
psql -U atul -d university -h localhost
```

Create Table:

```sql
CREATE TABLE student(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
```

Insert Records:

```sql
INSERT INTO student(name)
VALUES
('Atul'),
('Ravi'),
('Amit');
```

View Records:

```sql
SELECT * FROM student;
```

Update Record:

```sql
UPDATE student
SET name='Rahul'
WHERE id=2;
```

Delete Record:

```sql
DELETE FROM student
WHERE id=3;
```

---

# PostgreSQL Configuration for Remote Access

Edit Configuration:

```bash
sudo vi /var/lib/pgsql/data/postgresql.conf
```

Update:

```text
listen_addresses='*'
```

Edit Authentication File:

```bash
sudo vi /var/lib/pgsql/data/pg_hba.conf
```

Add:

```text
host all all 10.0.0.0/16 md5
```

Restart Service:

```bash
sudo systemctl restart postgresql
```

Verify:

```bash
ss -tulpn | grep 5432
```

---

# Backup and Restore

## Backup

```bash
pg_dump -U atul university > university_backup.sql
```

## Restore

```bash
psql -U atul university < university_backup.sql
```

---

# Project Structure

```text
postgresql-app/
│
├── app.py
├── requirements.txt
├── venv/
│
├── static/
│
├── templates/
│
└── README.md
```

---

# Troubleshooting Commands

Check PostgreSQL:

```bash
sudo systemctl status postgresql
```

Check Logs:

```bash
sudo journalctl -u postgresql -f
```

Check Port:

```bash
ss -tulpn | grep 5432
```

Test Connectivity:

```bash
nc -zv DB_SERVER_IP 5432
```

Verify Environment Variables:

```bash
env | grep DB_
```

---

# Production Best Practices

### Use Gunicorn

```bash
pip install gunicorn
```

Run:

```bash
gunicorn -w 4 -b 0.0.0.0:80 app:app
```

### Use Nginx Reverse Proxy

Benefits:

* Load Balancing
* SSL Termination
* Better Performance
* Security

### Store Secrets Securely

Avoid storing:

* Database Passwords
* IAM Tokens
* AWS Access Keys

Use:

* AWS Secrets Manager
* AWS Systems Manager
* Environment Variables
* IAM Roles

### Monitoring

Recommended Tools:

* Prometheus
* Grafana
* Amazon CloudWatch

---

# Complete Workflow Summary

```text
1. Install Git
2. Clone Repository
3. Create Virtual Environment
4. Create requirements.txt
5. Install Dependencies
6. Install PostgreSQL
7. Install AWS CLI
8. Configure AWS Credentials
9. Connect PostgreSQL/RDS
10. Create Database
11. Create User
12. Grant Permissions
13. Create app.py
14. Configure Environment Variables
15. Run Flask Application
16. Test Application
17. Configure Security Groups
18. Enable Monitoring
19. Implement Backup Strategy
20. Deploy with Gunicorn + Nginx
```
