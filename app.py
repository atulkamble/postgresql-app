from flask import Flask, request, redirect, url_for, render_template_string
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com")
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "database-1-instance-1.c3iuq8u6iyy3.us-east-1.rds.amazonaws.com:5432/?Action=connect&DBUser=postgres&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAXZEFIC7NELACRMWI%2F20260616%2Fus-east-1%2Frds-db%2Faws4_request&X-Amz-Date=20260616T035059Z&X-Amz-Expires=900&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIHE5h9HyMDrfjGYVI%2FABPdlHS2MaEVvoiCAo2myqHTicAiEAx0DED1oSFDqEMZ6DlELX3TCY8p3ITmlK5DffG30otHoq3AIIbRAAGgw1MzUwMDI4Nzk5NjIiDDJQlqQwm9hsEmbuoyq5Ajwkc6tR5NSGCt9N6CknSbqzNUtxW9W6aiwQs205gKQ8FCRKoAEh9j0Z3CZRkorwMOoxHnJN8c2nVr07i%2F7ZUbvWuZ7%2FTxk9wKDSH%2FeoADW87yMCFtYlyp5YuIhXSHiSzQyva%2FRJeFcS8LWrvanLVS5whddcV9aLfI%2Bj6CKAUSN5wO7JxjBgloqAGdZoVGTH9wSsAvW8ASSRVKk4cII4%2BuRFGpSXulMLlwrsac6wrK06wQUEwKCwMmQcT46sGYRdaAEjuXZ45QP%2FOGlnDZye7tfb6UlN%2F6YYVCk6dRiCRa4zmLm57ikDoTgHRyS2mb9hbpviORRoCfvIrNgAwdhSFP9pLnIW4IQnFomIsZxXU6duM76Pe2O74mUURJcXXwHddKNNhgalb%2BTXJXJFvyY8R%2B3u4LNvbGdpOswwj%2FbC0QY6rQKmRPMT9%2BeEiGAIkjGhlTRLEEI3kzwbietSC%2FlVlWJWzsqHMNRo9H%2BWTvoNJylY0eeN2zpktjDeLSl6sLYBLDPayThzT%2B252XT4I%2FCwmDZCTVDsw%2BPglwAQf2MiuxRmHBuAjC9%2B6Gk7lxUpOc%2FwJwoBaxqc5HQqwNjZ%2BtmeXYlB76vWEUhlJ2MLxm4A1bzU3O9wT2Y71QxkK47UGqM1Mn5MqOf%2FX1RLY33%2Btb6x5wyA4yGTk1fEMSyp2SYsh4fVQlKcs1Oc5hYZZZZxTtQRrVZJjMRGwli99bjgFZTPwpj96oAr6N%2FfyBs7CvUO3A6rjGom3GhSCgULyWEcsRNgLeU6OSyOXHASGgiJJWGcDkEHpvUuXB5AI%2FcT8mS7eA4wiLZUMFhi6NoRzrPNr4bV&X-Amz-Signature=0afaa7626586409260d1320ef29e16e62da635b2bb78e88167a0f126ba6f58c7&X-Amz-SignedHeaders=host")

BASE_STYLE = """
<style>
  body { font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; background: #f5f5f5; }
  h1 { color: #333; }
  table { width: 100%; border-collapse: collapse; background: #fff; }
  th, td { padding: 10px 14px; border: 1px solid #ddd; text-align: left; }
  th { background: #4a90d9; color: #fff; }
  tr:nth-child(even) { background: #f9f9f9; }
  a { color: #4a90d9; text-decoration: none; margin-right: 8px; }
  a:hover { text-decoration: underline; }
  .btn { display: inline-block; padding: 8px 14px; border-radius: 4px; cursor: pointer; font-size: 14px; border: none; }
  .btn-primary { background: #4a90d9; color: #fff; }
  .btn-danger { background: #e74c3c; color: #fff; }
  .btn-success { background: #27ae60; color: #fff; }
  input[type=text] { padding: 8px; width: 100%; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
  .form-group { margin-bottom: 14px; }
  label { display: block; margin-bottom: 4px; font-weight: bold; }
  .alert { padding: 10px; border-radius: 4px; margin-bottom: 14px; }
  .alert-error { background: #fdecea; color: #c0392b; border: 1px solid #e74c3c; }
</style>
"""

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode='require'
    )

def init_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            );
        """)
        conn.commit()


@app.route('/')
def home():
    conn = None
    try:
        conn = get_conn()
        init_db(conn)
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM student;")
            count = cur.fetchone()[0]
        return render_template_string(BASE_STYLE + """
            <h1>Student Records</h1>
            <p>Connected successfully! Total records: <strong>{{ count }}</strong></p>
            <a href="{{ url_for('list_students') }}" class="btn btn-primary">View All Students</a>
            &nbsp;
            <a href="{{ url_for('add_student') }}" class="btn btn-success">Add Student</a>
        """, count=count)
    except psycopg2.OperationalError as e:
        return render_template_string(BASE_STYLE + '<div class="alert alert-error">Database connection failed: {{ e }}</div>', e=str(e)), 500
    except Exception as e:
        return render_template_string(BASE_STYLE + '<div class="alert alert-error">An error occurred: {{ e }}</div>', e=str(e)), 500
    finally:
        if conn:
            conn.close()


@app.route('/students')
def list_students():
    conn = None
    try:
        conn = get_conn()
        init_db(conn)
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM student ORDER BY id;")
            students = cur.fetchall()
        return render_template_string(BASE_STYLE + """
            <h1>All Students</h1>
            <a href="{{ url_for('add_student') }}" class="btn btn-success" style="margin-bottom:16px;display:inline-block;">+ Add Student</a>
            {% if students %}
            <table>
              <thead><tr><th>ID</th><th>Name</th><th>Actions</th></tr></thead>
              <tbody>
                {% for id, name in students %}
                <tr>
                  <td>{{ id }}</td>
                  <td>{{ name }}</td>
                  <td>
                    <a href="{{ url_for('edit_student', student_id=id) }}" class="btn btn-primary">Edit</a>
                    <form method="post" action="{{ url_for('delete_student', student_id=id) }}"
                          style="display:inline"
                          onsubmit="return confirm('Delete student {{ name }}?')">
                      <button type="submit" class="btn btn-danger">Delete</button>
                    </form>
                  </td>
                </tr>
                {% endfor %}
              </tbody>
            </table>
            {% else %}
            <p>No students found. <a href="{{ url_for('add_student') }}">Add one.</a></p>
            {% endif %}
            <br><a href="{{ url_for('home') }}">← Back to Home</a>
        """, students=students)
    except Exception as e:
        return render_template_string(BASE_STYLE + '<div class="alert alert-error">{{ e }}</div>', e=str(e)), 500
    finally:
        if conn:
            conn.close()


@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    error = None
    conn = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if not name:
            error = 'Name is required.'
        else:
            try:
                conn = get_conn()
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO student (name) VALUES (%s);", (name,))
                conn.commit()
                return redirect(url_for('list_students'))
            except Exception as e:
                error = str(e)
            finally:
                if conn:
                    conn.close()
    return render_template_string(BASE_STYLE + """
        <h1>Add Student</h1>
        {% if error %}<div class="alert alert-error">{{ error }}</div>{% endif %}
        <form method="post">
          <div class="form-group">
            <label for="name">Student Name</label>
            <input type="text" id="name" name="name" placeholder="Enter name" required>
          </div>
          <button type="submit" class="btn btn-success">Add Student</button>
          &nbsp;<a href="{{ url_for('list_students') }}">Cancel</a>
        </form>
    """, error=error)


@app.route('/students/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    error = None
    conn = None
    try:
        conn = get_conn()
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            if not name:
                error = 'Name is required.'
            else:
                with conn.cursor() as cur:
                    cur.execute("UPDATE student SET name=%s WHERE id=%s;", (name, student_id))
                conn.commit()
                return redirect(url_for('list_students'))

        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM student WHERE id=%s;", (student_id,))
            student = cur.fetchone()

        if not student:
            return render_template_string(BASE_STYLE + '<div class="alert alert-error">Student not found.</div><a href="{{ url_for(\'list_students\') }}">← Back</a>'), 404

        return render_template_string(BASE_STYLE + """
            <h1>Edit Student</h1>
            {% if error %}<div class="alert alert-error">{{ error }}</div>{% endif %}
            <form method="post">
              <div class="form-group">
                <label for="name">Student Name</label>
                <input type="text" id="name" name="name" value="{{ name }}" required>
              </div>
              <button type="submit" class="btn btn-primary">Save Changes</button>
              &nbsp;<a href="{{ url_for('list_students') }}">Cancel</a>
            </form>
        """, name=student[1], error=error)
    except Exception as e:
        return render_template_string(BASE_STYLE + '<div class="alert alert-error">{{ e }}</div>', e=str(e)), 500
    finally:
        if conn:
            conn.close()


@app.route('/students/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM student WHERE id=%s;", (student_id,))
        conn.commit()
        return redirect(url_for('list_students'))
    except Exception as e:
        return render_template_string(BASE_STYLE + '<div class="alert alert-error">{{ e }}</div><a href="{{ url_for(\'list_students\') }}">← Back</a>', e=str(e)), 500
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
