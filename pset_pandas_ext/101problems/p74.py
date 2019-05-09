"""
75. How to split a text column into two separate columns?
"""
"""
Difficulty Level: L2
"""
"""
Split the string column in df to form a dataframe with 3 columns as shown.
"""
"""
Input
"""
"""
df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])

print(df)
#>                         row
#> 0          STD, City\tState
#> 1  33, Kolkata\tWest Bengal
#> 2   44, Chennai\tTamil Nadu
#> 3  40, Hyderabad\tTelengana
#> 4  80, Bangalore\tKarnataka
"""
"""
Desired Output
"""
"""
0 STD        City        State
1  33     Kolkata  West Bengal
2  44     Chennai   Tamil Nadu
3  40   Hyderabad    Telengana
4  80   Bangalore    Karnataka
"""
"""
# Input
df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])

# Solution
df_out = df.row.str.split(',|\t', expand=True)

# Make first row as header
new_header = df_out.iloc[0]
df_out = df_out[1:]
df_out.columns = new_header
print(df_out)0 STD        City        State
1  33     Kolkata  West Bengal
2  44     Chennai   Tamil Nadu
3  40   Hyderabad    Telengana
4  80   Bangalore    Karnataka
"""
"""
To be continued . .
"""
"""
RelatedNumpy Tutorial Part 2 - Vital Functions for Data AnalysisNumpy is the core package for data analysis and scientific computing in python. This is part 2 of a mega numpy tutorial. In this part, I go into the details of the advanced features of numpy that are essential for data analysis and manipulations. Introduction In part 1 of the…February 14, 2018In “Python”101 NumPy Exercises for Data Analysis (Python)The goal of the numpy exercises is to serve as a reference as well as to get you to apply numpy beyond the basics. The questions are of 4 levels of difficulties with L1 being the easiest to L4 being the hardest. If you want a quick refresher on numpy,…February 26, 2018In “Python”Numpy Tutorial Part 1 - Introduction to ArraysThis is part 1 of the numpy tutorial covering all the core aspects of performing data manipulation and analysis with numpy's ndarrays. Numpy is the most basic and a powerful package for scientific computing and data manipulation in python. 1. Introduction to Numpy Numpy is the most basic and a…February 7, 2018In “Python”
"""
"""

  
  

    
      
    


    

      
        
          
            

  
    
      
    
  

          

          
            Sharing is caring!
          
        
        
          

          
          
            
              212
              

                
                

                
                
                  Share
                  

                
              
            
          
            
              0
              

                
                

                
                
                  Tweet
                  

                
              
            
          
            
              230
              

                
                

                
                
                  Pin
                  

                
              
            
          
            
              0
              

                
                

                
                
                  Share
                  

                
              
            
          
            
              0
              

                
                

                
                
                  Mail
                  

                
              
            
          
            
              0
              

                
                

                
                
                  Share
                  

                
              
            
          
        
      
      
        
      
    
  


"""
