# HƯỚNG DẪN CÀI MÔI TRƯỜNG PYTHON

Tài liệu này trình bày **2 cách chuẩn và chuyên nghiệp** để quản lý môi trường & dependency cho project Python:

1. **Poetry** (quản lý dependency + môi trường ảo + packaging)
2. **python -m venv** (môi trường ảo truyền thống + pip)

---

# PHẦN 1 — CÀI ĐẶT VÀ SỬ DỤNG POETRY

## 1. Poetry là gì?
Poetry là công cụ **all-in-one** cho Python:
- Tạo virtualenv
- Quản lý dependency
- Quản lý version
- Build package
- Publish package

> Tương đương: `pip + venv + setuptools + wheel + twine`

---

## 2. Cài Poetry

### Cách 1: Linux / macOS
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Cách 2: Windows (PowerShell)
- Recommend (e.g custom python path: C:\Python\Python`<version>`\Scripts)
```bash
$ pip install poetry
```
- Install if default python path: C:\Users\`<user>`\AppData\Roaming\Python\Scripts

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

---

## 3. Thêm Poetry vào PATH

### Linux/macOS
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows
```text
custom python path: C:\Python\Python<version>\Scripts
default python path: C:\Users\<User>\AppData\Roaming\Python\Scripts
```

Kiểm tra:
```bash
poetry --version
```

---

## 4. Tạo project bằng Poetry
```bash
poetry new my_project
cd my_project
```

Hoặc với project có sẵn:
```bash
poetry init
```

---

## 5. Cấu trúc project
```text
my_project/
├── pyproject.toml
├── README.md
├── my_project/
│   └── __init__.py
└── tests/
```

---

## 6. Quản lý thư viện

### Cài package
```bash
poetry add fastapi "uvicorn[standard]" sqlalchemy passlib bcrypt==4.0.1 python-multipart "python-jose[cryptography]" psycopg2-binary alembic pytest httpx pytest-asyncio
```

> passlib, bcrypt: hash password
> python-multipart: submit forms to application
> "python-jose[cryptography]": some functions to return a professional JWT back to the client
> psycopg2-binary: connection to PostgreSQL
> alembic: lightweight database migration tools for when using SQLAlchemy to alter existed database.
> pytest: testing
> httpx: a way to be able to dynamically call URLs and API endpoints automatically through a library.
> pytest-asyncio: cope with error 'Failed: async def functions are not natively supported.'.


### Cài dev dependency
```bash
poetry add pytest --group dev
```


---

## 7. Virtual Environment với Poetry

Put env inside the project (instead C:\Users\`<user>`\AppData\Local\pypoetry\Cache\virtualenvs)

```bash
poetry config virtualenvs.in-project true
```

### Kích hoạt env
```bash
poetry self add poetry-plugin-shell
poetry shell
poetry env info
```

### Chạy lệnh trong env
```bash
poetry run python main.py
```

### Deactivate env
```bash
exit
```

---

## 8. Cài dependency từ file
```bash
poetry install
```

---

## 9. Export requirements.txt (nếu cần)
```bash
poetry export -f requirements.txt --output requirements.txt
```

---

# PHẦN 2 — CÀI MÔI TRƯỜNG BẰNG python -m venv

## 1. venv là gì?
`venv` là module built-in của Python dùng để tạo **virtual environment**.

> Chỉ tạo env, không quản lý dependency nâng cao như Poetry.

---

## 2. Tạo virtual environment

### Linux/macOS
```bash
python3 -m venv venv
```

### Windows
```powershell
python -m venv venv
```

---

## 3. Kích hoạt môi trường ảo

### Linux/macOS
```bash
source venv/bin/activate
```

### Windows CMD
```cmd
venv\Scripts\activate
```

### Windows PowerShell
```powershell
venv\Scripts\Activate.ps1
```

---

## 4. Cài package
```bash
pip install requests
```

---

## 5. Lưu dependency
```bash
pip freeze > requirements.txt
```

---

## 6. Cài dependency từ file
```bash
pip install -r requirements.txt
```

---

## 7. Thoát môi trường ảo
```bash
deactivate
```

---

# SO SÁNH NHANH POETRY vs VENV

| Tiêu chí | Poetry | venv + pip |
|------|------|------|
| Tạo env | Tự động | Thủ công |
| Quản lý dependency | Rất mạnh | Cơ bản |
| Lock version | poetry.lock | requirements.txt |
| Packaging | Có | Không |
| Publish | Có | Không |
| CI/CD | Rất tốt | Trung bình |
| Microservices | Rất phù hợp | Phù hợp |
| Enterprise | Rất tốt | Trung bình |

---

# KHUYẾN NGHỊ SỬ DỤNG

### Dùng **Poetry** khi:
- Project research
- AI/ML/DL
- Microservices
- SaaS
- Project thương mại
- Team dev
- CI/CD
- Open-source

### Dùng **venv** khi:
- Script nhỏ
- Automation đơn giản
- Demo nhanh
- Học Python
- Crawl tool ngắn hạn

---

# KIẾN TRÚC CHUẨN (PRO)

```text
project/
├── app/
├── tests/
├── pyproject.toml   (Poetry)
├── poetry.lock
└── README.md
```

hoặc

```text
project/
├── src/
├── tests/
├── requirements.txt
├── venv/
└── README.md
```

---

Nếu bạn muốn, mình có thể viết thêm:
- Template project Poetry chuẩn production
- Template microservices (FastAPI + Poetry)
- Template research AI (Poetry + MLflow + Hydra)
- Template crawler (Selenium + Playwright + Poetry)
- Template Docker + Poetry


---

## TodoApp

```bash
./myproject/TodoApp (main)
$ alembic init alembic
Creating directory .\myproject\TodoApp\alembic ...  done
Creating directory .\myproject\TodoApp\alembic\versions ...  done
Generating .\myproject\TodoApp\alembic.ini ...  done
Generating .\myproject\TodoApp\alembic\env.py ...  done
Generating .\myproject\TodoApp\alembic\README ...  done
Generating .\myproject\TodoApp\alembic\script.py.mako ...  done
Please edit configuration/connection/logging settings in .\myproject\TodoApp\alembic.ini before proceeding.
(myproject-py3.13)
```

alembic revision -m "Create phone number for user column"

```bash
./FastAPI-The-Complete-Course/myproject/TodoApp (main)
$ alembic revision -m "Create phone number for user column"
Generating .\myproject\TodoApp\alembic\versions\6fa63925ef43_create_phone_number_for_user_column.py ...  done
(myproject-py3.13) 
```
edit 6fa63925ef43_create_phone_number_for_user_column.py
alembic upgrade 6fa63925ef43

```bash
./myproject/TodoApp (main)
$ alembic upgrade 6fa63925ef43
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 6fa63925ef43, Create phone number for user column
(myproject-py3.13) 
```