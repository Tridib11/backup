#!/bin/bash

add_user()
{
    USER=$1
    PASS=$2

    useradd -m -p $PASS $USER && echo "Successfully added user"
}

add_user omraj omraj14

#the time u will run it run it with superuser (sudo su)
#useradd is a command in Linux and Unix operating systems used to create a new user account.

#The -m option specifies that a home directory should be created for the user. This 
#is typically where the user's files and personal settings will be stored.

#The -p option is used to specify the password for the user. 
#However, it is not recommended to use this option to set the password as 
#the password will be visible in the command history and it is better to use the passwd command to set the password securely.


#In general, it is recommended to create user accounts using the 
#useradd command with the appropriate options, and then use the passwd command to set the password for the user.
