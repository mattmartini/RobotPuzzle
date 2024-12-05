use circular doublely-linked list to represent robots

each robot has:
active?
register:
left_buffer
right_buffer

method action to take on each tic-tock

action
read buffers, take action explode or write neigbhoors

Robot output:

```
╭────────────────╮
│001  - 002 - 000│    prev_node  active_flag id active_flag  next_node
│_<--  1 0 _ -->0│    L_sent    l_rvc    register   r_rvc      R_sent 
╰────────────────╯
```


Use getters and setters

`export PYTHONSTARTUP=src/robotpuzzle/bpython_setup.py`  
