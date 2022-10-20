

Example usage:
```
hub = get_hub("Mac address of ics2000", "email", "password")
```

This will also list the devices connected
```
hub.turnon(id of device to turn on)
  
hub.turnoff(id of device to turn off)

print(hub.getlampstatus(id of device))
```

Heavily WIP
