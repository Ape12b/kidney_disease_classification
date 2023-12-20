# Kidney Disease Classification using MLflow-DVC

## Workflows:

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

## Steps to Run this Project:

### 1. Clone the repo
``` bash
git clone https://github.com/Ape12b/kidney_disease_classification.git
```

### 2. Create a virtual environment and activate it
``` bash
python -m venv .venv
```

### 3. Install requirements
``` bash
pip install -r .\requirements.txt
```

## Steps with DVC

### 1. Create the dvc.yaml file

``` bash
dvc init
dvc repro
```

If you run the command again without changing anything:

``` bash
dvc repro      
Stage 'data_ingestion' didn't change, skipping
Stage 'base_model_preparation' didn't change, skipping
Stage 'model_training' didn't change, skipping
Stage 'model_evaluation' didn't change, skipping
Data and pipelines are up to date.
```
You can run dag command to look at the pipeline:

``` bash
$ dvc dag
+----------------+                  +------------------------+ 
| data_ingestion |**                | base_model_preparation |
+----------------+  ******          +------------------------+
         *                *******                *
         *                       ******          *
         *                             ****      *
         **                             +----------------+
           ****                         | model_training |
               ***                      +----------------+
                  ***                 ***
                     ****         ****
                         **     **
                   +------------------+
                   | model_evaluation |
                   +------------------+
```

## Model used: VGG-16 (Visual Geometry Group Model)

![VGG-16](/research/images/vgg16.png)


VGG-16 is a convolutional neural network (CNN) architecture proposed by the Visual Geometry Group at the University of Oxford. It gained popularity for its simplicity and effectiveness in image classification tasks. The "16" in VGG-16 refers to the total number of weight layers in the network.

### Architecture

- The network consists of 16 layers, including 13 convolutional layers and 3 fully connected layers.
- Convolutional layers use small 3x3 filters with a stride of 1 and a padding of 1, maintaining spatial resolution.
- Max-pooling layers with 2x2 filters and a stride of 2 are used for downsampling.

### Depth

- VGG-16 has a deep architecture, surpassing many previous models at the time of its introduction.

### Filter Size and Stride

- Convolutional layers use 3x3 filters with a stride of 1, capturing finer details.

### Pooling

- Max-pooling layers follow convolutional blocks, reducing spatial dimensions hierarchically.

### Fully Connected Layers

- Three fully connected layers with 4096, 4096, and 1000 neurons, respectively.

### Activation Function

- ReLU is used as the activation function, except for the output layer where softmax is applied.

### Batch Normalization

- Batch normalization is used to normalize activations for training stability.

### Dropout

- Dropout is applied in fully connected layers to reduce overfitting during training.

VGG-16 achieved excellent results in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2014, demonstrating the effectiveness of deep CNNs for image classification tasks. While surpassed by newer architectures, VGG-16 remains a benchmark in deep learning development.

Here, the last layer has 2 neurons for the number of classes in the Kidney classification dataset.

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
