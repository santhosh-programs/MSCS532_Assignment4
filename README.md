# MSCS532_Assignment3

For all the files, I have added the main function. They already have code to test the implemented functions with a random sample data. 
If you need to test various different outputs, you can do by changing the list implemented or create a new list and pass it as a parameter. 

All explanations and detailed analysis will be submitted in a word document

| Distribution   | Heapsort (s) | Quicksort (s) | Merge Sort (s) |
|----------------|--------------|---------------|----------------|
| Random         | 0.00520      | 0.01437       | 0.01332        |
| Sorted         | 0.00198      | 0.00828       | 0.01338        |
| Reverse Sorted | 0.00483      | 0.01172       | 0.01372        |

Input=> 5000 random elements. 
Though technicaly heap sort is n log n for all cases, when its already sorted, it takes lesser time.
Compared with heapsort, on all cases, heapsort outperformed quicksort and merge sort. 
In quick sort too, while it was sorted, quicksort had a higher and faster perfomance. 