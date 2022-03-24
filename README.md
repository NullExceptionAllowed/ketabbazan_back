
## API Reference

#### Sign Up

```http
POST /accounts/signup/
```

| Parameter | Description                |
| :-------- | :------------------------- |
| `nickname` |  |
| `email` | **Required**, **Unique** |
| `password` | **Required** |

#### Login

```http
POST /accounts/login/
```

| Parameter | Description                |
| :-------- | :------------------------- |
| `email_or_username` | **Required** |
| `password` | **Required** |

#### Profile

```http
GET /accounts/profile/
```

#### Logout

```http
POST /accounts/logout/
```
