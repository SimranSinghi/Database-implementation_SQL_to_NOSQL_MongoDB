import pymongo
from extracredit import convertJson2Xml
from export_data import get_json
def create_conn():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    # print(client.server_info())
    return client

def department(client):
    mydb = client['COMPANY']
    mycol = mydb['DEPARTMENT']
    mycol2 = mydb['RESULT_DEPARTMENT']
    result = mycol.aggregate([
        {
            '$lookup': {
                'from': 'EMPLOYEE',
                'localField': 'MANAGER_SSN',
                'foreignField': 'EMP_SSN',
                'as': 'MANAGER_LNAME'
            }
        },
        {
            '$lookup': {
                'from': 'EMPLOYEE',
                'localField': 'DNUM',
                'foreignField': 'DNUM',
                'as': 'EMP_DETAILS'
            }
        },
        {
            '$project': {
                'DNAME': 1,
                'MANAGER_LNAME.E_LNAME': 1,
                'MGR_START_DATE': 1,
                'EMP_DETAILS.E_LNAME': 1,
                'EMP_DETAILS.E_FNAME': 1,
                'EMP_DETAILS.SALARY': 1
            }
        }
    ])

    result_array = []
    for item in result:
        result_array.append(item)
        print(item)

    print("Array length  :", len(result_array))
    x = mycol2.insert_many(result_array)


def employee(client):
    mydb = client['COMPANY']
    mycol = mydb['EMPLOYEE']
    mycol2 = mydb['RESULT_EMPLOYEE']
    result = mycol.aggregate([
        {
            '$lookup': {
                'from': 'DEPARTMENT',
                'localField': 'DNUM',
                'foreignField': 'DNUM',
                'as': 'DEPARTMENT_DETAILS'
            }
        },
        {
            '$lookup': {
                'from': 'PROJECT',
                'localField': 'DNUM',
                'foreignField': 'DNUM',
                'as': 'PROJECT_DETAILS'
            }
        },
        {
            '$lookup': {
                'from': 'WORKS_ON',
                'localField': 'EMP_SSN',
                'foreignField': 'EMP_SSN',
                'as': 'PROJECT_HOURS'
            }
        },
        {
            '$project': {
                'E_FNAME': 1,
                'E_LNAME': 1,
                'DEPARTMENT_DETAILS.DNAME': 1,
                'PROJECT_DETAILS.PNAME': 1,
                'PROJECT_DETAILS.PNUM': 1,
                'PROJECT_HOURS.HOURS': 1
            }
        }
    ])
    result_array = []
    for item in result:
        result_array.append(item)
        print(item)

    print("Array length  :", len(result_array))
    x = mycol2.insert_many(result_array)

def project(client):
    mydb = client['COMPANY']
    mycol = mydb['PROJECT']
    mycol2 = mydb['RESULT_PROJECT']
    result = mycol.aggregate([
        {
            '$lookup': {
                'from': 'DEPARTMENT',
                'localField': 'DNUM',
                'foreignField': 'DNUM',
                'as': 'DEPARTMENT_DETAILS'
            }
        },
        {
            '$lookup': {
                'from': 'EMPLOYEE',
                'localField': 'DNUM',
                'foreignField': 'DNUM',
                'as': 'EMPLOYEE_DETAILS'
            }
        },
        {
            '$lookup': {
                'from': 'WORKS_ON',
                'localField': 'PNUM',
                'foreignField': 'PNUMBER',
                'as': 'PROJECT_HOURS'
            }
        },
        {
            '$project': {
                'PNAME': 1,
                'PNUM': 1,
                'DEPARTMENT_DETAILS.DNAME': 1,
                'EMPLOYEE_DETAILS.E_FNAME': 1,
                'EMPLOYEE_DETAILS.E_LNAME': 1,
                'PROJECT_HOURS.HOURS': 1
            }
        }
    ])
    #Append all the items in a Array
    result_array = []
    for item in result:
        result_array.append(item)
        print(item)
    #Length of list
    print("Array length  :", len(result_array))
    x = mycol2.insert_many(result_array)

def queries(client):
    mydb = client['COMPANY']
    mycollection1 = mydb['RESULT_DEPARTMENT']
    mycollection2 = mydb['RESULT_EMPLOYEE']
    mycollection3 = mydb['RESULT_PROJECT']
    f = open("querydocument.txt", "w")
    f.write('------------------------------------')
    f.write("DEPARTMENT QUERY:-")
    f.write('------------------------------------')
    f.write('\n')
    for i in mycollection1.find({'DNAME': "'Software'"}):
        print(i)
        f.write(str(i))
    f.write('\n')
    f.write('------------------------------------')

    f.write("EMPLOYEE QUERY:-")
    f.write('------------------------------------')
    f.write('\n')
    for i in mycollection2.find({'E_FNAME': "'Jennifer'"}, {'E_LNAME': "'wallace'"}):
        print(i)
        f.write(str(i))
    f.write('-----')
    f.write('\n')

    f.write("PROJECT QUERY:-")
    f.write('\n')
    for i in mycollection3.find({'PNUM': "1"}):
        print(i)
        f.write(str(i))
    f.close()


if __name__ == "__main__":
    # Create Connection
    conn = create_conn()

    # Creating the result collections
    department(conn)
    employee(conn)
    project(conn)
    queries(conn)

    # Export Collection as JSON FILES
    get_json(conn,'RESULT_DEPARTMENT.json','RESULT_DEPARTMENT')
    get_json(conn,'RESULT_EMPLOYEE.json','RESULT_EMPLOYEE')
    get_json(conn,'RESULT_PROJECT.json','RESULT_PROJECT')


    # close Connection
    conn.close()

    # Convert Json File to XML Files
    convertJson2Xml('JSON_FILES/RESULT_DEPARTMENT.json','RESULT_DEPARTMENT.xml')
    convertJson2Xml('JSON_FILES/RESULT_EMPLOYEE.json','RESULT_EMPLOYEE.xml')
    convertJson2Xml('JSON_FILES/RESULT_PROJECT.json','RESULT_PROJECT.xml')


    