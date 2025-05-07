# Use a slim Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy your project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your game
CMD ["python", "game.py"]
