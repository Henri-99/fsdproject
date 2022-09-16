# fsdproject
The official GitHub repo for the INF5006S Financial Systems Design project for Group 3. This project is a financial dashboard that aims to generate useful insights and data visualisations from raw equity price data from the JSE. The dataset has been provided by the African Institute of Financial Markets and Risk Management. 

# Setup Instructions
1. Install [SQL Server 2019 Express](https://www.microsoft.com/en-gb/sql-server/sql-server-downloads) and [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
2. Run the SQL Server and connect it to Management Studio
3. [Restore](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-backup-using-ssms) the [AIFMRM_ERS.bak](https://drive.google.com/file/d/1-1pryQ54kOfKQl9ymtRMNaWRGoL7O4k3/view) database
4. Install Python modules using `pip install -r requirements.txt`
5. Launch backend using `flask run`
6. In a separate termnial, `cd client` and `npm install`
7. Launch frontend using `npm run serve`
