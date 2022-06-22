import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


__all__ = ["save_all"]

def save_all(filename):
    with PdfPages(filename) as pdf:
        for fig in plt.get_fignums():
            pdf.savefig(fig)
