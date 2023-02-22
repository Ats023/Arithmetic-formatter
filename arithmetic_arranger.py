def arithmetic_arranger(problems, bool=False):
    mid_row = []
    top_row = []
    dashed_row = []
    bottom_row = []
    error_present = 0

    for problem in problems:
      if len(problems) > 5:
        error_present = 1
        arranged_problems = 'Error: Too many problems.'
        break
      if '+' in problem:
        a, b = problem.split(' + ')
        if len(a) > 4 or len(b) > 4:
          error_present = 1
          arranged_problems = 'Error: Numbers cannot be more than four digits.'
          break
        try:
          res = int(a) + int(b)
        except ValueError:
          error_present = 1
          arranged_problems = 'Error: Numbers must only contain digits.'
          break
        sp_pad = abs(len(a) - len(b))
        if len(a) > len(b):
          b = ' ' * sp_pad + b
        elif len(b) > len(a):
          a = ' ' * sp_pad + a
        mid_row.append(('+ ' + b))
      elif '-' in problem:
        a, b = problem.split(' - ')
        if len(a) > 4 or len(b) > 4:
          error_present = 1
          arranged_problems = 'Error: Numbers cannot be more than four digits.'
          break
        try:
          res = int(a) - int(b)
        except ValueError:
          error_present = 1
          arranged_problems = 'Error: Numbers must only contain digits.'
          break
        sp_pad = abs(len(a) - len(b))
        if len(a) > len(b):
          b = ' ' * sp_pad + b
        elif len(b) > len(a):
          a = ' ' * sp_pad + a
        mid_row.append(('- ' + b))
      else:
        error_present = 1
        arranged_problems = "Error: Operator must be '+' or '-'."
        break
      top_row.append(' ' * 2 + a)
      res_sp = len('  ' + b) - len(str(res))
      bottom_row.append(' ' * res_sp + str(res))

    if error_present == 1:
      return arranged_problems
    else:
      for x in mid_row:
        dashed_row.append('-' * len(x))

      dashed_row_final = '    '.join(dashed_row)
      top_row_final = '    '.join(top_row)
      mid_row_final = '    '.join(mid_row)
      bottom_row_final = '    '.join(bottom_row)

      if bool:
        arranged_problems = "\n".join(
          (top_row_final, mid_row_final, dashed_row_final, bottom_row_final))
      else:
        arranged_problems = "\n".join(
          (top_row_final, mid_row_final, dashed_row_final))

    return arranged_problems
