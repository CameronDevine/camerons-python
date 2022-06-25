import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np


__all__ = ["save_all", "named_bar_chart"]


def save_all(filename):
    with PdfPages(filename) as pdf:
        for fig in plt.get_fignums():
            pdf.savefig(fig)


def named_bar_chart(labels, data, *args, width_factor=1, offset_factor=1, **kwargs):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    if data.ndim == 1:
        data = data.reshape(-1, data.size)
    num_labels = len(labels)
    num_sets = data.shape[0]
    assert num_labels == data.shape[1]
    max_width = 1 / num_sets
    width = max_width * width_factor * offset_factor
    x = np.arange(0, num_labels)
    offsets = offset_factor * np.arange(-0.5 + max_width / 2, 0.5, max_width)
    output = []
    for offset, row in zip(offsets, data):
        output.append(plt.bar(x + offset, row, width=width, *args, **kwargs))
    output.extend(plt.xticks(x, labels))
    return output
