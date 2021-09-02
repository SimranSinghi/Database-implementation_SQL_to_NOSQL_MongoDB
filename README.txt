
The input to your program will be data files in flat relational format (text files in .csv format - comma separated values) for the COMPANY database from the textbook. The schemas for this data are the same as for the COMPANY database in the textbook in chapters 5 and 6 for the tables DEPARTMENT, EMPLOYEE, PROJECT, and WORKS_ON. You will need to design three document collections (complex objects) corresponding to this data and store each as a document collection in MongoDB:

 

The PROJECTS document collection will store a collection of PROJECT documents. Each PROJECT document will include the following data about each PROJECT object (document): PNAME, PNUMBER, DNAME (for the controlling DEPARTMENT), and a collection of the workers (EMPLOYEES) who work on the project. This will be nested within the PROJECT object (document) and will include for each worker: EMP_LNAME, EMP_FNAME, HOURS.
The EMPLOYEES document collection will store a collection of EMPLOYEE documents. Each EMPLOYEE document will include the following data about each EMPLOYEE object (document): EMP_LNAME, EMP_FNAME, DNAME (department where the employee works), and a collection of the projects that the employee works on. This will be nested within the EMPLOYEE object (document) and will include for each project: PNAME, PNUMBER, HOURS.
The DEPARTMENTS document collection will store a collection of DEPARTMENT documents. Each DEPARTMENT document will include the following data about each DEPARTMENT object (document): DNAME, MANAGER_LNAME (the last name of the employee who manages the department), MGR_START_DATE, and a collection of the employees who work for that department. This will be nested within the DEPARTMENT object (document) and will include for each employee: E_LNAME, E_FNAME, SALARY.
 

HOW TO RUN THE PROGRAM:

-> Download VSCODE and MongoDB
-> Create database named COMPANY in Mongo DB Compass
-> Create collections named EMPLOYEE, DEPARTMENT, PROJECT and WORKS_ON
-> Upload the csv files in EMPLOYEE, DEPARTMENT, PROJECT and WORKS_ON collection one by one the mongo db compass
-> Set up connection to the local host:27017 in Mongo DB Compass
-> please see the requirement.txt for any package installation
-> Run main.py using the command "python main.py" or else you can click the play button above to run the program
-> Go to Mongo DB compass to see the Result files by clicking refresh button
-> Also, A "querydocument" will be generated. it contains the result of queries fired in the queries() function.

NOTE: PLease delete the results generated in MongoDB for executing the program as it may cause errors

EXTRA CREDIT:
-> JSON FILES and XML FILES FOLDERS will be created. 

