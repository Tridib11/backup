
#!/bin/bash
#This is known as a "shebang" line, which specifies the interpreter to use for executing the script. In this case, it specifies
# that the script should be executed using the Bash shell.
src_dir=/home/tridib/shellscripting
target_dir=/home/tridib/Documents/Backups
#These lines declare two variables: src_dir and target_dir. src_dir is set to the path of the directory to be backed up, 
#and target_dir is set to the path of the directory where the backup will be stored.
current_timestamp=$(date "+%Y-%m-%d-%H-%M-%S")
#This line uses the date command to generate a timestamp in the format "YYYY-MM-DD-HH-MM-SS". The $(...) syntax is 
#used to capture the output of the date command and assign it to the current_timestamp variable.
backup_file=$target_dir/$current_timestamp.tgz
#This line declares a variable named backup_file and assigns it a value.
#The value is a combination of target_dir, the current timestamp generated earlier, and the file extension ".tgz".
#This creates a backup filename that includes the current timestamp and ends with a ".tgz" extension.
echo "Taking backup on $current_timestamp"
#This line prints a message to the console indicating that a backup is being taken, along with the current timestamp.
tar czf $backup_file --absolute-names $src_dir
#This line uses the tar command to create a compressed archive of the source directory 
#specified in src_dir. The archive is saved to the file specified in backup_file. The --absolute-names option 
#is used to preserve the full path of the source files in the archive.
echo "Backup complete"
#This line prints a message to the console indicating that the backup is complete.

