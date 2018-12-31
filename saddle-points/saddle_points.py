def saddle_points(matrix):
    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise ValueError('All rows need to be of equal length!')

    columns = list(zip(*matrix))

    rows_maximums = [max(row) for row in matrix]
    cols_minimums = [min(col) for col in columns]

    points = {(row_idx, col_idx) for row_idx, row in enumerate(matrix)
              for col_idx, value in enumerate(row)
              if (value == rows_maximums[row_idx] and
                  value == cols_minimums[col_idx])}

    return points
