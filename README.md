# FSLab
the operating system final project file system management

### Download
You can use the git command line interface, enter the following command

```
git clone git@github.com:New-generation-hsc/FSLab.git
```

### Run

```python
python main.py
```

### Operation

The default login user is guest, and the guest has only read permission. if you want to create file or directory, please login using `admin`

The `admin` has all permission in any place, include the following permission:

- create file
- create directory
- add user
- delete user
- write to file
- read from file

---

### Commands

The System contains the following commands:

> `su` [username]

switch user, you can use different username to login the system

for example:

```
su admin
```

> `adduser` [username]

add a new user to this system, and a corresponding user directory will be created in the root directory

for example:

```
adduser greek
```

> `deleteuser` [username]

delete a user from this system, and the corresponding user directory will be delete from root directory

```
deleteuser greek
```

> `touch` [file [file1 [file2]]]

create a new file in current directory, and you can create multiple files in one time

for example:

```
touch file1 file2 file3
```

> `mkdir` [directory [directory2 [directory3]]]

create a new directory in current directory, and you can create multiple directories in one time

for example:
```
mkdir directory1 directory2 directory3
```

> `ls` [-s] [-d] [-f] [-l]

list current file or directory information

for example:

```
ls -l
```

> `rm` [-r] [file [directory]]

remove file or directory from current path

for example:
```
rm file1

rm -r directory1
```

> `cd` [path]

change directory from current path, and support `.`, `..`, `/[path]`

for example:

```
cd /dir1
```

> `clear`

 clear screen

 for example:

```
clear
```