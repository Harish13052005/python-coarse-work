Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = 'python'
for i in range(len(s))
    for j in range(i+1, s):
        
SyntaxError: expected ':'
s = 'python'
for i in range(len(s)):
    for j in range(i+1, s):
        
SyntaxError: multiple statements found while compiling a single statement

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py", line 3, in <module>
    for j in range(i+1, s):
TypeError: 'str' object cannot be interpreted as an integer

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
p y
p t
p h
p o
p n
y t
y h
y o
y n
t h
t o
t n
h o
h n
o n

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
p yp tp hp op ny ty hy oy nt ht ot nh oh no n

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
p y p t p h p o p n y t y h y o y n t h t o t n h o h n o n 

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
py pt ph po pn yt yh yo yn th to tn ho hn on 

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py", line 13, in <module>
    s+=i
TypeError: unsupported operand type(s) for +=: 'int' and 'list'

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py", line 14, in <module>
    s+=i
TypeError: unsupported operand type(s) for +=: 'int' and 'list'

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
45

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
120

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
Account number: 1234
Pin Number: 4567
Account number: 5677
Pin Number: 8789
Account number: 5676
Pin Number: 6565
Account number: 3436
Pin Number: 3456

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 

===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
enter the size:
===== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py =====
enter the size:
    p yp tp hp op ny ty hy oy nt ht ot nh oh no n
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py", line 42, in <module>
    n = int(input("enter the size:"))
ValueError: invalid literal for int() with base 10: ''

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
10
0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
0101010101
0101010101
0101010101
0101010101
0101010101
0101010101
0101010101
0101010101
0101010101
0101010101

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:20
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101
01010101010101010101

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:20
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:20
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * * 
* * * * * * * * * * * * * 
* * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
5
* * * * * 
* * * * 
* * * 
* * 
* 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:5
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py", line 79, in <module>
    print(" "*n-i)
NameError: name 'i' is not defined. Did you mean: 'id'?

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:5
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py", line 79, in <module>
    print(" "*n-i)
TypeError: unsupported operand type(s) for -: 'str' and 'int'

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:5
     
     
*    
**   
***  
**** 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:5
      
     *
    **
   ***
  ****

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:20
                     
                    *
                   **
                  ***
                 ****
                *****
               ******
              *******
             ********
            *********
           **********
          ***********
         ************
        *************
       **************
      ***************
     ****************
    *****************
   ******************
  *******************

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:20
                     
                     * 
                    *  * 
                   *  *  * 
                  *  *  *  * 
                 *  *  *  *  * 
                *  *  *  *  *  * 
               *  *  *  *  *  *  * 
              *  *  *  *  *  *  *  * 
             *  *  *  *  *  *  *  *  * 
            *  *  *  *  *  *  *  *  *  * 
           *  *  *  *  *  *  *  *  *  *  * 
          *  *  *  *  *  *  *  *  *  *  *  * 
         *  *  *  *  *  *  *  *  *  *  *  *  * 
        *  *  *  *  *  *  *  *  *  *  *  *  *  * 
       *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
      *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
     *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
    *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
   *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:20
                     
                    *
                   **
                  ***
                 ****
                *****
               ******
              *******
             ********
            *********
           **********
          ***********
         ************
        *************
       **************
      ***************
     ****************
    *****************
   ******************
  *******************

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:5
      
     *
    **
   ***
  ****

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:20
* * * * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * * 
        * * * * * * * * * * * * * * * * 
          * * * * * * * * * * * * * * * 
            * * * * * * * * * * * * * * 
              * * * * * * * * * * * * * 
                * * * * * * * * * * * * 
                  * * * * * * * * * * * 
                    * * * * * * * * * * 
                      * * * * * * * * * 
                        * * * * * * * * 
                          * * * * * * * 
                            * * * * * * 
                              * * * * * 
                                * * * * 
                                  * * * 
                                    * * 
                                      * 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:5
0
1
0
1
0

1
0
1
0
1

0
1
0
1
0

1
0
1
0
1

0
1
0
1
0


=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:5
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:20
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:10
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py", line 86, in <module>
    for sp in range(n-i):
NameError: name 'i' is not defined. Did you mean: 'id'?

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:10
Traceback (most recent call last):
  File "C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py", line 86, in <module>
    for sp in range(n-i):
NameError: name 'i' is not defined. Did you mean: 'id'?

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:10
                    
                  *

                *
*

              *
*
*

            *
*
*
*

          *
*
*
*
*

        *
*
*
*
*
*

      *
*
*
*
*
*
*

    *
*
*
*
*
*
*
*

  *
*
*
*
*
*
*
*
*

enter size:
=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:10
                    
                  * 
                * * 
              * * * 
            * * * * 
          * * * * * 
        * * * * * * 
      * * * * * * * 
    * * * * * * * * 
  * * * * * * * * * 
enter size:
=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:10
                    
                  * 
                * * 
              * * * 
            * * * * 
          * * * * * 
        * * * * * * 
      * * * * * * * 
    * * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * 
enter size:24
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:10
                    
                  * 
                * * 
              * * * 
            * * * * 
          * * * * * 
        * * * * * * 
      * * * * * * * 
    * * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
           
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
           
           *
          * *
         * * *
        * * * *
       * * * * *
      * * * * * *
     * * * * * * *
    * * * * * * * *
   * * * * * * * * *
  * * * * * * * * * *

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
                      *          **         ***        ****       *****      ******     *******    ********   *********  ********** 

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
                     
                   *
                 **
               ***
             ****
           *****
         ******
       *******
     ********
   *********
 **********

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
           
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
          

         
*
        
**
       
***
      
****
     
*****
    
******
   
*******
  
********
 
*********

**********

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:10
           
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********

=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter size:10
                    
                  * 
                * * 
              * * * 
            * * * * 
          * * * * * 
        * * * * * * 
      * * * * * * * 
    * * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * 
>>> 
=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:12
001 
001 001 
001 001 001 
001 001 001 001 
001 001 001 001 001 
001 001 001 001 001 001 
001 001 001 001 001 001 001 
001 001 001 001 001 001 001 001 
001 001 001 001 001 001 001 001 001 
001 001 001 001 001 001 001 001 001 001 
001 001 001 001 001 001 001 001 001 001 001 
001 001 001 001 001 001 001 001 001 001 001 001 
>>> 
=============================================== RESTART: C:/Users/HARISH/Desktop/python-coarse-work/day-13/nested.py ==============================================
enter the size:12
01 
01 01 
01 01 01 
01 01 01 01 
01 01 01 01 01 
01 01 01 01 01 01 
01 01 01 01 01 01 01 
01 01 01 01 01 01 01 01 
01 01 01 01 01 01 01 01 01 
01 01 01 01 01 01 01 01 01 01 
01 01 01 01 01 01 01 01 01 01 01 
01 01 01 01 01 01 01 01 01 01 01 01 
