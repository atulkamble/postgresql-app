# Deploy a Python Flask App with PostgreSQL on Amazon Linux

## Architecture

```text
+-------------------+
|   User Browser    |
+---------+---------+
          |
          v
+-------------------+
| Flask Application |
| Amazon Linux EC2  |
+---------+---------+
          |
          v
+-------------------+
| PostgreSQL DB     |
| Amazon Linux EC2  |
+-------------------+
```

---

# Step 1: Launch EC2 Instances

Create two Amazon Linux EC2 instances:

| Server     | Purpose             |
| ---------- | ------------------- |
| App Server | Flask Application   |
| DB Server  | PostgreSQL Database |

Example:

| Server     | Private IP |
| ---------- | ---------- |
| App Server | 10.0.1.10  |
| DB Server  | 10.0.2.10  |

---

# Step 2: Install PostgreSQL on DB Server

SSH into DB Server:

```bash
ssh -i key.pem ec2-user@DB-Public-IP
```

Update system:

```bash
sudo dnf update -y
```

Install PostgreSQL:

```bash
sudo dnf install postgresql15-server postgresql15 -y
```

Initialize database:

```bash
sudo postgresql-setup --initdb
```

Enable and start service:

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

Verify:

```bash
sudo systemctl status postgresql
```

---

# Step 3: Configure PostgreSQL

Edit configuration:

```bash
sudo vi /var/lib/pgsql/data/postgresql.conf
```

Find:

```text
listen_addresses = 'localhost'
```

Change:

```text
listen_addresses = '*'
```

---

Edit pg_hba.conf:

```bash
sudo vi /var/lib/pgsql/data/pg_hba.conf
```

Add:

```text
host all all 10.0.0.0/16 md5
```

Restart PostgreSQL:

```bash
sudo systemctl restart postgresql
```

---

# Step 4: Create Database

Switch postgres user:

```bash
sudo -i -u postgres
```

Open PostgreSQL:

```bash
psql
```

Create database:

```sql
CREATE DATABASE university;
```

Create user:

```sql
CREATE USER atul WITH PASSWORD 'Password@123';
```

Grant permissions:

```sql
GRANT ALL PRIVILEGES ON DATABASE university TO atul;
```

Exit:

```sql
\q
```

---

# Step 5: Configure Security Group

Allow PostgreSQL Port:

| Type       | Port | Source                    |
| ---------- | ---- | ------------------------- |
| PostgreSQL | 5432 | App Server Security Group |

---

# Step 6: Install Flask App on App Server

SSH into App Server:

```bash
ssh -i key.pem ec2-user@APP-Public-IP
```

Update:

```bash
sudo dnf update -y
```

Install Python:

```bash
sudo dnf install python3 python3-pip git -y
```

Verify:

```bash
python3 --version
```

---

# Step 7: Create Application Directory

```bash
mkdir flaskapp
cd flaskapp
```

Install dependencies:

```bash
pip3 install flask psycopg2-binary
```

---

# Step 8: Create Flask Application

Create file:

```bash
vi app.py
```

Paste:

```pythonfrom flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com")
DB_NAME = os.environ.get("DB_NAME", "university")
DB_USER = os.environ.get("DB_USER", "atul")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")

@app.route('/')
def home():
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
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

# Step 9: Run Application

```bash
sudo python3 app.py
```

Output:

```text
* Running on http://0.0.0.0:80
```

---

# Step 10: Open Security Group

Allow:

| Type | Port |
| ---- | ---- |
| HTTP | 80   |

Source:

```text
0.0.0.0/0
```

---

# Step 11: Test

Open browser:

```text
http://APP-Public-IP
```

Expected Output:

```text
Connected Successfully! Total Records: 0
```

---

# Insert Sample Data

Connect PostgreSQL:

```bash
psql -U atul -d university -h localhost
```

Insert:

```sql
INSERT INTO student(name)
VALUES ('Atul'),
       ('Ravi'),
       ('Amit');
```

Check:

```sql
SELECT * FROM student;
```

---

# Production Improvements

* Use Gunicorn instead of Flask development server.
* Configure Nginx as reverse proxy.
* Store database credentials in environment variables.
* Enable SSL using Let's Encrypt.
* Use PostgreSQL on Amazon RDS instead of EC2-hosted PostgreSQL.
* Deploy application using CI/CD with [GitHub](https://github.com?utm_source=chatgpt.com) and [Azure DevOps](https://azure.microsoft.com/products/devops?utm_source=chatgpt.com).
* Enable monitoring using [Prometheus](https://prometheus.io?utm_source=chatgpt.com) and [Grafana](https://grafana.com?utm_source=chatgpt.com).

This is a complete hands-on lab suitable for AWS, Linux, Python, Flask, and PostgreSQL practice.
