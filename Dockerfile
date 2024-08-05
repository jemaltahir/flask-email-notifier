FROM python:3.12-slim

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Change ownership of the application files
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
