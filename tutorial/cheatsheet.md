###Sublime
```bash
// ctrl+`
>> sublime.log_commands(False)
```

| Key           |  Action  |
| ------------------------ | -------------------------|
| ctrl+m | Move to bracket |

###Tmux
| Key           |  Action  |
| ------------------------ | -------------------------|
| & | Delete current window |
| x | Delete current pane |
| i  j  k  l | Move pane |
| n,p | Move window |
| z | Resize current pane |
| . | Change number of window |
| , | Rename window |
| c | Create new window |
| y | Rotate pane |
| t | Swap window |


###Emacs
| Key           |  Action  |
| ------------------------ | -------------------------|
| C-u C-x =                | Check the font info |
| C-c zuojiantou           | back to last window split |
| C-c <                    | Python mode indentation |
| C-x 4 t                  | toggle-window-split |
| C-x 0                    | Close the selected window |
| C-middle click on scroll | Split the window |
| C-x tab                  | Intent one space |
| C-x w r                  | Unhight-light regex |
| C-x r k                  | Select region, move cursor to x spaces before the indent want to kill of the text, then run this
| C-h b                    | Show all key bindings |

#####M-x
* controller-view-toggle
* find-library
* load-file
* winner-mode
* query-replace
* hight-regex
* replace
* delete-matching-lines
* delete-non-matching-lines
* speedbar
* untabify
* repleace-regex <RET>^<RET>Your Text<RET> Insert text to every line begin
* sort lines

###bash
```
dig any yancao-terry.com +short            # DNS lookup tool
```

```
sudo su -
su - rnd
```

```
killall -v python                          # when seeing a lot python process, use this to kill all of them
```

```
grep search for a error code               # grep -r "[0-9]\{4\}" *
```

###git
Way to do the rebase:
1. ```git checkout master```
2. ```git pull origin master```
3. ```git checkout mybranch```
4. ```git rebase -i master```   In this step, do squash or pick up the commit message
5. ```git checkout master```
6. ```git merge mybranch```    Which will easily merge branch since it's as if you just created new changes.
7. ```git push -u origin master```     After that git pull is all set
8. ```git log --author="Yan Cao" --pretty=tformat: --numstat | gawk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s removed lines: %s total lines: %s\n", add, subs, loc }' -```

###python
```python
python -m SimpleHTTPServer
```
#####Open File
```python
f = open('perm_log.txt', 'w')
f.write('Something\n')
```

#####Output Template
```python
new_user_template = '{emp_id:10} {first_name:20} {last_name:20} {group_name_new:30} {group_name_old}\n'
f.write(new_user_template.format(emp_id = 'Emp Id', first_name = 'First Name', last_name = 'Last Name', group_name_new = 'Granted Group Name', group_name_old = 'Because had Group'))
```

#####Args Parser
```python
import argparse

# Flag parser for either store or abort database
parser = argparse.ArgumentParser(description='Map NQE users to Mercury')

# Named arguments (leading "-" or "--") (args.database)
parser.add_argument('-d', '--database', dest='database', action='store_true', required=False, default=False, help='Actually commit database work (default: no)')
parser.add_argument('-d', '--days', dest='days', action='store',type=int, help='Set a window of past x days')

# file
parser.add_argument('fname', type=argparse.FileType('r'), action='store', help='A text file containing a dictionary of the old term ID and the new body')

args = parser.parse_args()

data_entered = (args.fname).read()
new_data = ast.literal_eval(data_entered)


if args.database:
    sqlcorp.commit()
    print 'Committed.'
else:
    sqlcorp.rollback()
    print 'Aborted.'
```

#####Excel
```python
from xlwt import *
w = Workbook()
ws1 = w.add_sheet('Sheet Name')
ws1.write(row_num,col_num, 'Text')
```

#####CSV
```python
f = open('new_quotes.csv', 'wb')
writer = csv.writer(f)
headers = ['quote_id', 'quote_num', 'descr', 'status', 'date_created', 'date_modified', 'created_by', 'mod_by']
writer.writerow(headers)
```

#####Regex For Date
```python
pattern = re.compile(r'(\d{4})(\d{2})(\d{2})')
start_date = datetime.datetime( *[int(x) for x in pattern.match(args.start).groups()] )
```

#####Previous Date
```python
start_date = datetime.date.today() - datetime.timedelta(days=args.days)
start_date = datetime.date(2014, 7, 29)
```

#####eval
```python
# Python has an eval() function which evaluates a string of Python code:
assert eval("2 + 3 * len('hello')") == 17

# ast.literal_eval raises an exception if the input isn't a valid Python datatype, so the code won't be executed if it's not.
new_data = ast.literal_eval(data_entered)
```

###Iterm2
* Command + Option + Shift + H for a horizontal split
* Command + Option + Shift + V for a vertical split
* Command + Option + [Arrow Key]: Switches to the next pane in that direction
* Command + Shift + Enter: Maximizes the active pane
