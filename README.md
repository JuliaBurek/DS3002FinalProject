# DS3002FinalProject

In this project, I wrote and deployed a process that executes exactly once every minute, retrieving data from a remote API and wrote all retrieved values to a database for 60 minutes. Using code-based data analysis techniques against the database, try to (i) describe any patterns or changes in the data over time; and (ii) explain the logic of these changes.

After writing the retrieved values to a database for 60 minutes, I made some observations about the data. The 'factor' number is increasing per minute by several thousand numbers. In the 'pi' values, there appears to be a sort of alternating pattern between the minutes with the numbers increasing, then decreasing. For example, at minute 2 the pi value is approximately 3.1415836, at minute 3 the pi value is approximately 3.1416011, and at minute 4 the pi value is approximately 3.1415846. The values all seem to be roughly 3.1416. There are numbers following each of these values every minute but that is the pattern I recognized for the first 5 digits. Considering the actual value of pi begins with 3.14159265359, it makes sense for the pi values to be around this number. 
