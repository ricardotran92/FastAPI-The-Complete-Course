## 🔐 JSON Web Token (JWT) là gì?

<!-- ![Image](https://fusionauth.io/img/shared/json-web-token.png)

![Image](https://media2.dev.to/dynamic/image/width%3D1600%2Cheight%3D900%2Cfit%3Dcover%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8wiw2dbjerzq6br66qv8.png)

![Image](https://mintlify.s3.us-west-1.amazonaws.com/auth0/docs/images/cdy7uua7fh8z/5U3Azt2AReuNzNuQqkRs5/9629ab9924a0212b74bee0b8fa88c295/legacy-app-auth-5.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2Ayw5uOmNXgNhfs5na) -->

<div style="display:flex; overflow-x: auto; gap: 10px;">
<img src = "https://fusionauth.io/img/shared/json-web-token.png" alt="img0" height=480>
<img src="https://media2.dev.to/dynamic/image/width%3D1600%2Cheight%3D900%2Cfit%3Dcover%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8wiw2dbjerzq6br66qv8.png" alt= "img1" height=480>
<img src="https://mintlify.s3.us-west-1.amazonaws.com/auth0/docs/images/cdy7uua7fh8z/5U3Azt2AReuNzNuQqkRs5/9629ab9924a0212b74bee0b8fa88c295/legacy-app-auth-5.png" alt="img2" height=480>
<img src="https://miro.medium.com/v2/resize%3Afit%3A1400/0%2Ayw5uOmNXgNhfs5na" alt="img3" height=480>
</div>


### 1️⃣ JWT là gì?

**JSON Web Token (JWT)** là một **chuỗi ký tự đặc biệt** dùng để **truyền thông tin an toàn giữa Client và Server** dưới dạng **JSON object**.

👉 Nó thường được dùng trong **Authentication (xác thực đăng nhập)** và **Authorization (phân quyền)**.

Điểm quan trọng:

* JWT có thể được **ký số (digitally signed)**.
* Nếu ai đó sửa nội dung token → server sẽ phát hiện ngay.
* Server không cần lưu session (stateless).

---

## 🧱 Cấu trúc JWT

Một JWT gồm **3 phần**, ngăn cách bởi dấu chấm (`.`):

```
aaaaa.bbbbb.ccccc
  (a)   (b)   (c)
```

| Phần | Tên       | Chức năng               |
| ---- | --------- | ----------------------- |
| (a)  | Header    | Thông tin thuật toán ký |
| (b)  | Payload   | Dữ liệu (claims)        |
| (c)  | Signature | Chữ ký bảo mật          |

---

## 🧩 1. JWT Header (a)

Header thường gồm:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

| Key   | Ý nghĩa                          |
| ----- | -------------------------------- |
| `alg` | Thuật toán ký (VD: HS256, RS256) |
| `typ` | Loại token (JWT)                 |

➡ Sau đó header được **mã hóa Base64**.

---

## 📦 2. JWT Payload (b)

Payload chứa **data (claims)**.

Có 3 loại claims:

### 🔹 Registered Claims (chuẩn)

Ví dụ:

* `iss` (issuer)
* `exp` (expiration time)
* `sub` (subject)

### 🔹 Public Claims

Tự định nghĩa nhưng phải tránh trùng tên.

### 🔹 Private Claims

Dữ liệu riêng giữa server và client.
Ví dụ:

```json
{
  "userId": 123,
  "role": "admin"
}
```

➡ Payload cũng được **mã hóa Base64**.

⚠ Lưu ý:
Base64 **KHÔNG phải mã hóa bảo mật** → ai cũng decode được.
Không nên để mật khẩu trong payload.

---

## 🔏 3. JWT Signature (c)

Signature được tạo bằng:

```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```

Trong đó:

* `secret` chỉ có server biết.
* Nếu payload bị sửa → signature sẽ sai → token invalid.

---

## 🔄 JWT hoạt động như thế nào?

### Bước 1: User đăng nhập

* Server kiểm tra username/password.
* Nếu đúng → tạo JWT gửi về client.

### Bước 2: Client gửi request

* Gửi JWT trong HTTP Header:

```
Authorization: Bearer <token>
```

### Bước 3: Server kiểm tra

* Xác minh chữ ký.
* Nếu hợp lệ → cho phép truy cập.

---

## 🎯 Tại sao JWT phổ biến?

✅ Không cần lưu session
✅ Phù hợp hệ thống Microservices
✅ Dễ mở rộng
✅ Tốc độ nhanh
✅ Cross-domain friendly

---

## 🧠 Tóm tắt siêu ngắn

JWT = **Header + Payload + Signature**

| Thành phần | Vai trò       |
| ---------- | ------------- |
| Header     | Thuật toán ký |
| Payload    | Dữ liệu       |
| Signature  | Chống sửa đổi |

👉 JWT giúp server biết:

* Token có hợp lệ không?
* Có bị chỉnh sửa không?
* Có hết hạn chưa?

---

Nếu bạn muốn, mình có thể:

* Vẽ lại 1 infographic cực clean dạng 1 slide
* Hoặc giải thích JWT theo kiểu "so sánh với Session truyền thống"
* Hoặc demo code JWT bằng Python / NodeJS 🚀

<div style="display:flex; overflow-x: auto; gap:10px">
<img src="https://substackcdn.com/image/fetch/f_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25af8b79-f58d-4b9c-aeaa-b6ffb8b93f39_1280x1608.gif" alt="img0" height=1080>
<img src="https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AZ9oRUYzXehjvDlrWwpCtFQ.png" alt="img1" height=480>
</div>