FROM python:3.11

RUN pip install numpy pandas scipy scikit-learn flask

COPY . /app
ENTRYPOINT ["python"]
CMD ["main.py"]