Pascal's Triangle
Pascal's triangle is a triangular arrangement of numbers named after the French mathematician Blaise Pascal. Each number in the triangle is the sum of the two numbers directly above it.

Here is an example of Pascal's triangle with 5 rows:

          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
In the above triangle, the numbers on the edges are always 1, and the other numbers are obtained by adding the two numbers directly above them.

Solution expalined
Integer n as input, representing the number of rows of Pascal's triangle. It returns a list of lists that represents the triangle. an empty list lists is initialized. If n is equal to 0, indicating that the number of rows requested is 0, an empty list is returned immediately.

Overall, this function efficiently generates Pascal's triangle based on the given number of rows n. It handles the edge case of n = 0 by returning an empty list. The function uses nested loops to populate the triangle row by row, calculating each element based on the two elements directly above it. The resulting triangle is returned as a list of lists.
