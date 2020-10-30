# Back-End

## Todo
- Create fixtures from given quizzes
- Send emails after post to Quiz Taker
  - [Create default email template](./email.txt)
    - Score
    - Questions
      - Correct Answers
      - Info Link

## [How to deploy API to Heroku](./heroku_ins.md)

## FE Endpoints    

### [Postman Link](https://documenter.getpostman.com/view/10119276/TVYGdyQr)

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
