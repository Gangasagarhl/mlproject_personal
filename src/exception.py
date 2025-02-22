"""
Step	Explanation
1️⃣ Define a Custom Exception	CustomException is created to handle errors with extra details.
2️⃣ Extract Error Details	error_message_detail() fetches file name, line number, and error message.
3️⃣ Store the Error Message	CustomException calls error_message_detail() to format the message.
4️⃣ Return the Message	__str__() returns the formatted error message when printed.


 What Is Happening in the Code?
The code defines a custom exception handling mechanism in Python. It provides detailed error messages, including:

File name where the error occurred.
Line number of the error.
Error message.
📌 Corrected Step-by-Step Explanation
1️⃣ Custom Exception Handling is Implemented
A custom exception class CustomException is created by inheriting Python’s built-in Exception class.
This class ensures that when an error occurs, detailed error information is extracted.
2️⃣ error_message_detail() Extracts Error Details
The function error_message_detail(error, error_details:sys) extracts information about the error using sys.exc_info().
It retrieves:
File name (co_filename) where the error occurred.
Line number (tb_lineno) where the error happened.
Actual error message (str(error)).
The extracted details are formatted into a readable error message.
🔹 Example Output of error_message_detail()

scss
Copy
Edit
Error occurred in python file name [script.py] line number [23] error message [ZeroDivisionError: division by zero]
3️⃣ The CustomException Class Stores the Formatted Error
The CustomException class stores the detailed error message and passes it to the parent Exception class.
super().__init__(error_message) ensures that Python’s built-in exception mechanism is preserved.
self.error_message = error_message_detail(error_message, error_details=error_detail)
Calls error_message_detail() to format the error message.
Stores the formatted message in self.error_message.
4️⃣ __str__() Returns the Formatted Error Message
When the exception is printed (print(CustomException(...))), Python calls __str__(), which returns self.error_message.


"""


import sys
#import logging
from src.logger import logging

def error_message_detail(error,  error_details:sys):
    _,_,exec_tb =  error_details.exc_info()
    #exec_td is the director to the error that has occurred.
    #line number
    #file name, those all will be there in the exec_td
    file_name =  exec_tb.tb_frame.f_code.co_filename
    #this is given in the custom exeception handling 
    
    error_message = "Error occurred in python file name [{0}] line number [{1}] error messsage [{2}]".format(file_name, exec_tb.tb_lineno, str(error))
    
    return error_message



class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details = error_detail)
        
    def __str__(self): 
        return self.error_message
    
    
    
    
if __name__=="__main__":
    try: 
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
        