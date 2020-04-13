# Correct structural index in Euler deconvolution via base-level estimates

by
Felipe F. Melo and Valéria C.F. Barbosa

## About

This paper was published in the journal *Geophysics*. `Melo, F.F., Barbosa, V.C.F., 2018. Correct structural index in Euler deconvolution via base-level estimates. Geophysics 83 (6), J87–J98. https://doi.org/10.1190/geo2017-0774.1`.

This repository contains the source code to perform an additional synthetic test with four sources and a constant base level. The codes `euler_python.py`, the synthetic data `synthetic_data.dat` presented in the paper and the codes `synthetic_test.py`, `estimates_statistics.py` and `plot_functions.py` to generate the results of the synthetic test.

The *euler_python* program is compatible with both Python 2.7 and Python 3.7 programming language.
 
## Abstract

In most applications, the Euler deconvolution aims to define the nature (type) of the geologic source (i.e., the structural index [SI]) and its depth position. However, Euler deconvolution also estimates the horizontal positions of the sources and the base level of the magnetic anomaly. To determine the correct SI, most authors take advantage of the clustering of depth estimates. We have analyzed Euler’s equation to indicate that random variables contaminating the magnetic observations and its gradients affect the base-level estimates if, and only if, the SI is not assumed correctly. Grounded on this theoretical analysis and assuming a set of tentative SIs, we have developed a new criterion for determining the correct SI by means of the minimum standard deviation of base-level estimates. We performed synthetic tests simulating multiple magnetic sources with different SIs. To produce mid and strongly interfering synthetic magnetic anomalies, we added constant and nonlinear backgrounds to the anomalies and approximated the simulated sources laterally. If the magnetic anomalies are weakly interfering, the minima standard deviations either of the depth or base-level estimates can be used to determine the correct SI. However, if the magnetic anomalies are strongly interfering, only the minimum standard deviation of the base-level estimates can determine the SI correctly. These tests also show that Euler deconvolution does not require that the magnetic data be corrected for the regional fields (e.g., International Geomagnetic Reference Field [IGRF]). Tests on real data from part of the Goiás Alkaline Province, Brazil, confirm the potential of the minimum standard deviation of base-level estimates in determining the SIs of the sources by applying Euler deconvolution either to total-field measurements or to total-field anomaly (corrected for IGRF). Our result suggests three plug intrusions giving rise to the Diorama anomaly and dipole-like sources yielding Arenópolis and Montes Claros de Goiás anomalies.

## Content

- euler_python.py:
	General Python module containing the functions to compute de derivatives and 
	Euler deconvolution.
	
- synthetic_test.py:
	Python script to generate the synthetic results. The script loads the total-field
	anomaly of a synthetic model from the file "synthetic_data.dat" and computes the
	Euler deconvolution using the functions in "euler_python.py". The results are 
	generated using the functions "plot_functions.py" for the plots and 
	"estimates_statistics.py" to compute the statistics of the data.
	
- plot_functions.py:
	Python script to generate the figures in the synthetic tests results. 
	
- estimates_statistics.py:
	Python script to compute the mean of the northing, easting and depth estimates. 
	
Test data:

- synthetic_data.dat:
		Synthetic total-field anomaly data generated using the Python packaged
		"Fatiando a Terra": http://fatiando.org/. This data is an example used
		in the current publication.

## Getting the code

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/ffigura/Euler-deconvolution-plateau.git

or [download a zip archive](https://github.com/ffigura/Euler-deconvolution-plateau/archive/master.zip).


## Dependencies

The Python program Euler deconvolution - "euler_python.py" requires the Python library "numpy", 
the scripts "synthetic_test.py" and "plot_functions.py" require the Python packages "numpy"
and "matplotlib", and the script "estimates_statistics.py" requires the Python package "numpy".
The easier way to get Python and all libraries installed is through the Anaconda Python 
distribution (https://www.anaconda.com/distribution/). After installed Anaconda, install the libraries 
by running the following command in your terminal:

	conda install numpy matplotlib

The program for Euler deconvolution "euler_python.py" and the additional codes "synthetic_test.py",
"plot_functions.py" and "estimates_statistics.py" are compatible with both Python 2.7 and 3.7.

## Reproducing the results

The results and figures for the synthetic test are reproducible from the folder `/test_4_sources`.
Running the code `synthetic_test.py` will allow the reprodution of the results. For more information
read the file `README.MD` or `README.txt` in the folder `/code`.


## License

All source code is made available under a BSD 3-clause license. You can freely
use and modify the code, without warranty, so long as you provide attribution
to the authors. See `LICENSE.md` for the full license text.

The manuscript text is not open source. The authors reserve the rights to the
article content, which is currently submitted for publication in the
*Geophysics*.
