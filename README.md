# File Lock

An illustration to write, append and delete files using file locks.

Setup:
```
git clone https://github.com/bhuvansingla/filelock.git
cd filelock
pip3 install -r requirements.txt
```

Run:
```
python3 script.py <destination_file> <source_file> <operation_code>
```

Operation Codes:  
```0``` : Append source_file to destination_file  
```1``` : Overwrite destination_file with source_file  
```2``` : Delete both source_file and destination_file  
