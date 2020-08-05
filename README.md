# VolumeShapingAzureFunction
    change the allocated capacity of the Azure NetApp files using time triggered azure function
    This project has the following files:
    TimeTrigger/__init__.py: Python file that contains all code to scrape websites. This Azure Function is time triggered.
    TimeTrigger1/__init__.py: Python file that contains all code to scrape websites. This Azure Function is time triggered.
    TimeTrigger/__init__.py/volumeShapingsizing.py: The time trigger triggers the function to allocate more capacity to the volume at a particular time
    TimeTrigger1/__init__.py/volumeShapingsizing_dealloc.py: The time trigger triggers the function to reallocate less capacity to the volume at a particular time
    TimerTriggerServiceLevelChange/__init__.py/volumeShapingsizing_serviceLevel.py: The time trigger triggers the function to change the service level of the capacity pool to another service level. 
