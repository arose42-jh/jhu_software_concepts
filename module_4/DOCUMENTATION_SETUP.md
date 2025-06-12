module_4
    pizzaorders
        __init__.py
        order.py
        pizza.py
    tests
        __init__.py
        order_test.py
        pizza_test.py
        test_integration.py

# To generate documentation for module_4, follow these steps:

1. Open a terminal in the root of your project (where Makefile is located).
2. Run the following command to generate HTML documentation:
   
   ```powershell
   .\make.bat html
   ```
   
   or, if using WSL or a Unix-like shell:
   
   ```sh
   make html
   ```
3. The generated documentation will be in the `build/html` directory. Open `build/html/index.html` in your browser to view it.

# To document new modules or functions:
- Add docstrings to your Python files in `module_4/pizzaorders/`.
- Re-run the documentation build command above.

# To include all modules automatically:
- In `source/index.rst`, add:

  ```
  .. automodule:: pizzaorders.order
      :members:
  .. automodule:: pizzaorders.pizza
      :members:
  ```

Or use the `.. autosummary::` directive for summary tables.

# Troubleshooting
- Ensure your virtual environment is activated and Sphinx is installed.
- If you add new files, re-run the build command.
