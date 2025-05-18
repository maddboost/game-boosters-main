# Build stage
FROM python:3.11-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and switch to non-root user
RUN useradd --create-home appuser
WORKDIR /app
USER appuser

# Install Python dependencies
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --user --no-warn-script-location -r requirements.txt

# Final stage
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:${PATH}"

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    netcat-openbsd \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create and switch to non-root user
RUN useradd --create-home appuser
WORKDIR /app
USER appuser

# Copy Python packages from builder
COPY --from=builder --chown=appuser:appuser /home/appuser/.local /home/appuser/.local

# Copy application code
COPY --chown=appuser:appuser . .

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD nc -z localhost 8000 || exit 1

# Expose port
EXPOSE 8000

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
