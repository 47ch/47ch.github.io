from django.shortcuts import render
import pandas as pd

# Create your views here.

def display_tables(request):

    df = pd.read_csv('data/Table_Input.csv')
    
    df2 = pd.DataFrame({
        'City': ['New York', 'Los Angeles', 'Chicago'],
        'Population': [8000000, 4000000, 2700000]
    })
    
    # Convert DataFrames to HTML tables
    table1 = df.to_html(classes='table table-striped')
    table2 = df2.to_html(classes='table table-striped')
    
    context = {
        'table1': table1,
        'table2': table2
    }
    
    return render(request, 'display_tables.html', context)
