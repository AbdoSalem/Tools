from Visualize import init
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

def define_cmap(cmap, n):
    cm = plt.get_cmap(cmap)
    cNorm = colors.Normalize(vmin=0, vmax=n)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    return scalarMap

def __plot_one_line(ax, xs, ys, line_label, yerr=None, c=None, anotate = False):
    if c:
        ax.plot(xs, ys, label=line_label, c=c)
    else:
        ax.plot(xs, ys, label=line_label if line_label else 'f(x)')
    if anotate:
            for a, b in zip(xs, ys):
                ax.annotate('%.2f' % (b), (a, b))

def __plot_one_errorbar(ax, xs, ys,line_label, yerr=None, c=None, anotate = False):
    if c:
        ax.errorbar(xs, ys, yerr=yerr, label=line_label, c=c,capsize=3)
    else:
        ax.errorbar(xs, ys, yerr=yerr, label=line_label if line_label else 'f(x)',capsize=3)
    if anotate:
            for a, b in zip(xs, ys):
                ax.annotate('%.2f' % (b), (a, b))

def __plot_xs_ys_func(plotf,xs, ys, ax, lines_label,yerr = None, cmap = None, anotate = False):
    print(ys,xs,yerr)
    if not isinstance(ys[0], list):
        if cmap:
            colors = define_cmap(cmap, 1)
            plotf(ax,xs,ys,yerr=yerr, line_label=lines_label if lines_label else 'f(x)',c=colors.to_rgba(0),anotate=anotate)
        else:
            plotf(ax,xs, ys,yerr=yerr, line_label=lines_label if lines_label else 'f(x)', anotate=anotate)
    else:
        for i, ysi in enumerate(ys):
            if cmap:
                colors = define_cmap( cmap,len(ys))
                plotf(ax,xs, ysi,yerr=yerr[i], line_label=lines_label[i] if lines_label else r'$f_{%s}i(x)$' % i,c=colors.to_rgba(i),anotate=anotate)
            else:
                plotf(ax,xs, ysi,yerr=yerr[i], line_label=lines_label[i] if lines_label else r'$f_{%s}i(x)$' % i)


def draw_line_graph(xs,ys,ys1=None,xlabel = None,yerr= None,yerr1= None,ylabel = None,ylabel1=None,lines_label=[],lines_label1=[],pdf_dir=None,show = False,anotate = False):
    fig,ax = init(plt.rcParams.get('figure.figsize'))
    if ys1:
        ax1 = ax.twinx()

    f=  __plot_one_errorbar if yerr else __plot_one_line

    f1 = __plot_one_errorbar if yerr1 else __plot_one_line

    __plot_xs_ys_func(f,xs, ys, ax, lines_label,yerr=yerr, anotate=anotate)


    if ys1 and ax1:
        __plot_xs_ys_func(f1,xs, ys1, ax1, lines_label1,yerr=yerr1, anotate=anotate, cmap='jet')
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
        if ys1:
            ax1.set_ylabel(ylabel1)

    ax.legend(loc='upper left')
    ax1.legend(loc='upper right')
    if(pdf_dir):
        plt.savefig(pdf_dir, format='pdf')
    if show:
        plt.show()




