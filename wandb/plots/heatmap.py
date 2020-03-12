import wandb
from wandb import util
from wandb.plots.utils import test_missing, test_types, encode_labels
np = util.get_module("numpy", required="Logging plots requires numpy")
scikit = util.get_module("sklearn")
chart_limit = wandb.Table.MAX_ROWS
def round_3(n):
    return round(n, 3)

def heatmap(x_labels, y_labels, matrix_values, x_axis_label=None, y_axis_label=None):
        """
        Generates a heatmap.

        Arguments:
         y_true (arr): Test set labels.
         y_probas (arr): Test set predicted probabilities.
         labels (list): Named labels for target varible (y). Makes plots easier to
                         read by replacing target values with corresponding index.
                         For example labels= ['dog', 'cat', 'owl'] all 0s are
                         replaced by 'dog', 1s by 'cat'.

        Returns:
         Nothing. To see plots, go to your W&B run page then expand the 'media' tab
               under 'auto visualizations'.

        Example:
         wandb.log({'roc': wandb.plots.HeatMap(x_labels, y_labels,
                    matrix_values, x_axis_label=None, y_axis_label=None)})
        """
        if (test_missing(x_labels=x_labels, y_labels=y_labels,
            matrix_values=matrix_values) and test_types(x_labels=x_labels,
            y_labels=y_labels, matrix_values=matrix_values)):
            matrix_values = np.array(matrix_values)

            def heatmap_table(x_labels, y_labels, matrix_values, x_axis_label=None, y_axis_label=None):
                x_axis=[]
                y_axis=[]
                values=[]
                x_label=[]
                y_label=[]
                count = 0
                for i, x in enumerate(x_labels):
                    for j, y in enumerate(y_labels):
                        x_axis.append(x)
                        y_axis.append(y)
                        values.append(round_3(matrix_values[i][j]))
                        x_label.append(x_axis_label)
                        y_label.append(y_axis_label)
                        count+=1
                        if count >= chart_limit:
                            wandb.termwarn("wandb uses only the first %d datapoints to create the plots."% wandb.Table.MAX_ROWS)
                            break

                return wandb.visualize(
                    'wandb/heatmap/v1', wandb.Table(
                    columns=['x_axis', 'y_axis', 'values', 'x_label', 'y_label'],
                    data=[
                        [x_axis[i], y_axis[i], values[i], x_label[i], y_label[i]] for i in range(len(x_axis))
                    ]
                ))
            return heatmap_table(x_labels, y_labels, matrix_values, x_axis_label, y_axis_label)
