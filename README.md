## backend

## git

- git init
- git commit -m "first commit"
- git branch -M main (no aplica)
- git remote add origin https://github.com/zeron-team/edu_alum_ia_be.git
- git push -u origin master

## requirements.txt
```python 
pip install flask flask-cors pymongo openai 
```

## estructura
```text
proyecto_asistente_alumno/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── api.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── thesaurus.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── openai_service.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── explanation_controller.py
├── config.py
├── run.py
├── requirements.txt
```