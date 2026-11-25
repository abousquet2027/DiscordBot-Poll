# starts a python image
FROM python:3.12-slim

# Forces the python logs to be in Docker
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# sets the working directory for the image
WORKDIR /app

# copy dependencies from requirements.txt and installs them
COPY requirements.txt .
RUN pip install -r requirements.txt

# copies the remainder of the bots files
COPY . .

# starts the bot
CMD ["python", "test.bot.py"]
