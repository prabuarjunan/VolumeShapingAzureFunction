# VolumeShapingAzureFunction
    The Azure Functions trigger volume shaping using the REST API. The defined time trigger triggers the azure function to optimize 
    the performance for the required peak workload and change the service level of the capacity pool. The pre-defined Azure functions calls 
    the REST API to update the volume with the differnt service level and required allocated capacity change the allocated capacity 
    of the Azure NetApp files using time triggered azure function
    This project has the following files:
    TimerTriggerAllocateMoreCapacity/__init__.py:This Azure Function triggers every business day to increase the allocated capacity based on required perfromance.
    TimerTriggerAllocateLessCapacity/__init__.py:This Azure Function triggers every business day to decrease the allocated capacity after the work hours 
    based on required perfromance.
    TimerTriggerServiceLevelChange/__init__.py/volumeShapingsizing_serviceLevel.py: The time trigger triggers the function to change the service level of the 
    capacity pool to another service level. 
