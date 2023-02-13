
# Django backend

backend logic of project, cointains: database models, api routes, data serializers, etc...



## API Docs
---
### Inventory app routes 

#### Returs all itens from games tale

```http
  GET | POST /games
```

| Parâmetro | Tipo | Descrição |
| :-------- | :--- | :-------- |

#### Return a single game

```http
  GET | PUT | PATCH | DELETE /games/${id}
```

| Parâmetro | Tipo  | Descrição                          |
| :-------- | :---- | :--------------------------------- |
| `id`      | `int` | **required**. id of game to return |

#### Return games by genre tag

```http
  GET /games/${genre}
```

| Parâmetro | Tipo  | Descrição                                    |
| :-------- | :---- | :------------------------------------------- |
| `genre`   | `str` | **required**. tag of lits of games to return |

#### Return games by score

```http
  GET /games/${score}
```

| Parâmetro | Tipo  | Descrição                                          |
| :-------- | :---- | :------------------------------------------------- |
| `score`   | `int` | **required**. return games above or equal to score |

#### Return games by score

```http
  GET /games/${price}
```

| Parâmetro | Tipo  | Descrição                                         |
| :-------- | :---- | :------------------------------------------------ |
| `price`   | `int` | **required**. return games less or equal to price |
----

### Authentication app routes

#### API endpoint that allows users to be viewed or edited.

```http
  GET | POST /auth/
```

#### API endpoint that allows user to login.
    
```http
  POST /auth/login/
```

####  API endpoint that allows user to logout and clean tokens.
    
```http
  POST /auth/logout/
```

####  API endpoint that sends users an email to be varified.
    
```http
  POST /auth/registe/
```

####  API endpoint that verifies user tokens and validateds him.
    
```http
  GET /auth/email-verify/
```
  
####  API endpoint that user built-in TokenRefreshView of DRF-simple-jwt
    
```http
  POST /auth/token/refresh/
```

####  API endpoint that allows user to reques an reset password email.
    
```http
  POST /auth/request-reset-email/
```

####  API endpoint that allows user to check his tokens.
    
```http
  GET /auth/password-reset/<uidb64>/<token>/
```

| Parâmetro | Tipo  | Descrição                           |
| :-------- | :---- | :---------------------------------- |
| `uidb64`  | `str` | **required**. base64 encoded string |
| `token`   | `str` | **required**. auth access jwt       |

####  API endpoint that allows user to check his tokens.
    
```http
  GET /auth/password-reset-confirm
```
####  API endpoint that confirms if user changed his password.
    
```http
  PATCH /auth/password-reset-confirm
```

| Parâmetro | Tipo  | Descrição                                    |
| :-------- | :---- | :------------------------------------------- |
| `genre`   | `str` | **required**. tag of lits of games to return |
