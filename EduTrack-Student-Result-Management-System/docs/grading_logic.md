Validation rules

GPA formula

Grade table

Fail conditions

Pseudo-logic

Edge cases

## Result Object Structure

After result computation, the system stores the derived result
inside the student record in the following structured format:

{
  "result": {
    "gpa": 9.2,
    "grade": "A+",
    "status": "PASS"
  }
}

This structure ensures separation between raw marks data
and computed academic outcomes.


## Result Processing Workflow (Pseudo Logic)

The system follows the below logical steps to process results:

FOR each student:
    FETCH marks for all subjects
    VALIDATE marks

    IF any subject marks < 35:
        status = FAIL
    ELSE:
        status = PASS

    CALCULATE total marks obtained
    CALCULATE total maximum marks
    COMPUTE GPA

    ASSIGN grade based on GPA
    STORE result object inside student record
