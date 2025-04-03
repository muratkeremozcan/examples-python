def function_with_long_parameters(
    parameter1,
    parameter2,
    parameter3="default",
):
  """This is a test function to demonstrate the indentation."""
  # Function body with 2-space indentation
  result = parameter1 + parameter2
  return result


# Regular function with docstring
def check_outputs(result):
  """Ensures that the result is not None and is a list."""
  if result is None:
    raise ValueError("Function output is None!")
  # For example, if we expect a list:
  if not isinstance(result, list):
    raise ValueError("Function output is not a list!")
