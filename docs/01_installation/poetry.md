## Installation Environment and Packages
- Mandatory: Install **python runtime**
- Poetry: This combination of pip and venv is so common that people started combining them to save steps and avoid that source shell wizardry. One such package is Pipenv, but a newer rival called Poetry is becoming more popular. To install: `$ pip install poetry`  
- Config poetry to put venv inside the project: `$ poetry config virtualenvs.in-project true`. If not venv will be installed at: `C:\Users\<user>\AppData\Local\pypoetry\Cache\virtualenvs`
- Check `$ poetry config --list` to have <em>virtualenvs.in-project = true</em>  
- Add main packages and dev packages:
```bash
poetry add fastapi "uvicorn[standard]"
```

- Create venv:
```bash
poetry new backend
cd backend
poetry install
```
  
- Activate venv: 
  - Option 1 (recommend, stable): `$ source .venv/Scripts/activate`
  - Option 2:
  ```bash
  poetry self add poetry-plugin-shell
  poetry shell
  poetry env info
  ```
  > If poetry need to uninstall in advance: `$poetry self remove poetry-plugin-shell`

- Deactivate venv:
  - If using `$source .venv/...` : `$deactivate`
  - If using `$power shell`: `$exit` 

---

- Some important syntax

| Hành động        | Lệnh                               | Kết quả                                        |
| ---------------- | ---------------------------------- | ---------------------------------------------- |
| Tạo project mới  | `poetry new myapp`                 | Sinh `pyproject.toml` mặc định                 |
| Thêm gói         | `poetry add <package>`             | Ghi vào `[tool.poetry.dependencies]`           |
| Thêm gói dev     | `poetry add --group dev <package>` | Ghi vào `[tool.poetry.group.dev.dependencies]` |
| Gỡ gói           | `poetry remove <package>`          | Xóa khỏi file                                  |
| Cập nhật version | `poetry update <package>`          | Cập nhật version mới trong file                |
| Cài lại toàn bộ  | `poetry install`                   | Dựa trên file `poetry.lock`                    |










<!-- 
```bash
poetry add pytest mypy ruff pre-commit types-passlib coverage
poetry add --group dev pytest mypy ruff pre-commit types-passlib coverage


- Add config:
```
[tool.mypy]
strict = true # strict = true → bật toàn bộ rule nghiêm ngặt (phát hiện lỗi kiểu rất sớm)
exclude = ["venv", ".venv", "alembic"] # exclude → bỏ qua các thư mục không cần check
mypy_path = ["src"] # Nếu bạn có module đặt trong src/

[tool.ruff]
target-version = "py310"
exclude = ["alembic"]

[tool.ruff.lint]
select = [
    "E", "W", "F", "I", "B", "C4", "UP", "ARG001",
]
ignore = [
    "E501", "B008", "W191", "B904",
]
# select: bật nhóm quy tắc bạn muốn kiểm tra (E=errors, W=warnings, F=flake8, I=isort, B=bugbear…)
# ignore: tắt các rule cụ thể mà bạn không thích

[tool.ruff.lint.pyupgrade]
keep-runtime-typing = true # giữ lại kiểu gốc ngay cả khi có from __future__ import annotations

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "lf"
``` -->





