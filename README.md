# Game Boosters

![Docker Build Status](https://github.com/maddboost/game-boosters-main/actions/workflows/docker-build.yml/badge.svg)

A Django-based game boosting platform.

## Docker

The application is available as a Docker image on Docker Hub:

```bash
docker pull madboost/game-boosters:latest
```

### Running with Docker

```bash
docker run -d -p 8000:8000 madboost/game-boosters:latest
```

## Development

1. Clone the repository:
```bash
git clone https://github.com/maddboost/game-boosters-main.git
cd game-boosters-main
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

## Security

- The project uses Trivy for security scanning
- Dependencies are regularly updated for security patches
- Automated builds ensure consistent deployment