# Back-end

## Todo
- Create Django Rest Proj/App
- Postgres DB
- Models
- FE Endpoints
- Deploy with Heroku
- CRUD Endpoints
- Create fixtures from given quizzes
- Send emails after post to Quiz Taker
  - [Create default email template](./email.txt)
    - Score
    - Questions
      - Correct Answers
      - Info Link
- Admin side
- Download CSV file (by Event)
  - Email
  - First Name
  - Last Name
  - Event Name
  - Event Date

## FE Endpoints

### Active Event Quiz (READ)
```json
{
  "event_id": "int",
  "quiz_id": "int",
  "child_mode": "bool",
  "timer": "int (min)", 
  "questions": [
    {
      "question": "varchar",
      "question_id": "int",
      "value": "int",
      "answers": [
        {
          "answer": "varchar",
          "is_correct": "bool",
        }
      ]
    }
  ]
}
```

### Quiz Taker (POST)

```json
{
  "email": "email/null",
  "fname": "varchar/null",
  "lname": "varchar/null",
  "initials": "varchar(3)",
  "event": "int",
  "quiz_bank": "int",
  "score": "int",
  "zip_code": "varchar(5)"
}
```

### Leaderboard (READ)
  - Return the top 5 of the active event
```json
[
  {
    "intials": "varchar(3)",
    "score": "int"
  }
]
```

## Admin

- Make sure only one event is active (Create & Update)
  - Add a note in admin on create and update
