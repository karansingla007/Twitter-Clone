  # Date: 16 Oct 2022

from sqlite.sqlite_helper import SqliteHelper

sqliteHelperObj = SqliteHelper.instance()


def createTables():
    # create user table
    createUserTableQuery = '''Create Table user(
        user_id varchar(255) not null PRIMARY KEY, 
        name varchar(255) not null, 
        user_name varchar(255) not null,
        bio varchar(255),
        created_at datetime default current_timestamp
        )'''
    print(createUserTableQuery)
    sqliteHelperObj.create_table(createUserTableQuery)

    # create userFollower table
    createUserFollowTableQuery = '''Create Table userFollower(
                user_id varchar(255) not null, 
                follower_id varchar(255) not null,
                FOREIGN KEY (user_id) REFERENCES user(user_id),
                FOREIGN KEY (follower_id) REFERENCES user(user_id)
                )'''
    print(createUserFollowTableQuery)
    sqliteHelperObj.create_table(createUserFollowTableQuery)

    # create userFollowing table
    createUserFollowingTableQuery = '''Create Table userFollowing(
                user_id varchar(255) not null, 
                following_id varchar(255) not null,
                FOREIGN KEY (following_id) REFERENCES user(user_id),
                FOREIGN KEY (user_id) REFERENCES user(user_id)
                )'''
    print(createUserFollowingTableQuery)
    sqliteHelperObj.create_table(createUserFollowingTableQuery)

    # create userTweets table
    createUserTweetsTableQuery = '''Create Table userTweets(
                tweet_id int AUTO_INCREMENT PRIMARY KEY,
                user_id varchar(255) not null, 
                created_at datetime default current_timestamp,
                title varchar(255) not null,
                description varchar(255) not null,
                FOREIGN KEY (user_id) REFERENCES user(user_id)
                )'''
    print(createUserTweetsTableQuery)
    sqliteHelperObj.create_table(createUserTweetsTableQuery)

    # create userLikes table
    createUserLikesTableQuery = '''Create Table userLikes(
                user_id varchar(255) not null,
                tweet_id int not null,
                status int not null,
                created_at datetime default current_timestamp,
                FOREIGN KEY (user_id) REFERENCES user(user_id),
                FOREIGN KEY (tweet_id) REFERENCES userTweets(tweet_id)
                )'''
    print(createUserLikesTableQuery)
    sqliteHelperObj.create_table(createUserLikesTableQuery)


def createDataBase():
    sqliteHelperObj.create_database()
    sqliteHelperObj.use_database_query()


if __name__ == "__main__":
    createDataBase()
    createTables()
