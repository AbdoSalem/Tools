from Visualize import init
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
import matplotlib.cm as cmx

def define_cmap(cmap, n):
    cm = plt.get_cmap(cmap)
    cNorm = colors.Normalize(vmin=0, vmax=n)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    return scalarMap

def plot_one_line(ax, xs, ys, line_label, c=None, anotate = False):
    if c:
        ax.plot(xs, ys, label=line_label, c=c)
    else:
        ax.plot(xs, ys, label=line_label if line_label else 'f(x)')
    if anotate:
            for a, b in zip(xs, ys):
                ax.annotate('%.2f' % (b), (a, b))

def plot_xs_ys_line(xs, ys, ax, lines_label, cmap = None, anotate = False):

    if not isinstance(ys[0], list):
        if cmap:
            colors = define_cmap(cmap, 1)
            plot_one_line(ax,xs,ys,label=lines_label if lines_label else 'f(x)',c=colors.to_rgba(0),anotate=anotate)
        else:
            plot_one_line(ax,xs, ys, label=lines_label if lines_label else 'f(x)', anotate=anotate)
    else:
        for i, ysi in enumerate(ys):
            plot_one_line()
            if cmap:
                colors = define_cmap( cmap,len(ys))
                plot_one_line(ax,xs, ysi, line_label=lines_label[i] if lines_label else r'$f_{%s}i(x)$' % i,c=colors.to_rgba(i),anotate=anotate)
            else:
                plot_one_line(ax,xs, ysi, line_label=lines_label[i] if lines_label else r'$f_{%s}i(x)$' % i)


def plot_xs_ys_error_bar(xs, ys, ax, lines_label, cmap = None, anotate = False):

    if not isinstance(ys[0], list):
        if cmap:
            colors = define_cmap(cmap,1)
            print(colors.to_rgba(0))
            ax.plot(xs, ys, label=lines_label if lines_label else 'f(x)',c = colors.to_rgba(0))
        else:
            ax.plot(xs, ys, label=lines_label if lines_label else 'f(x)')
        if anotate:
            for a, b in zip(xs, ys):
                ax.annotate('%.2f' % (b), (a, b))
    else:
        for i, ysi in enumerate(ys):
            if cmap:
                colors = define_cmap( cmap,len(ys))
                ax.plot(xs, ysi, label=lines_label[i] if lines_label else r'$f_{%s}i(x)$' % i,c=colors.to_rgba(i))
            else:
                ax.plot(xs, ysi, label=lines_label[i] if lines_label else r'$f_{%s}i(x)$' % i)
            if anotate:
                for a, b in zip(xs, ysi):
                    ax.annotate('%.2f'%(b),(a, b) )


def draw_line_graph(xs,ys,ys1=None,xlabel = None,ylabel = None,ylabel1=None,lines_label=[],lines_label1=[],pdf_dir=None,show = False,anotate = False):
    fig,ax = init(plt.rcParams.get('figure.figsize'))
    if ys1:
        ax1 = ax.twinx()

    plot_xs_ys_line(xs, ys, ax, lines_label, anotate=anotate)


    if ys1 and ax1:
        plot_xs_ys_line(xs, ys1, ax1, lines_label1, anotate=anotate, cmap='jet')
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


