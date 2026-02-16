## 🛠️ Alembic là gì?

<!-- ![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2ASmWmRRaMWdY9ymG5K-kfsg.png)

![Image](https://miro.medium.com/1%2ALx_Rsq76_JbOz4F4AzsllA.png)

![Image](https://www.bytebase.com/content/blog/what-is-database-migration/cover.webp)

![Image](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2022/08/23/DBBLOG-2254-image001.png) -->

<div style="display:flex; overflow-x:auto; gap:10px">
<img src="https://miro.medium.com/v2/resize%3Afit%3A1400/1%2ASmWmRRaMWdY9ymG5K-kfsg.png" alt="img0" height=224>
<img src="https://miro.medium.com/1%2ALx_Rsq76_JbOz4F4AzsllA.png" alt="img1" height=480>
<img src="https://www.kubeblogs.com/content/images/2025/06/image-3.png" alt="img2" height=480>
</div>


# 🧠 Định nghĩa đơn giản

**Alembic** là:

> 🔄 Công cụ quản lý migration (thay đổi cấu trúc database) khi dùng SQLAlchemy.

Nó giúp bạn:

* Thêm / sửa / xóa cột
* Thay đổi schema
* Version control database
* Upgrade / Downgrade database an toàn

---

# ❓ Vì sao cần Alembic?

SQLAlchemy chỉ:

```
Tạo bảng mới nếu chưa tồn tại
```

❌ Không thể:

* Thêm cột vào bảng đã có dữ liệu
* Sửa cấu trúc bảng cũ

👉 Khi ứng dụng phát triển, database cũng phải thay đổi
→ Alembic giải quyết vấn đề này.

---

# 🔄 Alembic hoạt động như thế nào?

### Ý tưởng chính:

> Database có "version" giống như Git commit.

Mỗi lần thay đổi cấu trúc:

* Tạo một **revision**
* Ghi lại thay đổi
* Có thể upgrade hoặc rollback

---

# 📁 Sau khi chạy:

```bash
alembic init alembic
```

Sẽ xuất hiện:

```
alembic.ini
alembic/
```

---

## 📄 1️⃣ alembic.ini

* File config chính
* Chứa connection string database
* Alembic đọc file này khi chạy lệnh

---

## 📂 2️⃣ alembic directory

Chứa:

* Môi trường Alembic
* Thư mục `versions/`
* Các file migration (revision)
* Script upgrade / downgrade

---

# 🧩 Revision là gì?

```bash
alembic revision -m "add phone_number column"
```

👉 Tạo một file mới trong `versions/`

Ví dụ:

```python
def upgrade():
    op.add_column("users",
        sa.Column("phone_number", sa.String(), nullable=True)
    )

def downgrade():
    op.drop_column("users", "phone_number")
```

Mỗi revision có:

* Revision ID riêng
* Hàm `upgrade()`
* Hàm `downgrade()`

---

# ⬆ Alembic Upgrade

```bash
alembic upgrade head
```

👉 Chạy migration
👉 Thực thi code trong `upgrade()`
👉 Database được cập nhật

Ví dụ:

* Thêm cột `phone_number`
* Dữ liệu cũ vẫn giữ nguyên

---

# ⬇ Alembic Downgrade

```bash
alembic downgrade -1
```

👉 Quay lại version trước
👉 Chạy `downgrade()`
👉 Xóa thay đổi vừa tạo

⚠ Nếu xóa cột → dữ liệu trong cột đó sẽ mất

---

# 📌 Ví dụ thực tế

Giả sử bảng `users` ban đầu:

| id | username |
| -- | -------- |

Sau upgrade:

| id | username | phone_number |
| -- | -------- | ------------ |

Sau downgrade:

| id | username |
| -- | -------- |

---

# 🎯 Tóm tắt cực ngắn

Alembic giúp bạn:

✔ Thay đổi database đã có dữ liệu
✔ Theo dõi version database
✔ Upgrade & rollback an toàn
✔ Phù hợp môi trường production

---

# 🔥 Các lệnh quan trọng

| Lệnh                   | Mục đích               |
| ---------------------- | ---------------------- |
| `alembic init`         | Khởi tạo               |
| `alembic revision -m`  | Tạo migration          |
| `alembic upgrade head` | Chạy migration         |
| `alembic downgrade -1` | Quay lại version trước |

---

# 🧠 So sánh dễ hiểu

| Git    | Alembic   |
| ------ | --------- |
| Commit | Revision  |
| Push   | Upgrade   |
| Revert | Downgrade |

---

Nếu bạn muốn mình:

* 🔥 Demo Alembic trong FastAPI project
* 🔥 Hướng dẫn cấu hình autogenerate
* 🔥 Giải thích cách Alembic lưu version trong DB
* 🔥 Vẽ sơ đồ workflow production chuẩn

Bạn chọn hướng mình đào sâu nhé 🚀
