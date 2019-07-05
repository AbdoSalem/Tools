import matplotlib.pyplot as plt

def init(figsize=(50,50)):
    fig = plt.figure(figsize=figsize, dpi=80, facecolor='w', edgecolor='k')
    ax = plt.gca()
    return fig,ax