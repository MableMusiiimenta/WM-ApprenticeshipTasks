 Document the concept
Create:

week-4/tuesday/input-validation.md
Explain these terms in your own words:

parsing / conversion  ---this means changing the data type of a value

validation  ---this is checking whether a value meets a condition required by the system/program

persistence  ---persistence basically means data staying intact in the database even when the server restarts

explain this example:

"hello"
    cannot become a price   ---a value error is raised due to trying to convert a letter string into an int/float

"-10"
    can become a number
    but is not an allowed price   ---It can be successfully converted because it is a number string, but it is still invalid because it is less than 0/negative

"25.50"
    can become a number
    and is an allowed price   ---It can be successfully converted because it is a number string, and it is still valid because it is greater than 0


Why should validation happen before add_product()?
because only validated values must be added to the database

Why is HTML form validation alone not enough?
because it could send invalid data to the database

Why does the database function not need to know about request.form?
because it 

