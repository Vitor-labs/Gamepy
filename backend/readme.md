
# Django backend

backend logic of project, cointains: database models, api routes, data serializers, etc...



## API Docs

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
