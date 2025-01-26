
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plotly_plot(df,x,y,color, title,ytitle):
    """
    plot a graph using plotly

    Parameters
    ----------
    :param df: dataframe
    :param x: str - column name that will be used in x axis
    :param y: str - column name that will be used in y axis
    :param color: str - column name that that will be used to color tickers names
    :param title: str - plot title
    :param ytitle: str - axis x title

    Returns
    -------
    a plot using plotly
    """

    fig = px.line(df, x=x, y=y, color=color,
                title=title)
    
    fig.update_layout(
        title_font_size=24,
        title_font_family='Montserrat',
        title_font_color='darkblue',
        font_family='Roboto',
        font_color='black',
        xaxis_title=None,
        yaxis_title=ytitle
    )
    return fig.show()

def matplotlib_plot(col_nomes, df, fcolumn, x,y,style='ggplot', grid=True):
    """
    plot a graph using matplotlib

    Parameters
    ----------
    col_names: array-like 
        array with values to identify each label value
    df: dataframe
    fcolumn: str 
        column that should be use to filter the dataframe
    x: str 
        column name that will be used in x axis
    y: str 
        column name that will be used in y axis
    style: str 
        matplotlib style that will be used in plot
    You can see the entire style list here or use mp_styles()

    https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    grid: boolean
        set True or False to show grid

    Returns
    -------
    a plot using matplotlib
    """

    fig,ax = plt.subplots(figsize=(15,8))

    for nome in col_nomes:
        ax.plot(df[df[fcolumn]==nome][x], df[df[fcolumn]==nome][y], label=nome)

    ax.set_title('Retorno dos principais índices (normalizado)', fontdict={'size':18,'weight':'bold'})
    ax.grid()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(54))
    ax.legend(loc=2)

    if grid:
        ax.grid()

    return plt.show()


def mp_styles():
    """
    Returns
    -------
     A list of available styles to use with plotar_matplotlib function
    """
    styles = plt.style.available
    return styles