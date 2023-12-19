md_content = """
# Kidney Disease Classification using MLflow-DVC

## Steps to Run this Project:

### 1. Clone the repo
```
git clone https://github.com/Ape12b/kidney_disease_classification.git
```

### 2. Create a virtual environment and activate it
```
python -m venv .venv
```

### 3. Install requirements
```
pip install -r .\requirements.txt
```




### Notes:

#### 1. Used ConfigBox to access calling dictionary values using "." syntax
```python
from box import ConfigBox

# Create a ConfigBox object
d2 = ConfigBox({"key": "val", "key1": 1})

# Accessing a value using dot notation
print(d2.key1)
```
Output:
``` python
1
```

#### 2. Usign ensure_annotations to typecast

``` python
def get_product(x:int, y:int) -> int:
    return x*y

print(get_product(2, 3))
print(get_product(2, '3')) 

```
Output:
```
6
33

```
This is not what we expected since b needs to be an int. 
We can avoid thisusing ensure_annotation
``` python
from ensure import ensure_annotations
@ensure_annotations
def get_product(x:int, y:int) -> int:
    return x*y

print(get_product(2, 3))
print(get_product(2, '3')) 
```
Output:
```
6
---------------------------------------------------------------------------
EnsureError                               Traceback (most recent call last)
Cell In[11], line 7
      4     return x*y
      6 print(get_product(2, 3))
----> 7 print(get_product(2, '3')) 

File d:\data_science\kidney_disease_classification\.venv\Lib\site-packages\ensure\main.py:845, in WrappedFunctionReturn.__call__(self, *args, **kwargs)
    840     if not isinstance(value, templ):
    841         msg = (
    842             "Argument {arg} of type {valt} to {f} "
    843             "does not match annotation type {t}"
    844         )
--> 845         raise EnsureError(msg.format(
    846             arg=arg, f=self.f, t=templ, valt=type(value)
    847         ))
    849 return_val = self.f(*args, **kwargs)
    850 if not isinstance(return_val, self.return_templ):

EnsureError: Argument y of type <class 'str'> to <function get_product at 0x0000016EBEB68540> does not match annotation type <class 'int'>
```