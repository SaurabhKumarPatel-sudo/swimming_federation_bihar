# Bihar Swimming Association Website

## Environment Variables

This project uses environment variables for configuration. These are stored in a `.env` file in the root directory of the project.

### Setting Up Environment Variables

1. Create a `.env` file in the root directory of the project (if not already present)
2. Add the following variables to the file:

```
# Django settings
DEBUG=True  # Set to False in production
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=127.0.0.1,localhost  # Add your domain in production

# Database settings
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432

# Static and media files
STATIC_URL=/static/
MEDIA_URL=/media/
```

### Adding New Environment Variables

1. Add the variable to your `.env` file
2. In `settings.py`, access the variable using `os.environ.get('VARIABLE_NAME', 'default_value')`

## Deployment to Render

This project is configured for deployment on Render. Follow these steps to deploy:

### Prerequisites

1. A Render account (https://render.com)
2. A PostgreSQL database on Render (already set up)
3. Your code pushed to a Git repository (GitHub, GitLab, etc.)

### Deployment Steps

1. Log in to your Render dashboard
2. Click on "New" and select "Web Service"
3. Connect your Git repository
4. Configure the following settings:
   - **Name**: Choose a name for your service
   - **Environment**: Python
   - **Region**: Choose the region closest to your users
   - **Branch**: main (or your preferred branch)
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn swimming_federation_bihar.wsgi`

5. Add the following environment variables in the Render dashboard:
   - `DEBUG`: False
   - `SECRET_KEY`: Generate a new secure key
   - `ALLOWED_HOSTS`: your-app.onrender.com
   - `DB_ENGINE`: django.db.backends.postgresql
   - `DB_NAME`: Your database name
   - `DB_USER`: Your database user
   - `DB_PASSWORD`: Your database password
   - `DB_HOST`: Your database host
   - `DB_PORT`: 5432

6. Click "Create Web Service"

### Files for Render Deployment

The following files have been created/modified for Render deployment:

1. **build.sh**: Script that runs during the build process
2. **Procfile**: Defines the command to start the application
3. **requirements.txt**: Updated with gunicorn and whitenoise
4. **settings.py**: Configured for production with WhiteNoise for static files

### Security Note

Never commit your `.env` file to version control. It contains sensitive information like database credentials and secret keys. Instead, set these values as environment variables in the Render dashboard.