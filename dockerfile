
FROM python
COPY . /opt/app
WORKDIR /opt/app
RUN pip install requests
RUN pip install Flask
RUN pip install selenium
RUN pip install webdriver-manager

CMD ["python","main_game.py"]