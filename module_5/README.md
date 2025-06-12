# Module 3 - Running the Flask Application

This guide will help you set up and run the Flask web application in the `module_3` folder.

## Prerequisites

- PostgreSQL installed and running

## 1. Set Up PostgreSQL

1. Install PostgreSQL from https://www.postgresql.org/download/
2. Add PostgreSQL's `bin` directory to your PATH (see instructions below).
3. Open PowerShell and run:
   ```powershell
   psql -U postgres
   ```
   - Enter your password when prompted.
4. Create a database:
   ```sql
   CREATE DATABASE mydatabase;
   ```
5. (Optional) Create a user and grant privileges if needed.

## 2. Set Up the Python Environment
   ```
1. Install required Python packages:
   ```powershell
   pip install -r requirements.txt
   ```

## 3. Configure Database Connection

- Edit `load_data.py` or any config file to ensure your PostgreSQL connection parameters (host, dbname, user, password) are correct.

## 4. Run the Application

In the `module_3` directory, run:
```powershell
python run.py
```

- The app will start on `http://0.0.0.0:8080/`.
- Open this address in your browser to view the site.

## 5. Troubleshooting

- If you get `psql : The term 'psql' is not recognized...`, add PostgreSQL's `bin` directory to your PATH:
  ```powershell
  [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\PostgreSQL\16\bin", "User")
  ```
  - Replace `16` with your installed version if different.
  - Restart PowerShell after updating PATH.

- Ensure PostgreSQL is running and accessible.
- Check your database credentials if you get connection errors.

## 6. Stopping the App

- Press `Ctrl+C` in the terminal to stop the Flask server.

Readme generated with AI