import matplotlib.pyplot as plt
import collections

import os
import pytagcloud

RESULT_DIRECTORY = '__results__/graph'


# pytagcloud 설치후
def wordcloud(wordsfreq, filename):
    taglist = pytagcloud.make_tags(wordsfreq.items(), maxsize=50)

    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(600, 400),
        rectangular=False,
        background=(0, 0, 0),
        fontname='Malgun'
    )


def graph_bar(title=None,
               xlabel=None,
               ylabel=None,
               show_grid=False,
               values=None,
               ticks=None,
               file_name=None,
              show_graph=True):

    fig, subplots = plt.subplots(1, 1)
    subplots.bar(range(len(values)), values, align='center')

    # ticks
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(values)))
        subplots.set_xticklabels(ticks, rotation=70, fontsize='small')

    # title
    if title is not None and isinstance(title, str):
        subplots.set_title(title)

    # xlabel
    if xlabel is not None and isinstance(title, str):
        subplots.set_xlabel(xlabel)

    # ylabel
    if ylabel is not None and isinstance(title, str):
        subplots.set_ylabel(ylabel)

    # show grid
    subplots.grid(show_grid)

    if file_name is not None and isinstance(file_name, str):
        save_filename = '%s/bar_%s.png' % (RESULT_DIRECTORY, file_name)
        plt.savefig(save_filename, dpi=400, bbox_inches='tight')

    if show_graph:
        plt.show()


if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)