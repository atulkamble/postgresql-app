# PostgreSQL Application Setup & Database Administration Guide

## 1. Clone the Application Repository

```bash
git clone https://github.com/atulkamble/postgresql-app
cd postgresql-app
```

---

## 2. Create and Activate Python Virtual Environment

### Linux / Ubuntu / Amazon Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Verify Virtual Environment

```bash
which python
which pip
```

---

## 3. Install PostgreSQL

### PostgreSQL Official Website

[PostgreSQL Downloads](https://www.postgresql.org/download/?utm_source=chatgpt.com)

### Ubuntu

```bash
sudo apt update
sudo apt install postgresql -y
```

### Amazon Linux / RHEL

```bash
sudo dnf install postgresql15 -y
```

---

## 4. Verify PostgreSQL Installation

```bash
postgres -V
```

Example Output:

```text
postgres (PostgreSQL) 16.x
```

---

# 5. Connect to AWS RDS PostgreSQL using IAM Authentication

## Set RDS Endpoint

```bash
export RDSHOST="database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com"
```

## Connect Using Generated Authentication Token

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

### Prerequisites

* AWS CLI installed
* AWS CLI configured

```bash
aws configure
```

* IAM Database Authentication enabled on RDS
* User mapped for IAM Authentication

---

# 6. Create Database

```sql
CREATE DATABASE university;
```

---

# 7. List Available Databases

### Method 1

```sql
\list
```

### Method 2

```sql
SELECT datname FROM pg_database;
```

Example:

```text
postgres
template0
template1
university
```

---

# 8. Exit PostgreSQL

```sql
\q
```

---

# 9. Create Database User

```sql
CREATE USER atul WITH PASSWORD 'Password@123';
```

---

# 10. Change User Password

```sql
ALTER USER atul WITH PASSWORD 'new_password';
```

---

# 11. Grant Database Permissions

```sql
GRANT ALL PRIVILEGES ON DATABASE university TO atul;
```

---

# 12. List Database Users and Roles

### Method 1

```sql
\du
```

### Method 2

```sql
\dg
```

Example:

```text
Role name | Attributes
-----------+--------------------------
postgres   | Superuser
atul       |
```

---

# 13. Verify Python Installation

```bash
python --version
```

Example:

```text
Python 3.12.x
```

---

# 14. Verify Pip Installation

```bash
pip --version
```

Example:

```text
pip 24.x
```

---

# 15. Install Pip Manually

If pip is not installed:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

---

# 16. Upgrade Pip

### Method 1

```bash
python -m pip install --upgrade pip
```

### Method 2

```bash
pip install --upgrade pip
```

---

# 17. Install Required Packages (Amazon Linux / RHEL)

```bash
sudo dnf install python3 python3-pip git -y
```

Verify:

```bash
python3 --version
pip3 --version
git --version
```

---

# 18. Complete Setup Workflow

```bash
# Install Packages
sudo dnf install python3 python3-pip git -y

# Clone Repository
git clone https://github.com/atulkamble/postgresql-app
cd postgresql-app

# Create Virtual Environment
python3 -m venv venv

# Activate Virtual Environment
source venv/bin/activate

# Verify Versions
python --version
pip --version

# Install PostgreSQL
sudo apt install postgresql -y

# Verify PostgreSQL
postgres -V

# Connect to RDS
export RDSHOST="database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com"

psql "host=$RDSHOST port=5432 dbname=postgres user=postgres sslmode=require password=$(aws rds generate-db-auth-token --hostname $RDSHOST --port 5432 --username postgres --region us-east-1)"

# Create Database
CREATE DATABASE university;

# Create User
CREATE USER atul WITH PASSWORD 'Password@123';

# Grant Permissions
GRANT ALL PRIVILEGES ON DATABASE university TO atul;

# List Databases
\list

# List Users
\du

# Exit PostgreSQL
\q
```

## Common PostgreSQL Commands

| Task                  | Command                                                |
| --------------------- | ------------------------------------------------------ |
| PostgreSQL Version    | `postgres -V`                                          |
| Connect to PostgreSQL | `psql`                                                 |
| List Databases        | `\list`                                                |
| List Users            | `\du`                                                  |
| List Roles            | `\dg`                                                  |
| Create Database       | `CREATE DATABASE dbname;`                              |
| Create User           | `CREATE USER username WITH PASSWORD 'password';`       |
| Change Password       | `ALTER USER username WITH PASSWORD 'newpassword';`     |
| Grant Access          | `GRANT ALL PRIVILEGES ON DATABASE dbname TO username;` |
| Exit PostgreSQL       | `\q`                                                   |

This guide covers Git, Python Virtual Environment, PostgreSQL installation, AWS RDS PostgreSQL IAM authentication, database creation, user management, and privilege assignment.
