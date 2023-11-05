# aad64_PySpark
PySpark Data Processing
[![CI](https://github.com/nogibjj/aad64_PySpark/actions/workflows/actions.yml/badge.svg)](https://github.com/nogibjj/aad64_PySpark/actions/workflows/actions.yml)

# Summary:
This project focuses on utilizing PySpark to perform data processing tasks on a large dataset. Here, a [`Spotify dataset`](https://github.com/nogibjj/aad64_PySpark/blob/main/songs_normalize.csv) was used. The main objectives are to implement at least one Spark SQL query and one data transformation operation.

# Project Structure:
```
|-- .devcontainer/
|   |-- Dockerfile
|   |-- devcontainer.json
|-- .github/
|   |-- workflows/
|       |-- actions.yml
|-- mylib/
|   |-- lib.py
|-- .gitignore
|-- Makefile
|-- main.py
|-- report.txt
|-- requirements.txt
|-- songs_normalize.csv
|-- test_main.py
```

# Objectives: 
* [x] Use PySpark to perform data processing on a large dataset
* [x] Include at least one Spark SQL query and one data transformation

# Results:

### Result of reading the CSV file: 
<p align = "center"><img width="1647" alt="Screenshot 2023-11-05 at 12 38 42 AM" src="https://github.com/nogibjj/aad64_PySpark/assets/143753050/1bac124c-6004-4189-befc-5368565cd88c"></p>

### SparkSQL Query Result
<p align = "center"><img width="1564" alt="Screenshot 2023-11-05 at 12 38 52 AM" src="https://github.com/nogibjj/aad64_PySpark/assets/143753050/77a1a0a3-2d73-4bed-9f96-a4edad3d1459"></p>

### Transformation:
<p align = "center"><img width="1540" alt="Screenshot 2023-11-05 at 12 39 01 AM" src="https://github.com/nogibjj/aad64_PySpark/assets/143753050/728a4060-7a42-426c-937e-51c50ffb0ae8"></p>


# GitHub Actions (i.e., CI/CD Pipeline):

### Linting
<p align = "center"><img width="420" alt="image" src="https://github.com/nogibjj/aad64_PySpark/assets/143753050/aa614e1d-fc71-4668-9b71-73f161036fc0"></p>

### Formatting
<p align = "center"><img width="446" alt="image" src="https://github.com/nogibjj/aad64_PySpark/assets/143753050/a35a9eca-948c-48ca-9d61-56ef96e44154"></p>

### Testing
<p align = "center"><img width="1502" alt="Screenshot 2023-11-05 at 11 11 32 AM" src="https://github.com/nogibjj/aad64_PySpark/assets/143753050/f0fc047e-58f8-4694-b439-fe67a093ecad"></p>
