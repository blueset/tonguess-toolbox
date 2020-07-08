Tonguess Toolkit
================

Read more in the [blog article](https://blog.1a23.com/?p=15823).

## Files
* `build_mapping.py`: Build guess-feedback mappings.
* `dict`: Full dictionary text
* `dict3`: Dictionary of 3 letter words
* `dict4`: Dictionary of 4 letter words
* `entropy_tree.py`: Build the entropy trees
* `entropy_tree.svg`: Visualization of the entropy trees
* `entropy_tree3`: Pickle of entropy tree of length 3
* `entropy_tree3.json`: JSON of entropy tree of length 3
* `entropy_tree4`: Pickle of entropy tree of length 4
* `entropy_tree4.json`: JSON of entropy tree of length 4
* `guess.py`: Word guessing helper functions
* `interactive.py`: CLI solver
* `mapping3`: Mapping for 3 letter words (need to build)
* `mapping4`: Mapping for 4 letter words (need to build)
* `std_dev.py`: Standard deviation helper functions
* `stdev_tree.py`: Build the standard deviation trees
* `stdev_tree3`: Pickle of standard deviation tree of length 3
* `stdev_tree3.json`: JSON of standard deviation tree of length 3
* `stdev_tree4`: Pickle of standard deviation tree of length 4
* `stdev_tree4.json`: JSON of standard deviation tree of length 4
* `translate.py`: Translate the pickled tree to JSON
* `tree_stats.py`: Statistics about trees built
* `visualize_freemind.py`: Build visualization of trees for FreeMind
* `visualize_graphviz.py`: Build visualization of trees for GraphViz
* Web interface
  * `index.html`: Landing page
  * `interactive.html`: The solver
  * `lookup.html`: The filter
  * `data.js`: Data of the entropy tree
  * `data_stdev.js`: Data used for standard deviation tree version
  * `tonguess-toolbox.svg`: The logo


## Build and run

```sh
# Build mappings
python3 build_mappings.py 3
python3 build_mappings.py 4

# Build entropy tree
python3 entropy_tree.py 3
python3 entropy_tree.py 4

# Translate the trees to JSON
python3 translate.py entropy_tree

# Start the CLI solver
python3 interactive.py entropy_tree
```


# License

```
MIT License

Copyright (c) 2020 Eana Hufwe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
