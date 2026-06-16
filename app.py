from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com")
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com:5432/?Action=connect&DBUser=postgres&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAXZEFIC7NELACRMWI%2F20260616%2Fus-east-1%2Frds-db%2Faws4_request&X-Amz-Date=20260616T035059Z&X-Amz-Expires=900&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIHE5h9HyMDrfjGYVI%2FABPdlHS2MaEVvoiCAo2myqHTicAiEAx0DED1oSFDqEMZ6DlELX3TCY8p3ITmlK5DffG30otHoq3AIIbRAAGgw1MzUwMDI4Nzk5NjIiDDJQlqQwm9hsEmbuoyq5Ajwkc6tR5NSGCt9N6CknSbqzNUtxW9W6aiwQs205gKQ8FCRKoAEh9j0Z3CZRkorwMOoxHnJN8c2nVr07i%2F7ZUbvWuZ7%2FTxk9wKDSH%2FeoADW87yMCFtYlyp5YuIhXSHiSzQyva%2FRJeFcS8LWrvanLVS5whddcV9aLfI%2Bj6CKAUSN5wO7JxjBgloqAGdZoVGTH9wSsAvW8ASSRVKk4cII4%2BuRFGpSXulMLlwrsac6wrK06wQUEwKCwMmQcT46sGYRdaAEjuXZ45QP%2FOGlnDZye7tfb6UlN%2F6YYVCk6dRiCRa4zmLm57ikDoTgHRyS2mb9hbpviORRoCfvIrNgAwdhSFP9pLnIW4IQnFomIsZxXU6duM76Pe2O74mUURJcXXwHddKNNhgalb%2BTXJXJFvyY8R%2B3u4LNvbGdpOswwj%2FbC0QY6rQKmRPMT9%2BeEiGAIkjGhlTRLEEI3kzwbietSC%2FlVlWJWzsqHMNRo9H%2BWTvoNJylY0eeN2zpktjDeLSl6sLYBLDPayThzT%2B252XT4I%2FCwmDZCTVDsw%2BPglwAQf2MiuxRmHBuAjC9%2B6Gk7lxUpOc%2FwJwoBaxqc5HQqwNjZ%2BtmeXYlB76vWEUhlJ2MLxm4A1bzU3O9wT2Y71QxkK47UGqM1Mn5MqOf%2FX1RLY33%2Btb6x5wyA4yGTk1fEMSyp2SYsh4fVQlKcs1Oc5hYZZZZxTtQRrVZJjMRGwli99bjgFZTPwpj96oAr6N%2FfyBs7CvUO3A6rjGom3GhSCgULyWEcsRNgLeU6OSyOXHASGgiJJWGcDkEHpvUuXB5AI%2FcT8mS7eA4wiLZUMFhi6NoRzrPNr4bV&X-Amz-Signature=0afaa7626586409260d1320ef29e16e62da635b2bb78e88167a0f126ba6f58c7&X-Amz-SignedHeaders=host")

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
