

from sqlite.sqlite_helper import SqliteHelper
from twitter_api.api_client import fetchTwitterUserDetailByUserName

sqliteHelperObj = SqliteHelper()

def getAndStoreUserDetail():
    json_response = fetchTwitterUserDetailByUserName("usernames=karansinglaOO7,saurabhs679,karafrenor,kartikryder,thegambhirjr7,sdrth,karannagpal96,anshulgoel02,CAPalakSingla2,theguywithideas")
    # print(json_response)
    for x in json_response['data']:
        insertUserDetailQuery = '''Insert into user(user_id, name, user_name, bio) values (%s, %s, %s, %s)'''%("'"+x['id']+"'","'"+x['name']+"'", "'"+x['username']+"'", "'"+x['description']+"'")
        sqliteHelperObj.executeInsertQuery(insertUserDetailQuery)



def main():
    sqliteHelperObj.useDatabaseQuery()
    # getAndStoreUserDetail()
    query = 'select * from user'
    sqliteHelperObj.executeQuery(query)


if __name__ == "__main__":
    main()