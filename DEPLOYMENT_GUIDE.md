# Deployment Guide for Bihar Swimming Association Website

## Deploying to Render

This guide provides step-by-step instructions for deploying the Bihar Swimming Association website to Render.

### Prerequisites

1. A Render account (https://render.com)
2. A PostgreSQL database on Render (already set up)
3. Your code pushed to a Git repository (GitHub, GitLab, etc.)

### Step 1: Prepare Your Project

The following files have been created/modified for Render deployment:

1. **build.sh**: Script that runs during the build process
   - Installs dependencies
   - Collects static files
   - Applies database migrations

2. **Procfile**: Defines the command to start the application
   - Uses gunicorn to serve the application

3. **requirements.txt**: Updated with necessary packages
   - gunicorn for serving the application
   - whitenoise for serving static files
   - psycopg2-binary for PostgreSQL database connection
   - python-dotenv for environment variables

4. **settings.py**: Configured for production
   - WhiteNoise middleware for static files
   - Environment variables for configuration
   - Static files configuration

5. **runtime.txt**: Specifies the Python version

6. **render.yaml**: Defines the service configuration for Render

7. **.gitignore**: Ensures sensitive files are not committed

### Step 2: Push Your Code to a Git Repository

```bash
# Initialize a Git repository (if not already done)
git init

# Add all files to the repository
git add .

# Commit the changes
git commit -m "Prepare for Render deployment"

# Add your remote repository
git remote add origin <your-repository-url>

# Push to the repository
git push -u origin main
```

### Step 3: Deploy to Render

1. Log in to your Render dashboard at https://dashboard.render.com

2. Click on "New" and select "Web Service"

3. Connect your Git repository

4. Configure the following settings:
   - **Name**: bihar-swimming-association (or your preferred name)
   - **Environment**: Python
   - **Region**: Choose the region closest to your users
   - **Branch**: main (or your preferred branch)
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn swimming_federation_bihar.wsgi`

5. Add the following environment variables:
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

### Step 4: Verify Deployment

1. Wait for the deployment to complete
2. Click on the URL provided by Render to access your application
3. Verify that all pages and functionality work as expected

### Troubleshooting

1. **Static Files Not Loading**:
   - Check that WhiteNoise is properly configured
   - Verify that `collectstatic` ran successfully during deployment

2. **Database Connection Issues**:
   - Verify database credentials in environment variables
   - Check that the database is accessible from Render

3. **Application Errors**:
   - Check the Render logs for error messages
   - Verify that all required environment variables are set

### Updating Your Application

To update your application:

1. Make changes to your code locally
2. Commit and push to your Git repository
3. Render will automatically deploy the new version

### Custom Domain (Optional)

To use a custom domain:

1. Go to your web service in the Render dashboard
2. Click on "Settings" and then "Custom Domain"
3. Follow the instructions to add your domain

### Conclusion

Your Bihar Swimming Association website should now be deployed on Render and accessible to users worldwide. If you encounter any issues, refer to the Render documentation or contact Render support.