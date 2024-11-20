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
╭─────────╮
│   003   │ # red for inactive, Green for active
│  1 1 _  │
│_<-- -->1│
╰─────────╯
```
