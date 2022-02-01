# SQL CheatSheet: https://www.sqltutorial.org/sql-cheat-sheet/

#                   Basic of SQL (Strutured Query Language)

    # SQL Wildcards
    'Check CheatSheet or any online materials'

    # SQL Statements

'''
    KEYWORD [object] KEYWORD [OBJECT] ...;
    Rules:
        SQL statements always start with the keywords.
        SQL statement ends with a semicolon. ";"
        SQL is not case sensitive, means the from is the same as FROM

'''
SELECT table_column from table_name WHERE condition; 

    # SQL Syntax

# SELECT 
SELECT table_column FROM table_name;
SELECT *            FROM table_name;

SELECT TOP number1|percent table_column
FROM table_name
WHERE condition;    
'The SELECT statement is used to select data from a database.
In SQL Server, SELECT TOP is used to spectify the number of records to return 
'

# SELECT DISTINCT
SELECT DISTINCT table_column1,table_column2 FROM table_name;
'The SELECT DISTINCT statement is used to return only distinct (different) values'

# WHERE
SELECT table_column FROM
WHERE condition;
'
The WHERE is used to extract only those records that fulfil a specifed condition
Values: String "abc", Number "123.64" and NULL (empty value)
Operators:
    =       Equal
    >       Greater than
    <       Less than
    >=      Greater than or equal
    <=      Less than or equal
    <>      Not Equal
    BETWEEN Between a certain range
    LIKE    Search for a pattern ('s%' means starting with 's' letter)
    IN      Search multiple possible values
'
# BETWEEN
SELECT table_column
FROM table_name
WHERE table_column BETWEEN value1 AND value2

# LIKE
SELECT table_column
FROM table_name
WHERE table_column1 LIKE pattern;
'
There are two signs of Wildcard with LIKE: percent sign (%) and underscore sign(_)
'
# IN
SELECT table_column
FROM table_name
WHERE table_column IN (value1, value2,...);

'or'
SELECT table_column
FROM table_name
WHERE table_column IN (SELECT [new STATEMENT]) 



# AND, OR, NOT 
SELECT table_column1, table_column2
FROM table_name
WHERE condition1 AND condition2 OR condition3 NOT condition....;
'
The WHERE can be combined with AND,OR and NOT operators
    AND displays a record IF all conditions are TRUE
    OR displays a record IF ANY of all conditions are TRUE
    NOT displays a record IF the conditions are NOT TRUE
'

# ORDER BY
SELECT table_column1, table_column2
FROM table_name
ORDER BY table_column1, table_column2 ASC|DESC;
'The ORDER BY is used to sort the result-set in Ascending(default) or Descending'

# INSERT INTO
INSERT INTO table_name(table_column1, table_column2)
VALUES (value1, value2);
'The INSERT INTO is used to insert new record in a table'

# UPDATE
UPDATE table_name
SET table_column1 = value1, table_column2 = value2
WHERE condition;
'The UPDATE is used to modify the existing records in a table'

# DELETE
DELETE 
FROM table_name
WHERE condition;
'The Delete is used to delete existing records in a table' 

# AS (Aliases-'Temporary name')
SELECT table_column AS Aliases_column
FROM table_name AS Aliases_table;

# JOIN
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;


#       SQL FUNCTION()

# MIN() and MAX()
SELECT MIN(table_column)
FROM table_name
WHERE condition;
'MIN() function returns the SMALLEST value of the selected column
 MAX() function returns the LARGEST value of the selected column
'

# COUNT(), AVG(), SUM()
SELECT COUNT(table_column)
FROM table_name
WHERE condition;
'
COUNT() function returns the number of rows that match the condition
AVG() function returns the average value of a NUMERIC column
SUM() function returns the total sum of a NUMERIC column
'