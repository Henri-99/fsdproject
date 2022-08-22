# fsdproject
Group project for Financial Systems Design

# Setup Instructions
1. Install [SQL Server 2019 Express](https://www.microsoft.com/en-gb/sql-server/sql-server-downloads) and [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
2. Run the SQL Server and connect it to Management Studio
3. [Restore](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-backup-using-ssms) the AIFMRM_ERS.bak database
4. Install Python modules using `pip install -r requirements.txt`
5. Launch backend using `flask run`
6. In a separate termnial, `cd client` and `npm install`
7. Launch frontend using `npm run serve`
