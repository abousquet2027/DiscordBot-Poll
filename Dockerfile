# Austin Bousquet
# starting python
FROM python:3

# Austin Bousquet
# sets two enviornment variables
# first variable stops python from creating cache files
# the second variable will print python logs from the container immediately
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Austin Bousquet
    # sets the working directory
WORKDIR /app

# Austin Bousquet
# copies the requirments.txt file to install dependencies for the container    
COPY requirements.txt .

# Austin Bousquet
# installs the dependencies from the requirments.txt
RUN pip install --no-cache-dir -r requirements.txt

# Austin Bousquet
# copies the rest of the files but will ignore .env and dockerignore files into the container
COPY . .

# Austin Bousquet
# Runs python and the script
CMD ["python", "Austin - William - Sebastian - DiscordBot.py"]