# Pypfm
Python pfm files reader. Fast and python3 compatible, with compression included

Install
```
pip install pypfm
```

If you know the size upfront, specify it:
```python
from pypfm import PFMLoader
loader = PFMLoader((width, height), color=False, compress=False)
```
Otherwise it will find it by itself (slower):
```python
from pypfm import PFMLoader
loader = PFMLoader(color=False, compress=False)
```

Read a pfm file
```python
pfm = loader.load_pfm('test.pfm')
```

Save a pfm file:
```python
loader.save_pfm('test.pfm', pfm)
```

Using zfp compression:

```python
from pypfm import PFMLoader
loader = PFMLoader(color=False, compress=True)
pfm = loader.load_pfm('test.pfm')
loader.save_pfm('test.pfm', pfm)
```
