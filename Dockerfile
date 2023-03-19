#Dockerfile, Image, Container
From python:3.11.2

ADD algo.py .

RUN pip install requests beautifulsoup4

CMD ["python", "algo.py","Mango","Seed"] && bash
#donot exit after running the comman
