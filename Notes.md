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








                                     ╭─────────────────╮
                                     │003  - 000 -  001│
                                     │_<-- _  _  _ -->_│
                                     ╰─────────────────╯


            ╭─────────────────╮                                 ╭─────────────────╮
            │002  - 003 -  000│                                 │000  - 001 -  002│
            │_<-- _  _  _ -->_│                                 │_<-- _  _  _ -->_│
            ╰─────────────────╯                                 ╰─────────────────╯
                                                            
                                                            
                                     ╭─────────────────╮
                                     │001  - 002 -  003│
                                     │_<-- _  _  _ -->_│
                                     ╰─────────────────╯



─────────────────────────────────────── Circle of Robots ────────────────────────────────────────
```
╭───────────────────╮ ╭───────────────────╮ ╭───────────────────╮ ╭───────────────────╮
│ 007  - 000 -  001 │ │ 000  - 001 -  002 │ │ 001  - 002 -  003 │ │ 002  - 003 -  004 │
│ _<-- _  _  _ -->_ │ │ _<-- _  _  _ -->_ │ │ _<-- _  _  _ -->_ │ │ _<-- _  _  _ -->_ │
╰───────────────────╯ ╰───────────────────╯ ╰───────────────────╯ ╰───────────────────╯
╭───────────────────╮ ╭───────────────────╮ ╭───────────────────╮ ╭───────────────────╮
│ 003  - 004 -  005 │ │ 004  - 005 -  006 │ │ 005  - 006 -  007 │ │ 006  - 007 -  000 │
│ _<-- _  _  _ -->_ │ │ _<-- _  _  _ -->_ │ │ _<-- _  _  _ -->_ │ │ _<-- _  _  _ -->_ │
╰───────────────────╯ ╰───────────────────╯ ╰───────────────────╯ ╰───────────────────╯
```

# TODO
refactor with better names  node-robot  CDLL-circle
advance_clock

robots to circle

max_pre_time

tupples for algo
```
(_,_)
(0,_)
(_,0)
(1,_)
(_,1)
(0,0)
(0,1)
(1,0)
(1,1)
```


