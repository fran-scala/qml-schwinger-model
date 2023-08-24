# Symmetrizing Quantum Machine Learning for Quantum Field Theory

Classification of QFT Schwinger model states by means of a symmetry-aware QML algorithm

### Schwinger
This folder contains all the Python code for the Quantum Field theory analysis using geometric quantum machine learning techniques. The sub-folders are `asymmetric` and `symmetric`, which contain the results from the experiments.

In addition, you have three iPython files used to run the experiments:

- `Schwinger_circuit_asym.ipynb`: quantum Neural Network model classifying Schwinger states without exploiting symmetries.
- `Schwinger_circuit.ipynb`: quantum Neural Network model classifying Schwinger states **exploiting symmetries**.
- `classical_NN.ipynb`: classical Neural Network model classifying Schwinger states.
- `dataset_generator.py`: file is used to generate the dataset.

## Requirements

For executing the quantum ML codes, the following Python libraries are required in the mentioned versions:
```
numpy 1.23.0
matplotlib 3.6.2
pennylane 0.29.1
jax 0.3.13
optax 0.1.3
jaxlib 0.3.10
jaxopt 0.8
```

The classical ML code was executed on Colab.
