
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

#### Show newest books information (limited by 10)

```http
GET /read_book/newest_books/
```

#### Show all books information (in order of when added in our database)

```http
GET /read_book/all_books
```

#### Get a specific book pdf file (URL of the file not the file itself)

```http
GET /read_book/pdf_file/<id>
```