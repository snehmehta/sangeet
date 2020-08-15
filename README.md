# Music Managment - Sangeet 

### Try our already Deployed on Heroku
```
https://sangeett.herokuapp.com/index
```


### Installing

A step by step series of examples that tell you how to get a development env running

Virtual ENV ( optional )

```
python -m venv venv
```
```
source venv\script\activate
```
Depending upon your OS, for windows ( remove source )

Requirements installation

```
pip install -r requirements.txt
```

Setting flask app

```
set FLASK_APP=music.py
```
set or export (mac | linux) depending upon your os

Flask database setup

```
flask db upgrade
```

Running

```
flask run
```


## Security (With Solution)
### csrf 
- Adding hidden token

### password hashing
- Saving only hash of user's password

### xss
- Rejecting all files expect mp3.

## Non functional Requirement
### Duplication 
- Users can store same song only once
- Another user can store that song on their playlist 

## UX
### Pagination
- 5 songs per page  (Can be any number)

## Scalability
### Database
- Using flask migrate with SqlAlchmey 

