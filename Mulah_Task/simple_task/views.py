from django.shortcuts import render
import pandas as pd

# Create your views here.

def display_tables(request):

    df = pd.read_csv('Table_Input.csv')

    value_1 = int(df.loc[df['Index #'] == 'A5', 'Value']) + int(df.loc[df['Index #'] == 'A20', 'Value'])
    value_2 = int(df.loc[df['Index #'] == 'A15', 'Value'])/int(df.loc[df['Index #'] == 'A7', 'Value'])
    value_3 = int(df.loc[df['Index #'] == 'A13', 'Value'])*int(df.loc[df['Index #'] == 'A12', 'Value'])
    
    df2 = pd.DataFrame({
        'Category': ['Alpha', 'Beta', 'Charlie'],
        'Value': [value_1, value_2, value_3]
    })
    
    # Convert DataFrames to HTML tables
    table1 = df.to_html(classes='table table-striped')
    table2 = df2.to_html(classes='table table-striped')
    
    context = {
        'table1': table1,
        'table2': table2
    }
    
    return render(request, 'simple_task/display_tables.html', context)

