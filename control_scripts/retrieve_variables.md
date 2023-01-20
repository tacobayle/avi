```
#!/usr/bin/python
#
# NSX Advanced Load Balancer ControlScript
#
# This sample ControlScript will output the environment values, and alert
# arguments that are passed from the alert that triggered the alert script.
# You can use these values to help construct your python script actions to
# handle the alert.
#
#
import os
import sys
 
if __name__ == "__main__":
    print("Environment Vars: %s \n" % os.environ)
    print("Alert Arguments: %s \n" % sys.argv)
```