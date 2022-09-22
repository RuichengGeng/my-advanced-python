This topic is about Python objects cross reference issue and garbage collection
Some related posts:
-  [circular-reference-in-python](https://pencilprogrammer.com/circular-reference-in-python/)
- [circular-references-without-memory-leaks-and-destruction-of-objects-in-python](https://medium.com/@chipiga86/circular-references-without-memory-leaks-and-destruction-of-objects-in-python-43da57915b8d)

## Findings: 
1. Please pay special attention to the order or memory profile and delete message:
   1. when using weak reference, objects are deleted when loop finished
   2. when not using weak reference, objects are only deleted when program ends
2. Please pay special attention to process memory usage, weak reference will make python GC effectively delete useless data and save memory use(aviod memory leak)
3. Circular reference are often encountered 
   1. In some often used data structures, especially in tree and list
   2. When classes are not very well organized.`it is normal practice to break code with one-way abstraction levels when the lower level knows nothing about the higher level and the higher one uses the lower level for any action`

### Update1: 2022-09-22
add anytree.Node based tree node based example, from the log file, we can find that:
1. anytree.Node is memory inefficient in constructing trees, memory released only after program end. 
2. newly implement node(MyEfficientNode) use weak reference, python GC will collect garbage in loop, memory efficient!